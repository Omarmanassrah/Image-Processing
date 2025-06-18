import cv2
import numpy as np

image = cv2.imread(r"C:\Users\omar.DESKTOP-4KRKGQT\Downloads\c1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value = 240
thresh = np.zeros_like(gray_image)
for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        if gray_image[i, j] > threshold_value:
            thresh[i, j] = 0
        else:
            thresh[i, j] = 255

kernel_open = np.ones((5,5), dtype=np.uint8)     
kernel_close = np.ones((11,11), dtype=np.uint8)  

#add padding function to handle borders 
def pad_image(img, pad_h, pad_w):
    return np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

def erosion(img, kernel):
    k_h, k_w = kernel.shape
    #how much to pad the image
    pad_h, pad_w = k_h // 2, k_w // 2
    img_padded = pad_image(img, pad_h, pad_w)
    eroded = np.zeros_like(img)
    for i in range(eroded.shape[0]):
        for j in range(eroded.shape[1]):
            region = img_padded[i:i+k_h, j:j+k_w]
            if np.all(region[kernel == 1] == 255):
                eroded[i, j] = 255
            else:
                eroded[i, j] = 0
    return eroded

def dilation(img, kernel):
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2
    img_padded = pad_image(img, pad_h, pad_w)
    dilated = np.zeros_like(img)
    for i in range(dilated.shape[0]):
        for j in range(dilated.shape[1]):
            region = img_padded[i:i+k_h, j:j+k_w]
            if np.any(region[kernel == 1] == 255):
                dilated[i, j] = 255
            else:
                dilated[i, j] = 0
    return dilated

def opening(img, kernel):
    return dilation(erosion(img, kernel), kernel)

def closing(img, kernel):
    return erosion(dilation(img, kernel), kernel)

def opening_multiple(img, kernel, iterations):
    result = img.copy()
    for _ in range(iterations):
        result = opening(result, kernel)
    return result

def closing_multiple(img, kernel, iterations):
    result = img.copy()
    for _ in range(iterations):
        result = closing(result, kernel)
    return result

opened = opening_multiple(thresh, kernel_open, iterations=2)

closed = closing_multiple(opened, kernel_close, iterations=5)
#important parts objects white color 
mask = closed == 255
#all white
restored = np.ones_like(image) * 255
restored[mask] = image[mask]

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Threshold Image", thresh)
cv2.imshow("After Opening (Noise Removed)", opened)
cv2.imshow("After Closing (Holes Filled)", closed)
cv2.imshow("Restored Image with White Background", restored)

cv2.waitKey(0)
cv2.destroyAllWindows()
