import math
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as img
from skimage.transform import resize
from scipy import ndimage
from skimage.util import crop
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from PIL import Image


# Note: While entering the path of the image, enter without the qoutation marks
# I have used matplotlib and PIL to show and read images 
# Run the code from interactive window, if needed



img_name = str(input(r"Enter the image path to perform the following actions on (without the qoutation marks): "))
img  = img.imread(img_name)
img1 = 'image1.png'
img2 = 'image2.png'


height, width, depth = img.shape


def rotate_at_angle(img, direction, angle):

   angle_rad = angle * np.pi / 180.0
   max_len = int(math.sqrt(height*height + width*width))
   rotated_image = np.zeros((max_len, max_len, depth))

   rotated_height, rotated_width, _ = rotated_image.shape
   mid_row = int( (rotated_height+1)/2 )
   mid_col = int( (rotated_width+1)/2 )

   for r in range(rotated_height):
        for c in range(rotated_width):
            #  apply rotation matrix, the other way
            y = (r-mid_col)*math.cos(angle_rad) + (c-mid_row)*math.sin(angle_rad)           #Affine transformation to rotate images
            x = -(r-mid_col)*math.sin(angle_rad) + (c-mid_row)*math.cos(angle_rad)

            #  add offset
            y += mid_col
            x += mid_row

            #  get nearest index
            x = round(x)
            y = round(y)


            if (x >= 0 and y >= 0 and x < width and y < height):
                rotated_image[r][c][:] = img[y][x][:]

   output_image = Image.fromarray(rotated_image.astype("uint8"))
   output_image.show()


def combo(image1, image2, orientation):

    images = [Image.open(x) for x in ['image1.png', 'image2.png']]                      #open the two images
    small_Shape = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]            #find smaller image and resize the others

    if(orientation == 'vertical' or orientation == 'Vertical'):

        verticalStackImage = np.vstack( (np.asarray( i.resize(small_Shape) ) for i in images ) )
        verticalStackImage = Image.fromarray( verticalStackImage)
        verticalStackImage.show()

    else:
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        horizontal = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            horizontal.paste(im, (x_offset,0))
            x_offset += im.size[0]
        horizontal.show()


def resize1(x_scale, y_scale):

    resize_image = resize(img, (height * y_scale, width * x_scale), anti_aliasing = 'True')
    plt.imshow(resize_image, interpolation='nearest')



def rgb2grayimg(img):

    R = (0.2989 * img[:,:,0])
    G = (0.5870 * img[:,:,1])                           #given formula to convert the planes to grayscale
    B = (0.1140 * img[:,:,2])
    grayscale = (R + G + B)
    plt.imshow(grayscale, cmap=plt.cm.gray, interpolation='nearest')



def rotate(img, direc, angle):

    if(direc == 'anticlockwise'):
        rotated90 = ndimage.rotate(img, angle)
    else:
        rotated90 = ndimage.rotate(img, (-1)*angle)
    plt.imshow(rotated90, interpolation='nearest')



def cropimage(img, dist1, dist2, dist3, dist4):

    cropped = crop(img, ((dist1, dist2), (dist3, dist4), (0,0)), copy = 'False')
    plt.imshow(cropped, interpolation='nearest')



def binarythresh(img):

    grayimg = rgb2gray(img)
    globalthreshold = threshold_otsu(grayimg)
    binaryLena = grayimg > globalthreshold
    plt.imshow(binaryLena, interpolation='nearest', cmap = plt.cm.gray)





choice = int(input("Enter \n1)For resizing imagewith scaling factor: \n2)For converting RGB image to grayscale image: \n3)For rotating angle at specific angle: \n4)To rotate the image at 90 or 180 in clockwise or anticlockwise direction"))

if (choice == 1):

    x_scale = float(input("Enter the scaling factor for width: "))
    y_scale = float(input("Enter the scaling factor for height: "))
    resize1(x_scale, y_scale)


elif (choice == 2):
    rgb2grayimg(img)
    

elif (choice == 3):

    direction = str((input("Enter the direction (anticlockwise or clockwise): ")))
    angle = int(input("Enter the angle for rotation: "))
    if(direction == "anticlockwise"):
        rotate_at_angle(img, direction, angle)
    else:
        rotate_at_angle(img, direction, -1*angle)


elif (choice == 4):

    direc = str((input("Enter the direction (anticlockwise or clockwise): ")))
    angle = int(input("Enter the angle for rotation: "))
    rotate(img, direc, angle)


elif(choice == 5):

    dist4 = int(input("Enter the distance from top axis within the range ({} x {})".format(height, width)))
    dist3 = int(input("Enter the distance from bottom axis within the range ({} x {})".format(height, width)))
    dist2 = int(input("Enter the distance from left axis within the range ({} x {})".format(height, width)))
    dist1 = int(input("Enter the distance from right axis within the range ({} x {})".format(height, width)))
    
    cropimage(img, dist1, dist2, dist3, dist4)

elif (choice == 6):
    binarythresh(img)

elif (choice == 7):

    orientation = str((input("Enter the orientation in which you want to align the two images: (vertical or horizontal) ")))
    combo(img1, img2, orientation)
    
    
