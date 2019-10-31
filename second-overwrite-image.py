#import libraries
import cv2

img = cv2.imread('/home/pi/Pictures/young.jpeg')

for y in range(0, img.shape[0]):
  for x in range(0, img.shape[1]):
    img[y, x] = (255, 0, 0)

cv2.imshow("New image: ", img)
cv2.imwrite('output-pictures/blue-image.jpeg', img)
