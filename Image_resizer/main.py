
''' This is a image_resizer program in which i am going to python libraries like Opencv to resize
  or to manipulate any image .'''

'''Opencv library-: OpenCV is a huge open-source library for computer vision, machine learning, and image 
processing. It can process images and videos to identify objects, faces, or even the handwriting of a human. 
When it is integrated with various libraries, such as Numpy which is a highly optimized library for numerical 
operations,
'''


'''For which firstly you have to install the Opencv-python then import the cv2 library'''
import cv2
# Reading the image using imread() function
image=cv2.imread("dragon.jpg")
# now here i am resizing the image for that firstly know the percentage by which you are resizing your img.
resize_per=50
# calculate the 50% of the original image dimension.

width=int(image.shape[1] * resize_per/100)
height=int(image.shape[0] * resize_per/100)
# once you have the dimensions now use the resize() to resize the image.
dim=(width,height)
output=cv2.resize(image,dim)

# now create a new img file with the desire dimensions.
cv2.imwrite("newdragon.jpg",output)
cv2.waitKey(0)
# cv2.imshow("img",image)
# cv2.waitKey(1000)


# explanation
'''
 Read the Image:

Python
image = cv2.imread("dragon.jpg")
Use code with caution.
content_copy
This line reads the image named "dragon.jpg" from your current working directory using the cv2.imread() 
function. The function returns a NumPy array representing the image data. If the image is not found or 
there's an error reading it, cv2.imread() will return None.

3. Calculate Resize Percentage:

Python
resize_per = 50
Use code with caution.
content_copy
This line defines the percentage by which you want to resize the image. Here, resize_per is set to 50, 
indicating a 50% reduction in size.

4. Calculate New Dimensions:

Python
width = int(image.shape[1] * resize_per / 100)
''image.shape is a read-only property that returns a tuple containing the dimensions of the image stored 
in the NumPy array.
The order of elements in the tuple typically represents:
Height (number of rows)
Width (number of columns)
Number of channels (e.g., 3 for RGB images)''
height = int(image.shape[0] * resize_per / 100)
Use code with caution.
content_copy
image.shape is a tuple containing the image's height, width, and number of channels (usually 3 for RGB).
image.shape[1] accesses the width of the image.
The calculation image.shape[1] * resize_per / 100 determines the new width by multiplying the original 
width with the resize percentage and dividing by 100 to get a percentage value.
The int() function converts the result to an integer number of pixels.
Similar calculations are performed for height.
5. Resize the Image:

Python
dim = (width, height)
output = cv2.resize(image, dim)
Use code with caution.
content_copy
dim is a tuple containing the new dimensions (width, height) calculated in the previous step.
The cv2.resize(image, dim) function resizes the image based on the specified dim dimensions. 
The resized image is stored in the output variable.
6. Save the Resized Image:

Python
cv2.imwrite("newdragon.jpg", output)
Use code with caution.
content_copy
The cv2.imwrite("newdragon.jpg", output) function saves the resized image (output) as a new file named 
"newdragon.jpg" in your working directory.
Commented Line:

Python
# cv2.imshow("img", image)
# cv2.waitKey(0)
In OpenCV, the cv2.waitKey(delay) function waits for a specified amount of time (delay in milliseconds)
for a key press on the keyboard.

These commented lines would have displayed the original image in a window titled "img" using cv2.imshow(). 
The cv2.waitKey(0) function waits for a key press (0 indicates indefinite wait) to close the window. 
You can uncomment these lines if you want to see the original image before resizing.
'''