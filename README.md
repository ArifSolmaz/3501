# 3501 Pre-Analysis Public Site

This repository is the public information and pre-analysis hub for the TUBITAK 3501 project.
It is designed for GitHub Pages at:

https://arifsolmaz.github.io/3501/

It includes selected figures, audit summaries, archive query manifests,
reproducibility scripts, reviewer information, and a project-update page that can
be extended if the project is accepted.

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
