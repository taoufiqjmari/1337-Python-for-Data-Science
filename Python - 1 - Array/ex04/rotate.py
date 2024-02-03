from PIL import Image
import numpy as np
from load_image import ft_load


# Transpose:
# 1 2 3      1 4 7
# 4 5 6  ->  2 5 8
# 7 8 9      3 6 9
def ft_transpose(arr):
    """Transpose a numpy array"""
    # Create empty array with swapped dimensions
    transposed_arr = np.empty((arr.shape[1], arr.shape[0]))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            transposed_arr[j, i] = arr[i, j]  # Copy elements swapping indices
    return transposed_arr


def zoom_image(path):
    """Zoom then print and show the new image"""
    np_pixel = ft_load(path)

    # Turn it to grayscale and slice
    grayscale_image = Image.fromarray(np_pixel).convert('L')
    grayscale_array = np.array(grayscale_image)

    # Slice the middle of the image
    new_height = grayscale_array.shape[0] // 3
    new_width = grayscale_array.shape[1] // 3
    grayscale_sliced = grayscale_array[0 + new_height:new_height*2,
                                       0 + new_width:new_width*2]

    # Reshape the np.ndarray for display
    new_shape = grayscale_sliced[:, :, np.newaxis]
    print(f"New shape after slicing: {new_shape.shape}", end='')
    print(f" or ({new_shape.shape[0]}, {new_shape.shape[1]})")
    print(new_shape)

    return grayscale_sliced


def transpose_image(np_image):
    """Transpose an image, print it's new information and show it"""
    transposed = ft_transpose(np_image)

    transposed_image = Image.fromarray(transposed)
    transposed_image.show()

    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)


if __name__ == "__main__":
    try:
        image_sliced = zoom_image("../animal.jpeg")
        transpose_image(image_sliced)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
