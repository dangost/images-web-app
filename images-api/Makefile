all: app docker

app:
	pyinstaller --onefile application/app.py
	cp .env ./dist/

docker:
	docker build -t dangost/images-api .

clean:
	rm -r build;
	rm *.spec
	rm -r dist


