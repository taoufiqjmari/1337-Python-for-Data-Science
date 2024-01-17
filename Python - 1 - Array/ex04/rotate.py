from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def rotate_image(image, angle):
    return [list(reversed(t)) for t in zip(image)]



def display_image_info(image_path):
    try:
        pixel_array = ft_load(image_path)

        grayscale_image = Image.fromarray(pixel_array).convert('L')
        grayscale_array = np.array(grayscale_image)
        grayscale_array = grayscale_array[:, :, np.newaxis]

        sliced_image = grayscale_array[100:500, 450:850]
        print(f"New shape after slicing: {sliced_image.shape} or ({sliced_image.shape[0]}, {sliced_image.shape[1]})")
        print(sliced_image)

        rotated_image = rotate_image(sliced_image, 90)

        plt.imshow(rotated_image, cmap='grey')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    display_image_info("../animal.jpeg")
