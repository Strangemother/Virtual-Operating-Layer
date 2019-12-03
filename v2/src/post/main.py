import sys

from sequence import kernel_proc


def main(host_driver_name, *argv):
    kernel_proc.post()

if __name__ == '__main__':
    main(sys.argv)
