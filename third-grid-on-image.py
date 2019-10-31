#Import libraries session
import cv2

#Variables
path = '/home/pi/Pictures/peoples.jpeg' #set your image path here
output = 'output-pictures/grid-modify.jpg' #set your output here

#Code content
image = cv2.imread(path)

for y in range(0, image.shape[0], 10):
  for x in range(0, image.shape[1], 10):
    image[y:y+5, x:x+5] = (0, 255, 255)
cv2.imshow('Modified image: ', image)
cv2.imwrite(output, image)
cv2.waitKey(0)
