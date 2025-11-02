# -*- mode: python ; coding: utf-8 -*-
import sys
import os

# 检测平台
is_mac = sys.platform == 'darwin'
is_windows = sys.platform == 'win32'

# 根据平台设置路径
if is_windows:
    site_packages = ".venv/Lib/site-packages"
    icon_file = 'resources/images/icon.ico'
else:  # macOS/Linux
    site_packages = ".venv/lib/python3.10/site-packages"
    icon_file = 'resources/images/icon.icns' if is_mac else 'resources/images/icon.ico'

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("./demo.yaml", "."),
        ("./config.json", "."),
        ("./unimernet/configs", "unimernet/configs"),
        ("./models/unimernet_small/*.json", "models/unimernet_small"),
        ("./models/unimernet_small/*.pth", "models/unimernet_small"),
        (os.path.join(site_packages, "transformers/models/gemma2"), "transformers/models/gemma2"),
        (os.path.join(site_packages, "latex2mathml/unimathsymbols.txt"), "latex2mathml"),  # 添加 latex2mathml 数据文件
        ("libs/katex", "libs/katex"),
        ("resources", "resources")  # 添加资源文件夹
    ],
    hiddenimports=[
        "unimernet",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FreeTex',  # The name of the executable
    icon=icon_file,  # 使用平台相关的图标
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FreeTex',
)

app = BUNDLE(
    coll,
    name='FreeTex.app',
    icon='resources/images/icon.icns',  # macOS App 图标
    bundle_identifier='com.freetex.app',
)