def are_lists_of_same_size(list_of_lists):
    # Check if the list is empty
    if not list_of_lists:
        return True

    # Get the size of the first list
    size = len(list_of_lists[0])

    # Iterate through the remaining lists and compare sizes
    for lst in list_of_lists[1:]:
        if len(lst) != size:
            return False

    return True


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list)
        assert are_lists_of_same_size(family)

        print(f'My shape is : ({len(family)}, {len(family[0])})')
        new_family = family[start:end]
        print(f'My new shape is : ({len(new_family)}, {len(new_family[0])})')
        return new_family
    except AssertionError:
        return 'AssertionError: the arguments are bad'
