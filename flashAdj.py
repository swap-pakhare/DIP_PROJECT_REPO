import cv2
import numpy as np

def flashAdj(amb_img, flash_img, alpha):
    amb_ycc = cv2.cvtColor(amb_img, cv2.COLOR_BGR2YCR_CB)
    flash_ycc = cv2.cvtColor(flash_img, cv2.COLOR_BGR2YCR_CB)
    out = ((1-alpha)*amb_ycc + alpha*flash_ycc).astype(np.uint8)
    out = cv2.cvtColor(out, cv2.COLOR_YCR_CB2RGB)
    
    return out