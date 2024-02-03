from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load image and return it as Numpy array"""
    try:
        # Open the image file
        with Image.open(path) as img:
            # Show image
            # img.show()

            # Turn image to RGB then to a Numpy array
            img_np = np.array(img.convert('RGB'))

            # Print image format
            print(f"The shape of image is: {img_np.shape}")

            return img_np
    except Exception as e:
        raise Exception(e)
