import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading in img
AtuImg = cv2.imread('C:\Lab8\ATU.jpg')

# Converting img to grayscale
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the image to grayscale
AtuGray = cv2.cvtColor(AtuImg, cv2.COLOR_BGR2GRAY)

# Plotting img for Part.6
# plt.imshow(AtuGray, cmap='gray')
# plt.title('Grayscale Image')   # Adding a Title
# plt.axis('off')  # Turning off axis numbers
# plt.show()  # Displaying 

# # Plotting the images
# plt.figure(figsize=(10, 20))  # Set the figure size as needed

# # Original Color Image
# plt.subplot(2, 1, 1)
# plt.imshow(cv2.cvtColor(AtuImg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
# plt.title('Original')
# plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis

# # Grayscale Image
# plt.subplot(2, 1, 2)
# plt.imshow(AtuGray, cmap='gray')
# plt.title('GrayScale')
# plt.xticks([]), plt.yticks([])


# # Apply Gaussian Blur with different kernel sizes
# kernel_sizes = [(3, 3), (5, 5), (9, 9), (13, 13)]
# blurred_images = [cv2.GaussianBlur(AtuImg, ksize, 0) for ksize in kernel_sizes]


# # Blurred images
# for i, AtuImg in enumerate(blurred_images, start=2):
#     plt.subplot(2, 3, i)
#     plt.imshow(cv2.cvtColor(AtuImg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
#     plt.title('Original')
        
#     plt.imshow(AtuGray, cmap='gray')
        
#     plt.imshow(cv2.cvtColor(AtuImg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
#     plt.title(f'Gaussian Blur {kernel_sizes[i-2]}')
#     plt.axis('off')

# plt.tight_layout()
# plt.show()

# # Additional subplots can be added for imgBlurred, imgSobel, imgCanny, etc.
# plt.show()

# Apply Gaussian Blur with two different kernel sizes
blurred_5x5 = cv2.GaussianBlur(AtuImg, (5, 5), 0)
blurred_9x9 = cv2.GaussianBlur(AtuImg, (9, 9), 0)

# Plotting the original, grayscale, and blurred images
plt.figure(figsize=(10, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(AtuImg, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.title('Original')
plt.axis('off')

# Grayscale image
plt.subplot(2, 2, 2)
plt.imshow(AtuGray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

# Blurred image with 5x5 kernel
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(blurred_5x5, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title('Blurred 5x5')
plt.axis('off')

# Blurred image with 9x9 kernel
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(blurred_9x9, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title('Blurred 9x9')
plt.axis('off')

plt.tight_layout()
plt.show()