# python-unittests
Supersimple examples how to write unit tests in Python

# How to run the tests
If you didn't do yet, install pipenv - virtual environment manager recommended by Python Packaging Authority
```bash
pip3 install --user pipenv
```
Install pytest into your virtual environment and add it to development packages. If you don't have virtual
environment for this folder, it will create one.
```bash
pipenv install -d pytest
```
Activate the environment in you aren't in it yet.
```bash
pipenv shell
```
Finally, run the tests
```bash
pytest
```
