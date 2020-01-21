all: init test

init:
	pip3 install -r requirements.txt

checkpypi: clean
	python setup.py sdist && twine check dist/*

unittest:
	python3 -m unittest test.test_zstat

clean:
	rm -rf dist/ zstat_cli.egg-info/

test: unittest checkpypi

deploy: test
	twine upload dist/*

.PHONY: init test

