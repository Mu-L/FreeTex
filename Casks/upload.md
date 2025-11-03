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

brew tap zstar1003/homebrew-freetex
brew install --cask freetex

签名/公证流程：

1) 生成 .app
2) 签名 app (codesign)
3) 打包成 .dmg / .zip / .pkg
4) 提交公证 (notarytool submit)
5) staple（附着公证票据）
6) 发布文件

# 使用 PyInstaller 打包
pyinstaller main.spec

# 验证应用签名
codesign -vvv --deep --strict dist/FreeTex.app

# 查看签名信息
codesign -dvvv dist/FreeTex.app

# 验证 Gatekeeper 是否允许运行
spctl -a -vvv dist/FreeTex.app

注意事项

- Developer ID 签名:使用的是 Developer ID
Application 证书,适用于在 App Store 外分发
- 如果要提交到 Apple 进行公证(notarization),需要额外步骤:

# 创建 DMG 后进行公证
xcrun notarytool submit
release/FreeTex-Installer-1.0.0.dmg \
    --apple-id 自己appid \
    --team-id 自己的team \
    --password 新密码 \
    --wait

# 公证完成后装订票据 
xcrun stapler staple release/FreeTex-Installer-1.0.0.dmg