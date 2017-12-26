clean:
	pip uninstall exp-kit
	rm -rf *.egg-info
	rm -rf build dist

local-install:
	pip install -e .

build:
	python setup.py sdist bdist_wheel

test-publish:
	twine upload -r test dist/exp*

test-install:
	pip install --index-url https://test.pypi.org/simple/ exp-kit

publish:
	echo
