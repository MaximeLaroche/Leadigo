(function () {
    const SUPPORTED = ['en', 'fr', 'es'];
    const FLAGS = [
        ['en', 'English version', '🇬🇧'],
        ['fr', 'Version française', '🇫🇷'],
        ['es', 'Versión en español', '🇪🇸']
    ];
    const ATTRS = ['alt', 'aria-label', 'title'];
    const SKIP_TAGS = ['SCRIPT', 'STYLE', 'NOSCRIPT', 'TITLE'];
    const DEFAULT_THEME = {
        themePrefix: 'Theme: ',
        clickSuffix: ' (click to switch)',
        System: 'System',
        Light: 'Light',
        Dark: 'Dark'
    };

    let current = 'en';
    let dict = {};
    let observer = null;
    let applying = false;
    let flagsEl = null;
    const dictCache = { en: Promise.resolve({}) };
    const nodeOriginals = new WeakMap();
    const attrOriginals = new WeakMap();
    const scrubOriginals = new WeakMap();
    const originalTitle = document.title;

    const valid = (lang) => SUPPORTED.includes(lang) ? lang : 'en';
    const detect = () => {
        const saved = localStorage.getItem('leadigo-lang');
        if (saved) return valid(saved);
        const nav = (navigator.language || 'en').toLowerCase();
        if (nav.startsWith('fr')) return 'fr';
        if (nav.startsWith('es')) return 'es';
        return 'en';
    };
    const load = (lang) => {
        if (!dictCache[lang]) {
            dictCache[lang] = fetch(`locales/${lang}.json`)
                .then((r) => r.ok ? r.json() : {})
                .catch(() => ({}));
        }
        return dictCache[lang];
    };
    const swap = (orig, translated) => {
        const key = orig.trim();
        const at = orig.indexOf(key);
        if (!key || at < 0) return orig;
        return orig.slice(0, at) + translated + orig.slice(at + key.length);
    };
    const translateNode = (node) => {
        const orig = nodeOriginals.get(node);
        if (orig == null) return;
        const key = orig.trim();
        const next = (current !== 'en' && key && dict[key]) ? swap(orig, dict[key]) : orig;
        if (node.nodeValue !== next) node.nodeValue = next;
    };
    const translateAttrs = (root) => {
        if (!root.querySelectorAll) return;
        root.querySelectorAll('*').forEach((el) => {
            if (el.id === 'theme-toggle') return;
            ATTRS.forEach((attr) => {
                if (!el.hasAttribute(attr)) return;
                let store = attrOriginals.get(el);
                if (!store) {
                    store = {};
                    attrOriginals.set(el, store);
                }
                if (!(attr in store)) store[attr] = el.getAttribute(attr);
                const orig = store[attr];
                const key = orig.trim();
                const next = (current !== 'en' && key && dict[key]) ? swap(orig, dict[key]) : orig;
                if (el.getAttribute(attr) !== next) el.setAttribute(attr, next);
            });
        });
    };
    const walk = (root) => {
        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
            acceptNode(node) {
                const parent = node.parentElement;
                if (!parent) return NodeFilter.FILTER_REJECT;
                if (SKIP_TAGS.includes(parent.tagName) || parent.id === 'theme-tip') return NodeFilter.FILTER_REJECT;
                if (parent.closest('.scrub-words')) return NodeFilter.FILTER_REJECT; // handled whole-element by translateScrub
                if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
                return NodeFilter.FILTER_ACCEPT;
            }
        });
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach((node) => {
            if (!nodeOriginals.has(node)) nodeOriginals.set(node, node.nodeValue);
            translateNode(node);
        });
        translateAttrs(root);
    };
    // .scrub-words elements are split into per-word spans by the GSAP animation,
    // so their text nodes never match a full-sentence dictionary key. Translate
    // them at the element level, then re-split via the hook exposed by the page.
    const translateScrub = (root) => {
        if (!root.querySelectorAll) return;
        const els = [];
        if (root.matches && root.matches('.scrub-words')) els.push(root);
        root.querySelectorAll('.scrub-words').forEach((el) => els.push(el));
        els.forEach((el) => {
            if (!scrubOriginals.has(el)) scrubOriginals.set(el, el.textContent);
            const orig = scrubOriginals.get(el);
            const key = orig.trim();
            const next = (current !== 'en' && key && dict[key]) ? swap(orig, dict[key]) : orig;
            if (el.textContent !== next) {
                el.textContent = next;
                if (typeof window.leadigoSplitScrubWords === 'function') window.leadigoSplitScrubWords(el);
            }
        });
    };
    const themeLabels = () => Object.assign({}, DEFAULT_THEME, dict.__theme || {});
    const refreshThemeChrome = () => {
        const toggle = document.getElementById('theme-toggle');
        const tip = document.getElementById('theme-tip');
        if (!toggle || !tip) return;
        const theme = localStorage.getItem('leadigo-theme') || 'system';
        const labelKey = theme === 'light' ? 'Light' : (theme === 'dark' ? 'Dark' : 'System');
        const labels = themeLabels();
        tip.textContent = labels.themePrefix + labels[labelKey];
        toggle.setAttribute('aria-label', labels.themePrefix + labels[labelKey] + labels.clickSuffix);
    };
    const updateFlags = () => {
        if (!flagsEl) return;
        flagsEl.querySelectorAll('.lang-flag').forEach((flag) => {
            if (flag.dataset.lang === current) flag.setAttribute('aria-current', 'page');
            else flag.removeAttribute('aria-current');
        });
    };
    const observe = () => {
        if (observer) return;
        observer = new MutationObserver((mutations) => {
            if (applying) return;
            mutations.forEach((mutation) => {
                if (mutation.type === 'characterData') {
                    const node = mutation.target;
                    if (node.parentElement && node.parentElement.id === 'theme-tip') return;
                    nodeOriginals.set(node, node.nodeValue);
                    translateNode(node);
                } else {
                    mutation.addedNodes.forEach((node) => {
                        if (node.nodeType === Node.TEXT_NODE) {
                            if (!nodeOriginals.has(node)) nodeOriginals.set(node, node.nodeValue);
                            translateNode(node);
                        } else if (node.nodeType === Node.ELEMENT_NODE) {
                            walk(node);
                            translateScrub(node);
                        }
                    });
                }
            });
        });
        observer.observe(document.body, { childList: true, subtree: true, characterData: true });
    };
    const broadcast = () => {
        document.querySelectorAll('iframe').forEach((frame) => {
            if (frame.contentWindow) frame.contentWindow.postMessage({ type: 'leadigo-lang', lang: current }, '*');
        });
    };
    const apply = () => {
        applying = true;
        if (observer) observer.disconnect();
        walk(document);
        translateScrub(document);
        document.documentElement.lang = current;
        const titleKey = originalTitle.trim();
        document.title = (current !== 'en' && dict[titleKey]) ? dict[titleKey] : originalTitle;
        refreshThemeChrome();
        updateFlags();
        applying = false;
        observer = null;
        observe();
    };
    const setLanguage = async (lang, options = {}) => {
        current = valid(lang);
        if (options.persist !== false) localStorage.setItem('leadigo-lang', current);
        dict = await load(current);
        apply();
        if (options.broadcast !== false) broadcast();
    };
    window.leadigoSetLang = setLanguage;

    const style = document.createElement('style');
    style.textContent = `
        .lang-flags { display: flex; align-items: center; gap: 0.25rem; }
        .lang-flag {
            width: 1.9rem; height: 1.9rem; border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.35);
            display: flex; align-items: center; justify-content: center;
            font-size: 0.9rem; line-height: 1; text-decoration: none;
            opacity: 0.55; background: transparent; cursor: pointer; padding: 0;
            transition: opacity 0.2s ease, border-color 0.2s ease, background-color 0.2s ease;
        }
        .lang-flag:hover { opacity: 1; border-color: rgba(96, 165, 250, 0.5); }
        .lang-flag[aria-current="page"] { opacity: 1; border-color: rgba(96, 165, 250, 0.65); background-color: rgba(30, 41, 59, 0.6); }
        html.light .lang-flag { border-color: rgba(15, 23, 42, 0.16); }
        html.light .lang-flag[aria-current="page"] { background-color: rgba(219, 234, 254, 0.7); }
        @media (max-width: 480px) {
            .lang-flags { gap: 0.1rem; }
            .lang-flag { width: 1.6rem; height: 1.6rem; font-size: 0.8rem; }
        }
    `;
    document.head.appendChild(style);

    flagsEl = document.createElement('div');
    flagsEl.className = 'lang-flags';
    FLAGS.forEach(([code, label, flag]) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.textContent = flag;
        button.className = 'lang-flag';
        button.dataset.lang = code;
        button.setAttribute('aria-label', label);
        button.addEventListener('click', () => setLanguage(code));
        flagsEl.appendChild(button);
    });

    const isEmbedded = document.body.classList.contains('is-embedded') || window.self !== window.top;
    const fab = document.querySelector('.theme-fab');
    if (fab && !isEmbedded) {
        fab.style.display = 'flex';
        fab.style.alignItems = 'center';
        fab.style.gap = '0.5rem';
        fab.insertBefore(flagsEl, fab.firstChild);
    } else if (!fab) {
        const themeWrap = document.querySelector('.theme-wrap');
        if (themeWrap && themeWrap.parentNode) themeWrap.parentNode.insertBefore(flagsEl, themeWrap);
    }

    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) themeToggle.addEventListener('click', () => setTimeout(refreshThemeChrome, 0));
    window.addEventListener('storage', (event) => {
        if (event.key === 'leadigo-theme') refreshThemeChrome();
        if (event.key === 'leadigo-lang' && event.newValue) setLanguage(event.newValue, { broadcast: false });
    });
    window.addEventListener('message', (event) => {
        if (event.data && event.data.type === 'leadigo-lang') {
            setLanguage(event.data.lang, { persist: false, broadcast: false });
        }
    });
    document.querySelectorAll('iframe').forEach((frame) => {
        frame.addEventListener('load', () => {
            if (frame.contentWindow) frame.contentWindow.postMessage({ type: 'leadigo-lang', lang: current }, '*');
        });
    });

    setLanguage(detect(), { broadcast: false });
})();
