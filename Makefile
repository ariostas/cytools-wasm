SHELL := /bin/bash

.PHONY: all build clean serve

all: clean build
	@ echo "Done"

clean:
	rm -r .cache .jupyterlite dist pypi *.egg-info || echo "Some files were already deleted"

build:
	pip install -r requirements.txt
	python -m build
	mkdir -p pypi
	rm -r pypi/* || echo "Nothing to delete"
	cp dist/*.whl pypi
	rm -r dist
	cd pypi && jupyter piplite index
	jupyter lite build --contents content --output-dir dist

serve:
	cd dist && python -m http.server
