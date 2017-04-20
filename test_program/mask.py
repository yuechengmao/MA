import numpy as np
import cv2


fgbg = cv2.BackgroundSubtractorMOG()

for i in range(1,460):
    image = cv2.imread('./data/motion1/imgs3/cam3_' + str(i) + '.jpg',-1)
    fgmask = fgbg.apply(image,learningRate=0.03)
    new_im = np.multiply(image,fgmask)

    cv2.imshow('frame',new_im)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
