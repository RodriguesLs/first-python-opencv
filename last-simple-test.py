import cv2

origin = '/home/pi/Pictures/young.jpeg'
output = 'output-pictures/rect-random.jpeg'

img = cv2.imread(origin)

#Create a blue rectangle on all width image
img[30:50, :] = (255, 0, 0)

#Create a red square
img[100:150, 50:100] = (0, 0, 255)

#Create a yellow square on all height image
img[:, 200:220] = (0, 255, 255)

#Create a green rectagle from line 150 to 300 and from column 250 to 350
img[150:300, 250:350] = (0, 255, 0)

#Create a cian (equals previous)
img[300:400, 50:150] = (255, 255, 0)

#(...)

cv2.imshow('Modify image >>', img)
cv2.imwrite(output, img)
cv2.waitKey(0)
