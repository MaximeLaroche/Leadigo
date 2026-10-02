(function () {
    const path = location.pathname;
    let file = path.substring(path.lastIndexOf('/') + 1) || 'index.html';
    if (!file.endsWith('.html')) file = 'index.html';

    const lang = file.includes('-fr.html') ? 'fr' : (file.includes('-es.html') ? 'es' : 'en');
    localStorage.setItem('leadigo-lang', lang);

    const base = file.replace('-fr.html', '.html').replace('-es.html', '.html');
    const localized = (baseName, targetLang) => targetLang === 'en' ? baseName : baseName.replace('.html', `-${targetLang}.html`);
    const pageBases = ['index.html', 'roi_calculator.html', 'strategy_call.html'];

    // Keep page-to-page navigation and embedded apps in the selected language.
    document.querySelectorAll('a[href], iframe[src]').forEach((el) => {
        const attr = el.tagName === 'IFRAME' ? 'src' : 'href';
        const value = el.getAttribute(attr);
        if (!value || value.startsWith('#') || value.startsWith('http') || value.startsWith('mailto:')) return;
        const valueBase = value.replace('-fr.html', '.html').replace('-es.html', '.html');
        if (!pageBases.includes(valueBase)) return;
        el.setAttribute(attr, localized(valueBase, lang));
    });

    const style = document.createElement('style');
    style.textContent = `
        .lang-flags { display: flex; align-items: center; gap: 0.25rem; }
        .lang-flag {
            width: 1.9rem;
            height: 1.9rem;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
            line-height: 1;
            text-decoration: none;
            opacity: 0.55;
            transition: opacity 0.2s ease, border-color 0.2s ease, background-color 0.2s ease;
        }
        .lang-flag:hover { opacity: 1; border-color: rgba(96, 165, 250, 0.5); }
        .lang-flag[aria-current="page"] {
            opacity: 1;
            border-color: rgba(96, 165, 250, 0.65);
            background-color: rgba(30, 41, 59, 0.6);
        }
        html.light .lang-flag { border-color: rgba(15, 23, 42, 0.16); }
        html.light .lang-flag[aria-current="page"] { background-color: rgba(219, 234, 254, 0.7); }
        @media (max-width: 480px) {
            .lang-flags { gap: 0.1rem; }
            .lang-flag { width: 1.6rem; height: 1.6rem; font-size: 0.8rem; }
        }
    `;
    document.head.appendChild(style);

    const makeFlag = (code, label, flag) => {
        const a = document.createElement('a');
        a.href = localized(base, code);
        a.textContent = flag;
        a.className = 'lang-flag';
        a.setAttribute('aria-label', label);
        if (code === lang) a.setAttribute('aria-current', 'page');
        return a;
    };

    const flags = document.createElement('div');
    flags.className = 'lang-flags';
    flags.appendChild(makeFlag('en', 'English version', '🇬🇧'));
    flags.appendChild(makeFlag('fr', 'Version française', '🇫🇷'));
    flags.appendChild(makeFlag('es', 'Versión en español', '🇪🇸'));

    const fab = document.querySelector('.theme-fab');
    if (fab) {
        fab.style.display = 'flex';
        fab.style.alignItems = 'center';
        fab.style.gap = '0.5rem';
        fab.insertBefore(flags, fab.firstChild);
        return;
    }

    const themeWrap = document.querySelector('.theme-wrap');
    if (themeWrap && themeWrap.parentNode) {
        themeWrap.parentNode.insertBefore(flags, themeWrap);
    }
})();
