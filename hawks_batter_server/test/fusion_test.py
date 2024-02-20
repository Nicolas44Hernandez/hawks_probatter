import cv2
import numpy as np

# Front Image
frontimage = '/home/nico/workspace/hawks_probatter/app_data/daemon/r_1b.png'  
# Back Image
backimage = '/home/nico/workspace/hawks_probatter/app_data/ball.png'

def resize_image(img):
    #Calculating the Pixel Size for Resizing
    new_width = int(img.shape[1]/2)
    new_height = int(img.shape[0]/2)

    img_double = cv2.resize(img, None, fx = 10, fy = 10)

    print('Image Width is',img_double.shape[1])
    print('Image Height is',img_double.shape[0])
    cv2.imwrite('new.png', img_double)

def read_transparent_png(filename):
    overlay_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    image_4channel = cv2.resize(overlay_image, (999, 998))
    alpha_channel = image_4channel[:,:,3]
    rgb_channels = image_4channel[:,:,:3]

    # White Background Image
    #white_background_image = np.ones_like(rgb_channels, dtype=np.uint8) * 255
    white_background_image = cv2.imread(backimage, cv2.IMREAD_UNCHANGED)

    # Alpha factor
    alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = white_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    return final_image.astype(np.uint8)

#img_front = cv2.imread(frontimage, cv2.IMREAD_UNCHANGED)

img_front = read_transparent_png(frontimage)
print(f"Original size: {img_front.shape}")
cv2.imshow('CENTERED',img_front)
cv2.waitKey(0)

# img_back = cv2.imread(backimage)
# print(f"Back image Original size: {img_front.shape}")
# cv2.imshow('CENTERED',img_back)
# cv2.waitKey(4000)
cv2.destroyAllWindows()



#resize_image(img_front)


# # load resized image as grayscale
# img = cv2.imread(frontimage, cv2.IMREAD_GRAYSCALE)
# h, w = img.shape
# print(h,w)

# # load background image as grayscale
# back = cv2.imread(backimage, cv2.IMREAD_GRAYSCALE)
# hh, ww = back.shape
# print(hh,ww)

# # compute xoff and yoff for placement of upper left corner of resized image   
# yoff = round((hh-h)/2)
# xoff = round((ww-w)/2)
# print(yoff,xoff)

# # use numpy indexing to place the resized image in the center of background image
# result = back.copy()
# result[yoff:yoff+h, xoff:xoff+w] = img

# # view result
# cv2.imshow('CENTERED', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # save resulting centered image
# cv2.imwrite('resized_centered.png', result)