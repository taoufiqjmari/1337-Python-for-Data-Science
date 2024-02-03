def ft_invert(array):
    """
    Inverts the colors of the image.
    """
    return 255 - array


def ft_red(array):
    """
    Extracts the red channel of the image.
    """
    red_channel = array.copy()
    red_channel[:, :, [1, 2]] = 0
    return red_channel


def ft_green(array):
    """
    Extracts the green channel of the image.
    """
    green_channel = array.copy()
    green_channel[:, :, [0, 2]] = 0
    return green_channel


def ft_blue(array):
    """
    Extracts the blue channel of the image.
    """
    blue_channel = array.copy()
    blue_channel[:, :, [0, 1]] = 0
    return blue_channel


def ft_grey(array):
    """
    Converts the image to grayscale using the NTSC formula.
    """
    grayscale_image = 0.299 * array[:, :, 0] + 0.587 * array[:, :, 1] + 0.114 * array[:, :, 2]
    return grayscale_image
