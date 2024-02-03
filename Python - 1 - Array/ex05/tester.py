from PIL import Image
from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey


array = ft_load("../landscape.jpg")
print(array)
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
Image.fromarray(ft_invert(array)).show()
Image.fromarray(ft_red(array)).show()
Image.fromarray(ft_green(array)).show()
Image.fromarray(ft_blue(array)).show()
Image.fromarray(ft_grey(array)).show()

print(ft_invert.__doc__)
