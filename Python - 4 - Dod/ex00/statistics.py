def ft_mean(args):
    """Calculate the mean"""
    mean = sum(args) / len(args)
    return mean


def ft_median(args):
    """Calculate the median"""
    sorted_data = sorted(args)
    data_length = len(sorted_data)
    median = None

    # Odd length, median is the middle element.
    if data_length % 2 == 1:
        median = sorted_data[data_length // 2]
    # Even lenfth, median is average of two middle elements.
    else:
        median = (sorted_data[data_length // 2 - 1]
                  + sorted_data[data_length // 2]) / 2

    return median


def ft_quartile(args):
    """Calculate the quartile (25% and 75%)"""
    sorted_data = sorted(args)
    data_length = len(sorted_data)

    # Calculate the index for the 25% quartile.
    q1_index = int(0.25 * data_length)
    # Calculate the index for the 75% quartile.
    q3_index = int(0.75 * data_length)

    q1 = None
    q3 = None

    if data_length % 2 == 1:
        q1 = sorted_data[q1_index]
        q3 = sorted_data[q3_index]
    else:
        q1 = (sorted_data[q1_index - 1] + sorted_data[q1_index]) / 2
        q3 = (sorted_data[q3_index - 1] + sorted_data[q3_index]) / 2

    return [float(q1), float(q3)]


def ft_var(args):
    """Calculate the Variance"""
    mean = ft_mean(args)

    # Calculate the squared deviations from the mean for each data point.
    squared_deviations = [(val - mean)**2 for val in args]

    # Calculate the variance (average squared deviation).
    var = sum(squared_deviations) / len(args)

    return var


def ft_std(args):
    """Calculate the Standard Deviation"""
    # Calculate the variance (average squared deviation).
    variance = ft_var(args)
    return variance**0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Entry point to calculate staticstics values"""
    statistics = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var,
    }

    for statistic, function in statistics.items():
        if statistic not in kwargs.values():
            continue
        if not args:
            print("ERROR")
        else:
            result = function(args)
            print(f"{statistic} : {result}")
