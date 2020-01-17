import cv2
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread('waldo_war.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('waldo.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
min_score, max_score, (min_x, min_y), (max_x, max_y) = cv2.minMaxLoc(res)
corner_topL = (max_x, max_y)
corner_botR = (corner_topL[0]+template.shape[1], corner_topL[1]+template.shape[0])
print (corner_topL, corner_botR)
cv2.rectangle(img_rgb, corner_topL, corner_botR, (0,255,0), 10)
cv2.imwrite('found_waldo.png',img_rgb) # Located Waldo
plt.imsave('map_waldo.png',res) # Map of where the template matcher found "Waldo"ß