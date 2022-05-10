all: app

app:
	pyinstaller --onefile application/app.py
	cp ./deployment/app/config.json ./dist/

docker:
	docker build -t dangost/images-api .

clean:
	rm -r build;
	rm *.spec
	rm -r dist


