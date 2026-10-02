(function () {
    const path = location.pathname;
    let file = path.substring(path.lastIndexOf('/') + 1) || 'index.html';
    if (!file.endsWith('.html')) file = 'index.html';

    const isFr = /-fr\.html$/.test(file) || document.documentElement.lang === 'fr';
    localStorage.setItem('leadigo-lang', isFr ? 'fr' : 'en');

    const enFile = isFr ? file.replace(/-fr\.html$/, '.html') : file;
    const frFile = isFr ? file : file.replace(/\.html$/, '-fr.html');

    // Keep page-to-page navigation in the selected language.
    const pageNames = ['index.html', 'roi_calculator.html', 'strategy_call.html', 'index-fr.html', 'roi_calculator-fr.html', 'strategy_call-fr.html'];
    document.querySelectorAll('a[href]').forEach((a) => {
        const href = a.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto:')) return;
        if (!pageNames.includes(href)) return;
        if (isFr && !href.includes('-fr.html')) {
            a.setAttribute('href', href.replace('.html', '-fr.html'));
        } else if (!isFr && href.includes('-fr.html')) {
            a.setAttribute('href', href.replace('-fr.html', '.html'));
        }
    });

    const style = document.createElement('style');
    style.textContent = `
        .lang-flags { display: flex; align-items: center; gap: 0.25rem; }
        .lang-flag {
            width: 2rem;
            height: 2rem;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
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
            .lang-flag { width: 1.75rem; height: 1.75rem; font-size: 0.85rem; }
        }
    `;
    document.head.appendChild(style);

    const makeFlag = (href, label, flag, active) => {
        const a = document.createElement('a');
        a.href = href;
        a.textContent = flag;
        a.className = 'lang-flag';
        a.setAttribute('aria-label', label);
        if (active) a.setAttribute('aria-current', 'page');
        return a;
    };

    const flags = document.createElement('div');
    flags.className = 'lang-flags';
    flags.appendChild(makeFlag(enFile, 'English version', '🇬🇧', !isFr));
    flags.appendChild(makeFlag(frFile, 'Version française', '🇫🇷', isFr));

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
