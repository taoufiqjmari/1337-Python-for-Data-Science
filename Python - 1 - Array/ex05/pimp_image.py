import numpy as np


RED = 0
GREEN = 1
BLUE = 2


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
    red_channel[:, :, [GREEN, BLUE]] = 0
    return red_channel


def ft_green(array):
    """
    Extracts the green channel of the image.
    """
    green_channel = array.copy()
    green_channel[:, :, [RED, BLUE]] = 0
    return green_channel


def ft_blue(array):
    """
    Extracts the blue channel of the image.
    """
    blue_channel = array.copy()
    blue_channel[:, :, [RED, GREEN]] = 0
    return blue_channel


def ft_grey(array):
    """
    Converts the image to grayscale.
    """
    # Use the formula: grayscale = 0.299 * R + 0.587 * G + 0.114 * B
    grey_image = np.dot(array[..., :3], [0.299, 0.587, 0.114])
    # Create a 3-channel grayscale image
    grey_array = np.stack([grey_image] * 3, axis=2)
    return grey_array.astype(np.uint8)
