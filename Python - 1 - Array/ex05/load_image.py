from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        # Open the image file
        with Image.open(path) as img:
            #Show image
            # img.show()

            # Print image format
            print(f"The shape of image is: {np.array(img).shape}")

            # Convert image to RGB mode
            rgb_img = img.convert("RGB")

            # Get pixel data as a numpy array
            pixels = np.array(rgb_img)

            # Return pixel content in RGB format
            return pixels

    except Exception as e:
        # Handle errors with a clear error message
        print(f"Error loading image: {e}")
        return None
