from PIL import Image
import numpy as np
from load_image import ft_load


def zoom_image(path):
    """Zoom then print and show the new image"""
    # Display original information of the image
    np_pixel = ft_load(path)
    print(np_pixel)

    # Turn it to grayscale and slice
    grayscale_image = Image.fromarray(np_pixel).convert('L')
    grayscale_array = np.array(grayscale_image)
    # Slice the middle of the image
    new_height = grayscale_array.shape[0] // 3
    new_width = grayscale_array.shape[1] // 3
    grayscale_sliced = grayscale_array[0 + new_height:new_height*2,
                                       0 + new_width:new_width*2]

    # It's necessary to get the new image here \
    # before reshaping the np.ndarray for display \
    # Image.fromarray() won't work properly after reshaping.
    sliced_image = Image.fromarray(grayscale_sliced)
    sliced_image.show()

    # Reshape the np.ndarray for display
    grayscale_sliced = grayscale_sliced[:, :, np.newaxis]
    print(f"New shape after slicing: {grayscale_sliced.shape}", end='')
    print(f" or ({grayscale_sliced.shape[0]}, {grayscale_sliced.shape[1]})")
    print(grayscale_sliced)


if __name__ == "__main__":
    try:
        zoom_image("../animal.jpeg")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
