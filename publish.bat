echo Deactivating...
deactivate
rmdir /s /q .venv

echo Clear cache...
rmdir /s /q dist
rmdir /s /q a3rt_talkpy.egg-info

echo Create virtual environment...
python -m venv .venv
.venv\Scripts\activate

echo Install dependencies...
pip install -r requirements-dev.txt

echo Build and publish...
python setup.py sdist
python setup.py bdist_wheel
twine upload --repository pypi dist/*

echo Deactivating...
deactivate
rmdir /s /q .venv

echo Clear cache...
rmdir /s /q dist
rmdir /s /q a3rt_talkpy.egg-info
