import cv2
x=input("enter the path of the image : ")
path=r""f"{x}"""
src=cv2.imread(path)
window_name='Image'
image=cv2.rotate(src,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)