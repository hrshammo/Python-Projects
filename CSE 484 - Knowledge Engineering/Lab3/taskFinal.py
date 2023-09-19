import cv2
import numpy as np

# Load an image
img = cv2.imread('a.webp', 1)

# Task 1: Remove Background
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
background = np.full_like(img, (255, 255, 255), dtype=np.uint8)
result_bg_removed = cv2.bitwise_and(img, img, mask=mask_inv) + cv2.bitwise_and(background, background, mask=mask)

# Task 2: Shifting
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
shifted_img = cv2.warpAffine(result_bg_removed, translation_matrix, (result_bg_removed.shape[1], result_bg_removed.shape[0]))

# Task 3: Rotation 90 Degrees Clockwise
rotated_img = cv2.rotate(shifted_img, cv2.ROTATE_90_CLOCKWISE)

# Display the final result
cv2.imshow("Final Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
