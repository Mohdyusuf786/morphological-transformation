import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('village.png',0)
# lets define mask and kernal
_,mask=cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV) #change the threshold value to get perfect result
kernal=np.ones((3,3),np.uint8)
#next is dilation
dilation=cv2.dilate(mask,kernal,iterations=2)
#next we have erosion
erosion=cv2.erode(mask,kernal,iterations=1)
#lets try opening and closing method
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
#their is one more method gradient
grade=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
titles=['image','mask','dilation','erosion','opening','closing','grade']
images=[img,mask,dilation,erosion,opening,closing,grade]
for i in range(7):
     plt.subplot(3,4,i+1),plt.imshow(images[i],'gray')
     plt.title(titles[i])
     plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

   
