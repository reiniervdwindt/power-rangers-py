PYTHON=@`which python`
COVERAGE=@`which coverage`

test:
	$(COVERAGE) run --source=power_rangers setup.py test
	$(COVERAGE) report