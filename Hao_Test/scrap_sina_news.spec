# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['scrap_sina_news.py'],
             pathex=['C:\\Users\\hao.ren3\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\Jupyter', 'C:\\Users\\hao.ren3\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\Jupyter\\python_scraping\\Hao_Test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='scrap_sina_news',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
