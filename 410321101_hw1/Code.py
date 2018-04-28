
# coding: utf-8

# In[32]:


import numpy as np
import cv2
img_k1 = cv2.imread('key1.png')
gray_k1 = cv2.cvtColor(img_k1, cv2.COLOR_BGR2GRAY)
gray_k1 = np.array(gray_k1)
img_k2 = cv2.imread('key2.png')
gray_k2 = cv2.cvtColor(img_k2, cv2.COLOR_BGR2GRAY)
gray_k2 = np.array(gray_k2)
img_E = cv2.imread('E.png')
gray_E = cv2.cvtColor(img_E, cv2.COLOR_BGR2GRAY)
gray_E = np.array(gray_E)
img_I = cv2.imread('I.png')
gray_I = cv2.cvtColor(img_I, cv2.COLOR_BGR2GRAY)
gray_I = np.array(gray_I)
img_Eprime = cv2.imread('Eprime.png')
gray_Eprime = cv2.cvtColor(img_Eprime, cv2.COLOR_BGR2GRAY)
gray_Eprime = np.array(gray_Eprime)

gray_I2= np.zeros(gray_Eprime.shape,np.uint8) 
w = [0,0,0]
w = np.array(w)
x = [0,0,0]
x = np.array(x)
e = [0,0,0]
e = np.array(e)
size = gray_k1.shape;
W = size[1]
H = size[0]

r = 0.00001 
epoch = 1 
while epoch < 2:
    

    for i in range(1,W):
            for j in range(1,H):
                k1 = gray_k1[j,i]
                k2 = gray_k2[j,i]
                I = gray_I[j,i]
                x[0] = k1
                x[1] = k2
                x[2] = I  #x[k1,k2,I]
                a = np.dot(w,x)
                e = gray_E[j,i] - a  
                w = w + r * e * x
 
    epoch = epoch + 1          

for i in range(1,W):
        for j in range(1,H):
            color = (gray_Eprime[j,i] - w[0]*gray_k1[j,i] - w[1]*gray_k2[j,i])/w[2] 
            if color > 255:
                color = 255
            if color < 0:
                color = 0
            gray_I2[j,i] = color 
    


cv2.imshow('My Image', gray_I2)
cv2.imwrite('Decryption.jpg', gray_I2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[29]:


print(w)

