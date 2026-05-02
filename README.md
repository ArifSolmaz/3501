# 3501 Pre-Analysis Public Site

This repository is a public-facing subset of the TUBITAK 3501 pre-analysis work.
It is designed for GitHub Pages at:

https://arifsolmaz.github.io/3501/

Only public-safe materials are included: selected figures, audit summaries,
archive query manifests, and reproducibility scripts. The full application
forms, budget files, personal/provenance material, and large cached raw data are
intentionally excluded.

## Publish

```bash
git init
git branch -M main
git add .
git commit -m "Publish 3501 pre-analysis site"
gh repo create arifsolmaz/3501 --public --source=. --remote=origin --push
```

Then enable GitHub Pages from the `main` branch and `/docs` folder.

## Update

```bash
git add .
git commit -m "Update public pre-analysis materials"
git push
```

