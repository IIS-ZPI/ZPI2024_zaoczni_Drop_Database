# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/UI/Control.py'],
    pathex=[],
    binaries=[],
    datas=[('src/UI', 'UI'), ('src/nbp', 'nbp'),('src/UI/images','images')],
    hiddenimports=['UI.MainScreen', 'nbp.data_analysis', 'nbp.data_types', 'nbp.nbp_repository','scipy','scipy.stats','requests','matplotlib'],
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
    a.binaries,
    a.datas,
    [],
    name='Control',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
