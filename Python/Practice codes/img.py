import numpy as np
from skimage import data
import matplotlib.pyplot as plt

# Load an image
image = data.coffee()

# Mask pixels with values less than 87
mask = image > 87
image[mask] = 255

# Display the result
plt.imshow(image, cmap='gray')
plt.title("Image Masking")
plt.axis('off')
plt.show()



