# 5. Installation and Configuration
## 5.1. Create a virtual environment

This runbook should be performed by the Developer.

1. We will start by navigating to our `app` folder. This is the root folder of our virtual environment.

Then, we will install `pipenv` and create a Python 3 virtual environment for this project.

```sh
cd app
pip3 install --user pipenv
pipenv --python 3.9
```

2. Before we can run our app, we need to activate virtual environment and install any dependencies. Ensure that you are in the `app` folder.

```sh
pipenv shell
```

This command creates both the `Pipfile` and `Pipfile.lock` in your current folder. To add any dependencies under the `[packages]` section, type the following command:

```sh
pipenv install PACKAGE_NAME==PACKAGE_VERSION
```

To uninstall any dependency.

```sh
pipenv uninstall PACKAGE_NAME
```

To deactivate the virtual environment.

```sh
exit
```

## 5.2. Create a Makefile

This runbook should be performed by the Developer.

You can use `make` to automate different parts of developing a Python app, like running tests, cleaning builds, and installing dependencies. To use `make` in your project, you need to have a file named `Makefile` at the root of your project.

1. Create a file `Makefile` in the `app` folder. Add the following lines to the file:

```makefile
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
```

Each rule consists of 3 parts: a target, a list of pre-requisities, and a recipe. The follow this format:

```makefile
target: pre-req1 pre-req2 pre-req3
  recipes
```

The `target` represents a file that needs to be created in your build. The pre-requisites list tells `make` what dependencies are required, which can be a file or another target. Finally the recipes are a list of shell commands that will be executed.

The `.PHONY` line declares a target that does not exist. As Python is an interpreted language, there is no build file.
