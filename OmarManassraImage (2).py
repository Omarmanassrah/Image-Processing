import cv2 as cv

img = cv.imread(r"C:\Users\omar.DESKTOP-4KRKGQT\Downloads\as.JPG", cv.IMREAD_GRAYSCALE )

size = img.shape
out_img = img.copy()


Threshold = input("Enter the First  threshold'1' value (0-255): ")
Threshold = int(Threshold)
Threshold2 = input("Enter the Second threshold'2' value (0-255): ")
Threshold2 = int(Threshold2)

if Threshold > Threshold2:
    Threshold, Threshold2 = Threshold2, Threshold
    
for i in range(size[0]):
    for j in range(size[1]):
        if img[i, j] < Threshold or img[i, j] > Threshold2:
            out_img[i, j] = 0

            
cv.imshow('out image', out_img)
cv.waitKey(0)

