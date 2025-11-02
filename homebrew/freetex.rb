cask "freetex" do
  version "1.0.0"
  sha256 "YOUR_SHA256_HERE"  # 运行 release.sh 后会显示

  url "https://github.com/YOUR_USERNAME/FreeTex/releases/download/v#{version}/FreeTeX-Installer-#{version}.dmg"
  name "FreeTeX"
  desc "Free intelligent formula recognition tool powered by AI"
  homepage "https://github.com/YOUR_USERNAME/FreeTex"

  # 系统要求
  depends_on macos: ">= :big_sur"

  # 安装应用
  app "FreeTeX.app"

  # 卸载时的清理
  zap trash: [
    "~/Library/Application Support/FreeTex",
    "~/Library/Caches/FreeTex",
    "~/Library/Preferences/com.freetex.app.plist",
    "~/Library/Saved Application State/com.freetex.app.savedState",
  ]

  # 使用说明
  caveats do
    <<~EOS
      FreeTeX 已安装完成！

      使用方法：
      1. 打开应用：在 Launchpad 中找到 FreeTeX
      2. 授予权限：首次运行需要授予屏幕录制权限
      3. 开始使用：使用快捷键 Ctrl+Alt+Q 截图识别公式

      更多信息请访问：https://github.com/YOUR_USERNAME/FreeTex
    EOS
  end
end
