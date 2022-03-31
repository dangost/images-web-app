all:
	pyinstaller --onefile application/app.py

docker:
	docker build -t images .

clean:
	rm -r build;
	rm app.spec

