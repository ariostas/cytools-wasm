# CYTools WASM

This is an experimental fork of the [CYTools package](https://cy.tools/) that attempts to get it running on WebAssembly with as much functionality as possible. If you are looking for the standard CYTools package please visit the [website](https://cy.tools/) or the [original repository](https://github.com/LiamMcAllisterGroup/cytools).

[Click here to view the live deployment](https://ariostas.github.io/cytools-wasm/)

## Status

This package is still in very early stages, but it already offers a decent amount of functionality.

## Detailed status

Here is a more detailed status for the different dependencies.

- [x] `numpy`
Fully compiled to wasm by `pyodide`.
- [x] `scipy`
Fully compiled to wasm by `pyodide`.
- [x] `matplotlib`
Fully compiled to wasm by `pyodide`.
- [x] `python-flint`
This package was compiled to wasm in [this repository](https://github.com/ariostas/python-flint-wasm).
- [ ] `pplpy`
Requires the `PPL` library to be compiled to wasm. It's probably not too difficult, but it might not be worth it since `qhull` (included in `scipy`) is probably enough for the lite version.
- [ ] `PALP`, `CGAL`, and `TOPCOM`
These ones might need more significant work to package them into wasm because apart from having to compile them to wasm they need to be more properly wrapped for use with Python because the `subprocess` module is far from ideal to use in this scenario. However, I think that for the lite version it's probably fine to go without them if it requires too might work.
- [ ] `ortools`
This one might be doable to package into wasm, but it would definitely require significant work because it has many dependencies and it's probably difficult to get everything working together.
- [ ] `requests`
This module is unfortunately unavailable in `pyodide` and it's difficult to find an alternative. There are wrappers for JavaScript functions that perform the same functionality, but modern browsers have security features that prevent us from using them the way we would want to. This means that `fetch_polytopes` is currently broken.