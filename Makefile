SHELL := /bin/bash

.PHONY: all build clean serve

all: clean build
	@ echo "Done"

clean:
	rm -r .cache .jupyterlite* dist pypi *.egg-info || echo "Some files were already deleted"

build:
	pip install -r requirements.txt
	python -m build
	mkdir -p pypi
	rm -r pypi/* || echo "Nothing to delete"
	cp dist/*.whl pypi
	cd pypi && wget https://github.com/ariostas/python-flint-wasm/releases/download/v0.1.0/python_flint_wasm-0.5.0-cp311-cp311-emscripten_3_1_45_wasm32.whl
	rm -r dist
	cd pypi && jupyter piplite index
	jupyter lite build --contents content --output-dir dist

serve:
	cd dist && python -m http.server
