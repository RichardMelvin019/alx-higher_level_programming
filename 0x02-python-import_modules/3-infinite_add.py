#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the sum of the argv"""
    import sys

    argv = sys.argv[1:]
    result = 0

    for i, arguments in enumerate(argv, 1):
	    result += int(arguments)
    print("{}".format(result))
