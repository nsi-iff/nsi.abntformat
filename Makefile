all: test

test_deps: should-dsl ludibrio specloud

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install https://github.com/hugobr/should-dsl/tarball/master

ludibrio:
	@python -c 'import ludibrio' 2>/dev/null || pip install https://github.com/nsigustavo/ludibrio/tarball/master

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install specloud --no-deps -r https://github.com/hugobr/specloud/raw/master/requirements.txt

test: test_deps
	@echo ==============================================
	@echo ============ Running unit specs ==============
	@specloud
	@python -c "import doctest; doctest.testfile('README.rst')"

