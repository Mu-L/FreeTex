#!/bin/bash

# FreeTex 无签名 DMG 创建脚本
# 适用于没有 Apple Developer 账号的情况

set -e

# 配置
VERSION="${1:-1.0.0}"
APP_NAME="FreeTex"
APP_PATH="dist/FreeTex.app"
DMG_NAME="FreeTex-Installer"
OUTPUT_DIR="release"

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 欢迎信息
echo ""
echo "╔════════════════════════════════════════╗"
echo "║   FreeTex DMG 创建脚本（无签名）     ║"
echo "╚════════════════════════════════════════╝"
echo ""
log_info "版本: $VERSION"
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

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 删除旧的 DMG
if [ -f "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg" ]; then
    log_warn "删除旧的 DMG: $OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
    rm -f "$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
fi

# 移除隔离属性（非常重要！）
log_info "移除应用的隔离属性..."
xattr -cr "$APP_PATH"
log_info "✅ 隔离属性已移除"

# 创建 DMG
log_info "正在创建 DMG..."
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

# 显示文件信息
DMG_PATH="$OUTPUT_DIR/$DMG_NAME-$VERSION.dmg"
DMG_SIZE=$(du -h "$DMG_PATH" | cut -f1)
log_info "文件位置: $DMG_PATH"
log_info "文件大小: $DMG_SIZE"

# 计算 SHA256
log_info "计算 SHA256..."
SHA256=$(shasum -a 256 "$DMG_PATH" | awk '{print $1}')
echo "$SHA256" > "$OUTPUT_DIR/$DMG_NAME-$VERSION.sha256"
log_info "SHA256: $SHA256"
log_info "SHA256 已保存到: $OUTPUT_DIR/$DMG_NAME-$VERSION.sha256"

# 测试 DMG
log_info "验证 DMG..."
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
log_info "2. 创建 GitHub Release:"
echo "   gh release create v$VERSION \\"
echo "     $DMG_PATH \\"
echo "     --title \"FreeTex v$VERSION\" \\"
echo "     --notes \"发布说明\""
echo ""
log_info "3. 更新 Homebrew Tap 的 SHA256:"
echo "   $SHA256"
echo ""
log_info "4. 或运行完整发布脚本:"
echo "   ./scripts/release_unsigned.sh $VERSION YOUR_USERNAME"
echo ""
