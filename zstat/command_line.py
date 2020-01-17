import sys
from zstat import get_percentiles

def main():
  inputs = sys.stdin.read().splitlines()
  # @TODO get this from a CLI argument
  percentiles = [0, 50, 90, 95, 99, 99.9, 100]
  outputs = get_percentiles(inputs, percentiles)
  for output in outputs:
    percentile = output[0]
    percentile_value = output[1]
    print("p" + str(percentile) + "\t=\t" + str(percentile_value))


if __name__ == "__main__":
  main()

