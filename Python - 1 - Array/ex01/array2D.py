import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice array by start and end parameters"""
    try:
        family_np_array = np.array(family)
        assert isinstance(family, list)

        print(f'My shape is : {family_np_array.shape}')
        new_family = family_np_array[start:end]
        print(f'My new shape is : {new_family.shape}')
        return new_family
    except Exception:
        return 'AssertionError: the arguments are bad'
