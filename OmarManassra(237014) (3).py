import cv2
import numpy as np

image = cv2.imread(r"C:\Users\omar.DESKTOP-4KRKGQT\Downloads\RoboCup11.jfif")
image_Field = cv2.imread(r"C:\Users\omar.DESKTOP-4KRKGQT\Downloads\RoboCup112233.jfif")

original = image.copy()
original_Field = image_Field.copy()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

lower_h, upper_h = 235, 245
lower_s, upper_s = 40, 255
# boolean mask for green color
h_thresh = (h >= lower_h) & (h <= upper_h)
s_thresh = (s >= lower_s) & (s <= upper_s)
green_mask = h_thresh & s_thresh
green_mask = green_mask.astype(np.uint8) * 255
height, width = green_mask.shape
for x in range(height):
    for y in range(width):
        if green_mask[x, y] == 255:
            image[x, y] = [0, 0, 255]


lower_hue = 0.03
upper_hue = 0.12
lower_saturation = 0.85
upper_saturation = 1.0

h_normalized = h / 180.0
s_normalized = s / 255.0
#boolean masks for value  
hue_condition = np.zeros_like(h_normalized, dtype=bool)
height, width = h.shape
for x in range(height):
    for y in range(width):
        if lower_hue <= h_normalized[x, y] <= upper_hue:
            hue_condition[x, y] = True

saturation_condition = np.zeros_like(s_normalized, dtype=bool)
for y in range(height):
    for x in range(width):
        if lower_saturation <= s_normalized[y, x] <= upper_saturation:
            saturation_condition[y, x] = True

orange_pixels = np.zeros_like(hue_condition, dtype=bool)
for y in range(height):
    for x in range(width):
        if hue_condition[y, x] and saturation_condition[y, x]:
            orange_pixels[y, x] = True

ball_mask = orange_pixels.astype(np.uint8) * 255

image[orange_pixels] = [0, 160, 255]

ball_alone = np.zeros_like(original)
for x in range(height):
    for y in range(width):
        if ball_mask[x, y] == 255:
            ball_alone[x, y] = original[x, y]

hsv_field = cv2.cvtColor(image_Field, cv2.COLOR_BGR2HSV)
h_field, s_field, _ = cv2.split(hsv_field)

green_mask_field = ((h_field >= lower_h) & (h_field <= upper_h)) & ((s_field >= lower_s) & (s_field <= upper_s))
green_mask_field = green_mask_field.astype(np.uint8) * 255

height, width = green_mask_field.shape
for x in range(height):
    for y in range(width):
        if green_mask_field[x, y] == 255:
            image_Field[x, y] = [0, 0, 255]

cv2.imshow("Original Image", original)
cv2.imshow("Ball Alone", ball_alone)
cv2.imshow("Field + Ball Detection", image)
cv2.imshow("Field Only Detection without ball", image_Field)

cv2.waitKey(0)
cv2.destroyAllWindows()
