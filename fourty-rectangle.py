import cv2

origin = '/home/pi/Pictures/young.jpeg' #set image path
output = 'output-pictures/rectangle.jpeg'

image = cv2.imread(origin)

image[20:60, :] = (255, 0, 0)

cv2.imshow('Need a text: ', image)
cv2.imwrite(output, image)
cv2.waitKey(0)
