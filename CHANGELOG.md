# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- See upcoming changes in [News directory](https://github.com/makukha/date62/tree/main/NEWS.d)

<!-- scriv-insert-here -->

<a id='changelog-0.2.0'></a>
## [0.2.0](https://github.com/makukha/date62/releases/tag/v0.2.0) — 2025-04-04

***Breaking 🔥***

- Redesigned API in the spirit of `base64`.
- Redesigned CLI to follow changes in API.

***Removed 💨***

- Eliminated optional dependency on `click` and `rich-click`, remove extra `[cli]`. Using `argparse` from now on.

***Added 🌿***

- Support for Python 2.7+

***Fixed***

- Mypy typing and Ruff errors and formatting.

***Misc***

- Applied [makukha/copython](https://github.com/makukha/copython) project template.
