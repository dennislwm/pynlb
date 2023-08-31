.PHONY: default pipenv_freeze pipenv_new pipenv_install pipenv_shell pipenv_venv test test_verbose

default: pipenv_shell

pipenv_freeze:
	pip3 install pipreqs
	pipreqs --ignore tests . --force
	echo "check-jsonschema==0.23.0" >> ./requirements.txt
	echo "pytest==7.1.3" >> ./requirements.txt
	echo "pyyaml==6.0.1" >> ./requirements.txt
	pip3 uninstall -y pipreqs

pipenv_new:
	pipenv --python 3.9

pipenv_install:
	pipenv install --dev check-jsonschema==0.23.0 pytest==7.1.3 pyyaml==6.0.1

pipenv_shell:
	pipenv shell

pipenv_venv:
	pipenv --venv

test:
	if [[ -z "$(NLB_API_TOKEN)" ]]; then exit 1; fi
	PYTHONPATH=./ pytest

test_verbose:
	if [[ -z "$(NLB_API_TOKEN)" ]]; then exit 1; fi
	PYTHONPATH=./ pytest -v -s --log-cli-level INFO --log-cli-format "[%(filename)s:%(lineno)s - def %(funcName)s()] %(levelname)s %(message)s"
