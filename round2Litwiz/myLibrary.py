import cv2
from main import Input

h = int(input("height : "))
w = input("width : ")
s = int(input("size : "))

i = Input(h, w, s)

h = i.height(h)
w = i.width(w)
s = i.resize(s)

d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
w = d[w]

colour = (0,0,0)

def image_proj():

    path = r'D:\round2Litwiz\input_image.png'
    image = cv2.imread(path)
    image = cv2.resize(image, (s,s))


    height,width,c = image.shape
    
    grid_size = height/8
    

    center_cord = (int((grid_size*(w-1))+grid_size/2), int((grid_size*(8-h))+grid_size/2))
    
    redius = int(grid_size/2)
    if image[center_cord][1] == 255:
        colour = (0,0,0)
    else:
        colour = (255,255,255)
    #print(image[center_cord][1]==[0])

    image = cv2.circle(image, center_cord, redius, colour, -1)

    cv2.imshow('Image', image)

    cv2.waitKey(0)

image_proj()