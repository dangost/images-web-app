NAME := $(shell uname -s)

ifeq ($(NAME), Linux)
	BUILD := build_app
	CLEAN := clean_unix
else
	ifeq ($(NAME), Darwin)
		BUILD := build_app
		CLEAN := clean_unix
	else
		BUILD := build_app_win
		CLEAN := clean_win
	endif
endif

all: $(BUILD)
clean: $(CLEAN)

build_app: app copy_external_data
build_app_win: app copy_external_data_win

app:
	pyinstaller --onefile application/app.py

docker:
	docker build -t dangost/images-api .

copy_external_data:
	cp ./deployment/app/config.json ./dist/
	cp -r views ./dist

copy_external_data_win:
	Xcopy /E /I /Y .\views .\dist\views
	copy .\deployment\app\config.json .\dist

clean_win:
	del /s *.spec
	rmdir /q /s dist
	rmdir /q /s build

clean_unix:
	rm -r build;
	rm *.spec
	rm -r dist


