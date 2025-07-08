
import argparse#parsing command line arguments
import numpy as np

def mean(n):
    return sum(n) / len(n)

def median(n):
    n = sorted(n)
    length = len(n)
    if length % 2 == 0:
        return (n[length // 2 - 1] + n[length // 2]) / 2
    else:
        return n[length // 2]

operations={
    "median":median,
    "mean":mean
}
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", help="Numbers you want to operate over.", nargs='+', type=float)
    parser.add_argument("operation", nargs='?', default="median", choices=["median", "mean"])
    args = parser.parse_args()
    print(
        operations[args.operation](args.numbers)
    )



if __name__ == "__main__":
    main()