import sys

sys.path.append('./build-scripts')

import build

def main():
    build.SETTINGS = build.load_settings()
    build.convert_tpys()


if __name__ == '__main__':
    main()
