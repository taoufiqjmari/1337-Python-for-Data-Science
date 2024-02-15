def ft_mean(args):
    """Calculate the mean"""
    mean = sum(args) / len(args)
    return mean


def ft_median(args):
    """Calculate the median"""
    sorted_data = sorted(args)
    data_length = len(sorted_data)
    median = None

    # If the length is odd, the median is the middle element.
    if data_length % 2 == 1:
        median = sorted_data[data_length // 2]
    # If the length is even, the median is the average of the two middle elements.
    else:
        median = (sorted_data[data_length // 2 - 1] + sorted_data[data_length // 2]) / 2

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

    # If the length is odd, the quartiles are the middle elements between their respective halves.
    if data_length % 2 == 1:
        q1 = sorted_data[q1_index]
        q3 = sorted_data[q3_index]
    # If the length is even, the quartiles are the averages of the two middle elements in their respective halves.
    else:
        q1 = (sorted_data[q1_index - 1] + sorted_data[q1_index]) / 2
        q3 = (sorted_data[q3_index - 1] + sorted_data[q3_index]) / 2

    return [float(q1), float(q3)]


def ft_std(args):
    """Calculate the Standard Deviation"""
    # Calculate the mean of the data.
    mean = ft_mean(args)

    # Calculate the squared deviations from the mean for each data point.
    squared_deviations = [(val - mean)**2 for val in args]

    # Calculate the variance (average squared deviation).
    variance = sum(squared_deviations) / len(args)

    # Calculate the standard deviation (square root of the variance).
    std = variance**0.5
    while abs(std**2 - variance) > 1e-6:
        std = (std + variance / std) / 2

    return std


def ft_var(args):
    """Calculate the Variance"""
    # Calculate the mean of the data.
    mean = ft_mean(args)

    # Calculate the squared deviations from the mean for each data point.
    squared_deviations = [(val - mean)**2 for val in args]

    # Calculate the variance (average squared deviation).
    var = sum(squared_deviations) / len(args)

    return var


def ft_statistics(*args: any, **kwargs: any) -> None:
    for value in kwargs.values():
        match value:
            case 'mean':
                if not args:
                    print("ERROR")
                else:
                    print(f"mean : {ft_mean(args)}")
            case 'median':
                if not args:
                        print("ERROR")
                else:
                    print(f"median : {ft_median(args)}")
            case 'quartile':
                if not args:
                        print("ERROR")
                else:
                    print(f"quartile : {ft_quartile(args)}")
            case 'std':
                if not args:
                        print("ERROR")
                else:
                    print(f"std : {ft_std(args)}")
            case 'var':
                if not args:
                        print("ERROR")
                else:
                    print(f"std : {ft_var(args)}")
            case _:
                pass
