import pysam
import numpy as np
import argparse
import sys


def main():
    parser = argparse.ArgumentParser("pack", description=f"Example package, using pysam {pysam.__version__}")
    parser.add_argument("-n", "--number", type=int, help="lucky number [6]", default=6)
    args = parser.parse_args(None if sys.argv[1:] else ['-h'])

    print(f"lucky number: {args.number}")
    print(f"pi = {np.pi}")


if __name__ == "__main__":
    main()
