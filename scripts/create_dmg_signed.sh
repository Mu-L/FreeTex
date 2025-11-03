#!/bin/bash

# FreeTex 签名 DMG 创建脚本
# 适用于有 Apple Developer 账号的情况

set -e

# 配置
VERSION="${1:-1.0.0}"
APP_NAME="FreeTex"
APP_PATH="dist/FreeTex.app"
DMG_NAME="FreeTex-Installer"
OUTPUT_DIR="release"

# 签名配置
SIGNING_IDENTITY="Developer ID Application: Xingyu Zhang (8VG8TNH2F2)"
TEAM_ID="8VG8TNH2F2"

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }
log_step() { echo -e "${BLUE}[STEP]${NC} $1"; }

# 欢迎信息
echo ""
echo "╔════════════════════════════════════════╗"
echo "║   FreeTex DMG 创建脚本（签名版本）   ║"
echo "╚════════════════════════════════════════╝"
echo ""
log_info "版本: $VERSION"
log_info "签名证书: $SIGNING_IDENTITY"
echo ""

# 检查应用
if [ ! -d "$APP_PATH" ]; then
    log_error "应用不存在: $APP_PATH"
    log_info "请先运行: pyinstaller main.spec"
    exit 1
fi

# 检查工具
if ! command -v create-dmg &> /dev/null; then
    log_error "create-dmg 未安装"
    log_info "请运行: brew install create-dmg"
    exit 1
fi

# 检查签名证书
log_step "检查签名证书..."
if ! security find-identity -v -p codesigning | grep -q "$SIGNING_IDENTITY"; then
    log_error "未找到签名证书: $SIGNING_IDENTITY"
    log_info "请检查您的开发者证书是否正确安装"
    exit 1
fi
log_info "✅ 签名证书验证通过"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 删除旧的 DMG
if [ -f "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg" ]; then
    log_warn "删除旧的 DMG: $OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
    rm -f "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
fi

# 移除隔离属性
log_step "移除应用的隔离属性..."
xattr -cr "$APP_PATH"
log_info "✅ 隔离属性已移除"

# 验证应用签名
log_step "验证应用签名..."
if codesign -vvv --deep --strict "$APP_PATH" 2>&1 | grep -q "valid on disk"; then
    log_info "✅ 应用签名有效"
    codesign -dvvv "$APP_PATH" 2>&1 | grep "Authority=" | head -n 1
else
    log_warn "应用签名验证失败，但继续创建 DMG"
    log_info "PyInstaller 应该已经在打包时进行了签名"
fi

# 创建 DMG
log_step "正在创建 DMG..."
create-dmg \
  --volname "$APP_NAME Installer" \
  --volicon "resources/images/icon.icns" \
  --window-pos 200 120 \
  --window-size 800 450 \
  --icon-size 100 \
  --icon "$APP_NAME.app" 200 190 \
  --hide-extension "$APP_NAME.app" \
  --app-drop-link 600 185 \
  --hdiutil-quiet \
  "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg" \
  "$APP_PATH"

log_info "✅ DMG 创建成功"

# 对 DMG 进行签名
log_step "对 DMG 进行签名..."
codesign --sign "$SIGNING_IDENTITY" \
         --force \
         --timestamp \
         "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"

if [ $? -eq 0 ]; then
    log_info "✅ DMG 签名成功"
else
    log_error "DMG 签名失败"
    exit 1
fi

# 验证 DMG 签名
log_step "验证 DMG 签名..."
codesign -vvv --deep --strict "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
if [ $? -eq 0 ]; then
    log_info "✅ DMG 签名验证通过"
else
    log_error "DMG 签名验证失败"
    exit 1
fi

# 显示文件信息
DMG_PATH="$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
DMG_SIZE=$(du -h "$DMG_PATH" | cut -f1)
log_info "文件位置: $DMG_PATH"
log_info "文件大小: $DMG_SIZE"

# 计算 SHA256
log_step "计算 SHA256..."
SHA256=$(shasum -a 256 "$DMG_PATH" | awk '{print $1}')
echo "$SHA256" > "$OUTPUT_DIR/$DMG_NAME-$VERSION.sha256"
log_info "SHA256: $SHA256"
log_info "SHA256 已保存到: $OUTPUT_DIR/$DMG_NAME-$VERSION.sha256"

# 测试 DMG
log_step "验证 DMG..."
hdiutil verify "$DMG_PATH" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    log_info "✅ DMG 验证通过"
else
    log_warn "DMG 验证失败，但这通常不影响使用"
fi

# 下一步提示
echo ""
echo "╔════════════════════════════════════════╗"
echo "║   下一步操作                          ║"
echo "╚════════════════════════════════════════╝"
echo ""
log_info "1. 测试 DMG（推荐）:"
echo "   open $DMG_PATH"
echo ""
log_info "2. 【可选】对 DMG 进行公证（推荐用于正式发布）:"
echo "   # 需要 App-Specific Password from appleid.apple.com"
echo "   xcrun notarytool submit $DMG_PATH \\"
echo "     --apple-id YOUR_APPLE_ID \\"
echo "     --team-id $TEAM_ID \\"
echo "     --password YOUR_APP_SPECIFIC_PASSWORD \\"
echo "     --wait"
echo ""
echo "   # 公证完成后，装订公证票据:"
echo "   xcrun stapler staple $DMG_PATH"
echo ""
log_info "3. 创建 GitHub Release:"
echo "   gh release create v$VERSION \\"
echo "     $DMG_PATH \\"
echo "     --title \"FreeTex v$VERSION\" \\"
echo "     --notes \"发布说明\""
echo ""
log_info "4. 更新 Homebrew Tap 的 SHA256:"
echo "   $SHA256"
echo ""
log_warn "注意: 公证过程可能需要几分钟到几小时不等"
log_info "公证后的应用在其他 Mac 上安装时不会显示安全警告"
echo ""
