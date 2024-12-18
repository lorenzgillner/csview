csview: csview.py
	pyinstaller --noconfirm --clean --onefile --icon icon.png --name $@ --optimize 2 --strip $<

install: dist/csview
	cp $< ~/.local/bin/
