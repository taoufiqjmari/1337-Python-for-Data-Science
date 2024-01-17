def is_list_of_numbers(input_list):
    """
    Check if a list is made up of only integers or floats.

    :param input_list: Input list to check
    :return: True if the list contains only integers or floats, False otherwise
    """
    for element in input_list:
        if not isinstance(element, (int, float)):
            return False
    return True


def calculate_bmi(height_m, weight_kg):
    """
    Calculate BMI (Body Mass Index).

    :param weight_kg: Weight in kilograms
    :param height_m: Height in meters
    :return: BMI value
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    bmi = weight_kg / (height_m ** 2)
    return bmi


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    result = []

    try:
        assert len(height) == len(weight)
        assert is_list_of_numbers(height)
        assert is_list_of_numbers(weight)

        for i in range(len(height)):
            result.append(calculate_bmi(height[i], weight[i]))
        return result
    except AssertionError:
        print('AssertionError: the arguments are bad')


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    result = []

    try:
        assert is_list_of_numbers(bmi)

        for el in bmi:
            result.append(el > limit)
        return result
    except AssertionError:
        print('AssertionError: the arguments are bad')
