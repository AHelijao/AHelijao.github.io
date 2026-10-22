# Portfolio — Helijao Andriamandranto

Static horizontal deck for **GitHub Pages**. FR / EN toggle (saved in `localStorage`).

## Local preview

```powershell
cd D:\career-factory\portfolio-site
python -m http.server 8765
```

Open http://127.0.0.1:8765

## Publish to GitHub Pages

Recommended: user site repo so the URL is clean.

```powershell
cd D:\career-factory\portfolio-site
git init
git add index.html styles.css script.js i18n.js README.md
git commit -m "Portfolio deck for GitHub Pages"
gh repo create AHelijao.github.io --public --source=. --remote=origin --push
```

Then: repo **Settings → Pages → Deploy from branch `main` / root**.

Live URL: **https://ahelijao.github.io/**

### Notes for Pages

- All asset paths are **relative** (`styles.css`, `script.js`, `i18n.js`) — works at site root.
- No build step; plain HTML/CSS/JS.
- Do not put secrets or private IP in this folder.
- Showcase repos later: link from each chapter when public.

### Alternative

If you prefer a project site: create any public repo, push this folder (or `/docs`), enable Pages — URL becomes `https://ahelijao.github.io/<repo>/`.
