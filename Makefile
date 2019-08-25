install:
	set -e; \
	. ./sh/environments.sh; \
	echo $(GPU_SINGLE_ALLOC_PERCENT)