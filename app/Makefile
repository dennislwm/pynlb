.PHONY: default pipenv_freeze pipenv_new pipenv_shell

default: pipenv_shell

pipenv_freeze:
	pip3 install pipreqs
	pipreqs --ignore tests . --force
	echo "pytest==6.2.4" >> ./requirements.txt
	pip3 uninstall -y pipreqs

pipenv_new:
	pipenv --python 3.9
	pipenv install --dev pytest==6.2.4

pipenv_shell:
	pipenv shell
