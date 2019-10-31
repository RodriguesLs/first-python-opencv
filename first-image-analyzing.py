#import libraries
import cv2

#read image
image = cv2.imread('/home/pi/Pictures/young.jpeg')

print('Width in pixels: ', end='')
print(image.shape[1])
print('Height in pixels: ', end='')
print(image.shape[0])
print('Quantity channels: ', end='')
print(image.shape[2])

#Show image with a function imshow
cv2.imshow('Window name:', image)
cv2.waitKey(0)

#Save file with another name
cv2.imwrite('/output-pictures/output.jpg', image)
