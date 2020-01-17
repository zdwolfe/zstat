init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest test.test_zstat

.PHONY: init test

