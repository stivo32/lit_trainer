call venv\Scripts\activate.bat
pyinstaller cli.spec
ren dist\cli.exe lit_trainer.exe
copy dist\lit_trainer.exe .
rmdir /s /q build
rmdir /s /q dist
call venv\Scripts\deactivate.bat