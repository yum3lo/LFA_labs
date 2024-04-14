from sys import *
from interpreter import *

if __name__ == "__main__":
    argv.append("test.txt")
    print(parse(argv[1]))