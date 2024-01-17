def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, retur"""
    filtered = [el for el in iterable if function(el)]
    return filtered
