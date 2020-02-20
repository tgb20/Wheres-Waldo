import cv2
from matplotlib import pyplot as plt

# Looking for this image
template = cv2.imread('female_waldo.jpg',0)

# in this image 
img_rgb = cv2.imread('waldo_town.jpg')

# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Compare the template to the image
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# Get the location where the template best matches the image
min_score, max_score, (min_x, min_y), (max_x, max_y) = cv2.minMaxLoc(res)

# Get the coordinates of the best match
width, height = template.shape[::-1]
corner_topL = (max_x, max_y)
corner_botR = (corner_topL[0]+width, corner_topL[1]+height)
print(corner_topL, corner_botR)

# Draw a box on the image 
cv2.rectangle(img_rgb, corner_topL, corner_botR, (0,255,0), 10)

# Make a new image with the box on it
cv2.imwrite('found_waldo.png',img_rgb) # Located Waldo
plt.imsave('map_waldo.png',res) # Map of where the template matcher found "Waldo"
