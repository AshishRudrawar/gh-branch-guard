install:
	python -m pip install --upgrade pip
	python -m pip install -e '.[test]'

test:
	pytest -q

clean:
	rm -rf build dist *.egg-info
