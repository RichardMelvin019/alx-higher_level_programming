#!/usr/bin/python3
if __name__ == "__main__":
	"""Prints the argv"""
	import sys

	argc = len(sys.argv) - 1
	argv = sys.argv[1:]

	if argc == 1:
		print("{:d} argument:".format(argc))
	elif argc > 1:
		print("{:d} arguments:".format(argc))
	else:
		print("{:d} arguments.".format(argc))
	for i, arguments in enumerate(argv, 1):
		print("{:d}: {:s}".format(i, arguments))
