<!--
<p align="center">
  <img src="https://github.com/biopragmatics/debio/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  DeBiO
</h1>

<p align="center">
    <a href="https://github.com/biopragmatics/debio/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/biopragmatics/debio/workflows/Tests/badge.svg" />
    </a>
    <a href="https://pypi.org/project/debio">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/debio" />
    </a>
    <a href="https://pypi.org/project/debio">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/debio" />
    </a>
    <a href="https://github.com/biopragmatics/debio/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/debio" />
    </a>
    <a href='https://debio.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/debio/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://codecov.io/gh/biopragmatics/debio/branch/main">
        <img src="https://codecov.io/gh/biopragmatics/debio/branch/main/graph/badge.svg" alt="Codecov status" />
    </a>  
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-snekpack-blue" /> 
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
    <a href="https://github.com/biopragmatics/debio/blob/main/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant"/>
    </a>
    <a href="https://zenodo.org/badge/latestdoi/505828431">
        <img src="https://zenodo.org/badge/505828431.svg" alt="DOI">
    </a>
</p>

A community-curated, decentralized biomedical ontology.

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.md](https://github.com/biopragmatics/debio/blob/master/.github/CONTRIBUTING.md) for more information on
getting involved. This document also includes:

1. Curation guidelines for new object properties
2. Instructions for rebuilding the ontology
3. Instructions for releasing the ontology to PyPI

## 🚀 Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/debio/) with:

```bash
$ pip install debio
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/biopragmatics/debio.git
```

## 👋 Attribution

### ⚖️ License

The code in this package is licensed under the MIT License.

<!--
### 📖 Citation

Citation goes here!
-->

<!--
### 🎁 Support

This project has been supported by the following organizations (in alphabetical order):

- [Harvard Program in Therapeutic Science - Laboratory of Systems Pharmacology](https://hits.harvard.edu/the-program/laboratory-of-systems-pharmacology/)

-->

<!--
### 💰 Funding

This project has been supported by the following grants:

| Funding Body                                             | Program                                                                                                                       | Grant           |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------|
| DARPA                                                    | [Automating Scientific Knowledge Extraction (ASKE)](https://www.darpa.mil/program/automating-scientific-knowledge-extraction) | HR00111990009   |
-->

### 🍪 Cookiecutter

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) template.

## 🛠️ For Developers

<details>
  <summary>See developer instructions</summary>


The final section of the README is for if you want to get involved by making a code contribution.

### Development Installation

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/biopragmatics/debio.git
$ cd debio
$ pip install -e .
```

### 🥼 Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in
a [GitHub Action](https://github.com/biopragmatics/debio/actions?query=workflow%3ATests).

### 📖 Building the Documentation

The documentation can be built locally using the following:

```shell
$ git clone git+https://github.com/biopragmatics/debio.git
$ cd debio
$ tox -e docs
$ open docs/build/html/index.html
``` 

The documentation automatically installs the package as well as the `docs`
extra specified in the [`setup.cfg`](setup.cfg). `sphinx` plugins
like `texext` can be added there. Additionally, they need to be added to the
`extensions` list in [`docs/source/conf.py`](docs/source/conf.py).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses [Bump2Version](https://github.com/c4urself/bump2version) to switch the version number in the `setup.cfg`,
   `src/debio/version.py`, and [`docs/source/conf.py`](docs/source/conf.py) to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel using [`build`](https://github.com/pypa/build)
3. Uploads to PyPI using [`twine`](https://github.com/pypa/twine). Be sure to have a `.pypirc` file configured to avoid
   the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.

</details>
