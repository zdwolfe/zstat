#!/usr/bin/env python3

# Get the Xth percentile from sorted_values
# Values must be sorted first
# Example:
# sorted_percentile(sorted([456, 366, 695, 773, 617, 826, 56, 78, 338, 326], 90) = 773
def sorted_percentile(sorted_values, x):
  d_index_of_percentile = (x / 100.0) * (len(sorted_values) - 1)
  index_of_percentile = round(d_index_of_percentile)
  return sorted_values[index_of_percentile]


# Get a list of percentile tuples
# Structure of each tuple: (percentile, value)
# Example: get_percentile([1], 100) = (100, 1)
# If the input is empty, returns None
def get_percentiles(inputs, percentiles):
  if (len(inputs) <= 0) : return None
  numerical_inputs = list(map(lambda x: int(x), inputs))
  sorted_inputs = sorted(numerical_inputs)

  outputs = []
  for percentile in percentiles:
    percentile_value = sorted_percentile(sorted_inputs, percentile)
    output = (percentile, percentile_value)
    outputs.append(output)

  return outputs

