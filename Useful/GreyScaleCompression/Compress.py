from PIL import Image
import numpy as np

img = Image.open("image.png")
arr = np.array(img)


print(arr)
