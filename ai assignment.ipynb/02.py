import statistics
data=[ 15,21,29,21,15,24,32,21,15,30]
data_mean = statistics.mean(data)
data_median = statistics.median(data)
data_mode = statistics.mode(data)
data_variance = statistics.variance(data)
data_std_deviation = statistics.stdev(data)
print(f"mean: {data_mean}")
print(f"median: {data_median}")
print(f"mode: {data_mode}")
print(f"varaince: {data_variance:.2f}")
print(f"standard deviation:{data_std_deviation:.2f}")