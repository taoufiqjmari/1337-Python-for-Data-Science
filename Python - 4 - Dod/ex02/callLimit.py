def callLimit(limit: int):
    """
    A wrapper to take a parameter which is a limit
    of how many time can a function be called
    """
    count = 0
    def callLimiter(function):
        """
        A wrapper to make a function run {limit} times only
        """
        def limit_function(*args: any, **kwds: any):
            """
            The modif on the function
            """
            nonlocal count
            if count < limit:
                function()
            else:
                print(f'Error: {function} call too many times')
                return None
            count += 1
        return limit_function
    return callLimiter
