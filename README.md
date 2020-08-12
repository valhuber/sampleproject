# Packaging Test
Explore how to contend PyPi & exports.

This is a very minor adaption of the [PyPa Sample Project](https://github.com/pypa/sampleproject):
* PyPa name changed in setup
* addition of src/sample/run.py
* and ability to call it in setup (search for valhuber)

The failure to run ```sample-run``` is posted to [StackOverflow](https://stackoverflow.com/questions/63363476/pypi-installed-app-fails-with-modulenotfound).

## Install (VSCode)
Source Control view, clone: https://github.com/valhuber/sampleproject.git.
```
cd sampleproject
virtualenv venv
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

## Run Locally

VSCode: F5 for `run.py`. Should print:
```
add_one(2) = 3
```
Or, from command console:
```
cd sampleproject
python src/sample/run.py
```

Suggestion: standard sampleproject might not want to use ```sample``` to run, since that's a pre-defined utility on the mac.  Mac users need to run something like 
```
/Users/val/python/vscode/sampleproject/venv/bin/sample
```

## Deploy to Pypi
Using [this reference](https://packaging.python.org/tutorials/packaging-projects/)...

Acquire the setup software (initial, 1-time setup):
```
cd sampleproject
deactivate
python setup.py install
python3 -m pip install --user --upgrade twine
python3 -m pip install --user --upgrade setuptools wheel
```

Creating the `dist`, **first time**
Get a [Saved API Key](https://test.pypi.org/manage/account/#api-tokens)

```
python3 setup.py sdist bdist_wheel  # verify this produces the dist folder
python3 -m twine upload --repository testpypi dist/*  # upload to test Pypi
```
User is `__token__`, pwd is **Saved API Key** (from above).

This should upload to the [Pypi site](https://test.pypi.org/project/sampleproject-valhuber/)

To **re-upload:**
1. Delete the `dist` folder (and `build`, and `.egg`)
2. Alter the version number in `__init__`
```
python3 setup.py sdist bdist_wheel
python3 -m twine upload  --skip-existing --repository testpypi dist/*
```

To install (beware - may require 15 mins until new version is active.

```
# windows: .\venv\Scripts\activate
source venv/bin/activate
pip uninstall sampleproject-valhuber
pip install -i https://test.pypi.org/simple/ sampleproject-valhuber
sample-run
```

Currently failing:

```
((venv) val@valMbp sampleproject % sample-run
Traceback (most recent call last):
  File "/Users/val/python/vscode/sampleproject/venv/bin/sample-run", line 5, in <module>
    from sample.run import main
  File "/Users/val/python/vscode/sampleproject/venv/lib/python3.8/site-packages/sample/run.py", line 1, in <module>
    import simple
ModuleNotFoundError: No module named 'simple'
(venv) val@valMbp sampleproject % 
```
