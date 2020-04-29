#########################################################
#														#
# EXPERIMENTAL - Only use if you know what you're doing #
#														#
#########################################################

BASE := $(shell /bin/pwd)

HD_RELEASE := $$(sed -n -E "s/__version__ = '(.+)'/\1/p" pointbreak/__version__.py)

target:
	$(info ${HELP_MESSAGE})
	@exit 0

all: clean build

test:
	@poetry install
	@poetry run pytest

shell:
	@poetry install
	@poetry shell
	
build: clean _build_section_01 _build_section_02
	$(info [*] Build complete..)
	

clean:
	$(info [*] Removing build artifacts..)
	@rm -rf site build dist .egs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox .ipython
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +
	$(info [*] Removing compiled slide artifacts..)
	@rm -rf compiled_slides/html/*
	@rm -rf compiled_slides/pdf/*
	@rm -rf compiled_slides/pptx/*

docker:
	docker-compose -f local.yml build
	docker-compose -f local.yml up -d

############# 
#  Helpers  #
#############

_docker_clean:
	$(info [*] Stoping development stack..)
	@docker-compose -f local.yml down -v 2>/dev/null 
	$(info [*] Removing development stack..)
	@docker-compose -f local.yml rm 2>/dev/null

_build_section_01:
	@marp --pdf -I 01_python3_tooling_build_systems/slides/ -o compiled_slides/pdf/
	@marp --pptx --jpeg-quality 100 -I 01_python3_tooling_build_systems/slides/ -o compiled_slides/pptx/
	@marp --bespoke.progress --bespoke.osc -I 01_python3_tooling_build_systems/slides/ -o compiled_slides/html/

_build_section_02:
	@marp --pdf -I 02_python3_packaging_managment/slides/ -o compiled_slides/pdf/
	@marp --pptx --jpeg-quality 100 -I 02_python3_packaging_managment/slides/ -o compiled_slides/pptx/
	@marp --bespoke.progress --bespoke.osc -I 02_python3_packaging_managment/slides/ -o compiled_slides/html/
