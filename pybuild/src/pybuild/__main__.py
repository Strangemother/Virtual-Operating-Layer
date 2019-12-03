import sys
from pybuild import build


def main():
    build.main(*sys.argv[1:])


if __name__ == '__main__':
    main()
