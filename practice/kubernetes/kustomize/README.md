cf.
- https://atmarkit.itmedia.co.jp/ait/articles/2101/21/news004.html
- https://github.com/cloudnativecheetsheet/kustomize

# setup
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | zsh

vim ~/.zprofile
---
alias kustomize="/Users/ida/github/hobby/practice/kubernetes/kustomize/kustomize"
---

diff -u <(kustomize build base) <(kustomize build overlays/prod)
