import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Returns a list of BMI values from two lists
    """
    try:
        height_np_array = np.array(height)
        weight_np_array = np.array(weight)

        assert np.issubdtype(height_np_array.dtype, np.number)
        assert np.issubdtype(weight_np_array.dtype, np.number)
        assert np.all(height_np_array > 0)
        assert np.all(weight_np_array > 0)
        assert height_np_array.shape == weight_np_array.shape

        return list(weight_np_array / height_np_array**2)
    except AssertionError:
        print('AssertionError: the arguments are bad')


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check whether BMI values are above or below a limit
    """
    try:
        bmi_np_array = np.array(bmi)
        assert np.issubdtype(bmi_np_array.dtype, np.number)

        return bmi_np_array > limit
    except AssertionError:
        print('AssertionError: the arguments are bad')
