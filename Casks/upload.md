# Homebrew 上传流程

1. brew tap --force homebrew/cask

2. brew create --cask "https://github.com/zstar1003/FreeTex/releases/download/v1.0.0/FreeTex-Installer-1.0.0.dmg" --set-name FreeTex

# EDITOR 会打开模板，填写 version、sha256、url、name、app、homepage 等字段

3. 本地测试

export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_NO_INSTALL_FROM_API=1
brew install --cask ./freetex.rb
brew uninstall freetex
brew audit --new --cask freetex
brew style --fix freetex

4. 下载

brew tap zstar1003/FreeTex
brew install --cask freetex