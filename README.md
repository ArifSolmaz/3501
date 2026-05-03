# 3501 Public Project Site

This repository is the public information hub for the TUBITAK 3501 starspot timing-systematics project.
It is designed for GitHub Pages at:

https://arifsolmaz.github.io/3501/

It includes project context, selected figures, the 24-month work plan, public
data-source notes, open-science output plans, and an update page that can be
extended if the project is accepted.

The website is custom static HTML/CSS/JS in `docs/`. Jekyll is disabled with
`docs/.nojekyll`, so there is no GitHub Pages theme layer.

## Publish

```bash
git init
git branch -M main
git add .
git commit -m "Publish 3501 public project site"
gh repo create arifsolmaz/3501 --public --source=. --remote=origin --push
```

Then enable GitHub Pages from the `main` branch and `/docs` folder.

## Update

```bash
git add .
git commit -m "Update public project materials"
git push
```
