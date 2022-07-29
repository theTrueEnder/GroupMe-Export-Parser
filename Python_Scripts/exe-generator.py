import PyInstaller.__main__
import os

print(os.getcwd())
os.chdir('Github/GroupMe-Export-Parser')
PyInstaller.__main__.run([
    'Python_Scripts/main.py',
    '--onefile',
    '--windowed',
#    '--icon=icon.ico',
    '--name=GroupMe-Export-Parser',
    '--distpath=./',
    '--workpath=./.build',

])