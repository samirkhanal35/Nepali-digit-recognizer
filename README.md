# Nepali Digit Recognizer

# Description

It is a recognizer developed using Tensorflow. It is used to recognize the Nepali digits from their images.<br/><br/>

<b>Design:</b><br/>
Front-end: Tkinter<br/>
Back-end: Tensorflow<br/>
Core-language: Python<br/><br/>

<b>Preprocessing:</b><br/>
The preprocessing module involves several other sub modules like Grayscale
conversion, Noise Removal, Binarization, Binarization, Gaussian Blurring and median
filtering.<br/><br/>

Grayscale conversion:<br/>
Grayscale conversion has many ways of converting colorful images into gray form. We
have used luminosity method to convert color image into gray, it can be carried out by
formula:<br/><br/>

Gr=0.21*R+0.72*G+0.07*B<br/><br/>

Algorithm:<br/>
Step 1: Read an RBG image with its height and width also.<br/>
Step 2: For any pixel, read the intensity values of Red, Blue and Green channels

as R, B and G respectively.<br/>

Step 3: Calculate the gray value, Gr = 0.21*R+0.72*G+0.07*B<br/>
Step 4: Set, R=B=G=GR<br/>
Step 5: Repeat steps from 2 to 4 until all pixels are scanned<br/><br/>
Since the OCR application potentially needs to handle the images of old and distorted
image documents, there is a big likelihood of the presence of noise in images. We have
used the median filtering, spatial filtering and gaussian filtering methods for removing
the noise, basically the salt and pepper noise, in real scanned and microfilmed image
documents.<br/><br/>
Median filtering:<br/>
It is done by calculating the median of certain window including odd number of pixels
and putting the median value to central pixel of that window. This noise reduction
method is effective for the reduction of salt and pepper noise. For implementation of
this method we have taken 3x3 window.<br/><br/>

Algorithm:<br/>
Step 1: Read gray image with its height and width.<br/>
Step 2: For any 3x3 pixel window, read gray values of all pixels and calculate

the median.<br/>


Step 3: For a window, Central_pixel_value= median_value, go to next pixel window.<br/>

Step 4: Repeat steps 2 to 3 until all pixels are scanned.<br/>
*For those pixels in a window that actually don’t exist or lie out of the image, pixel
values of their adjacent boundary pixels are taken.<br/><br/>

Gaussian Blurring:<br/>
Blurring can also be stated as smoothing because this technique helps to smooth the
edges distorted by previous methods.<br/>
Gaussian blur is based on the normal distribution of intensity of a pixel in the image
2D-plane. The 2D-gaussian function for calculation of weight of pixels in a window is
given by,<br/>

G(x,y)=
1
2πσ2
e
-(x
2+y
2
) 2σ
2 ⁄
<br/><br/>
Where, x and y as (x,y) represent the pixel vector in a window and σ is the standard
deviation of the normal distribution which is determined by using value of radius r
using the relation,<br/><br/>

r=σ√2*log(255)-1<br/><br/>

We have used Gaussian blur for 5x5 window i.e. radius r=3, which results the standard
deviation to be σ ≈ 1.823.<br/><br/>

Algorithm:<br/>
Step 1: Read gray image (after median filter) with its height and width.<br/>
Step 2: For any 5x5 window, calculate weights of all pixels using formula of

equation (3-2).<br/>

Step 3: Calculate products of pixel values and their respective weights.<br/>
Step 4: Calculate sum of all products and set Central_pixel_value=sum, go to

next pixel window.<br/>



Step 5: Repeat steps 2 to 4 until all pixels are scanned.<br/>
(*For those pixels in a window that actually don’t exist or lie out of the image, pixel
values of their adjacent boundary pixels are taken.)<br/><br/>

Binarization:<br/>
An image is called binary if the intensity value of each pixel is either 255 (white color)
or 0 (black color) i.e. logically binary values either 1 (high) or 0 (low) respectively.
Hence, the process of conversion is called binarization.<br/>
We have used global thresholding method where threshold value for all pixels of image
is same.<br/><br/>

Algorithm:<br/>
Step 1: Read the image (output of blurring) with its height and width.<br/>
Step 2: For any pixel<br/>

a. Set pixel_value=255, if pixel_value >= threshold_value.<br/>
b. Set pixel_value=0, if pixel_value < threshold_value.<br/>

Step 3: Repeat steps 2 until all pixels are scanned.<br/><br/>

<b>Segmentation</b><br/>
The segmentation means to extract characters from the text present in the image document.<br/>
We have used the concept of Point Count Approach for segmentation of characters but
with some variations as per requirements of our project.<br/> In this approach the separation
of character lines is identified by counting the number of black pixels which on
exceeding the threshold will indicate the presence of a character line otherwise the
white space or the separation. The spacing between lines are made constant for all other
lines.<br/>
In this project for segmentation, binary image is taken as input. Instead of using
constant line spacing, a flag has been used to indicate the presence or absence of line.<br/>


Similar method has been used for character detection with some alteration. For line
detection the scanning of pixels is done from left to right taking image height and width
as boundary whereas, for character detection after identifying top and bottom margins
of line:<br/>
a. First, vertical scanning of pixels is done from top to bottom margins of line
to identify the left and right margin of individual characters.<br/>
b. Second, horizontal scanning of pixels is done form left to right margins of
each character to identify their respective top and bottom margins.<br/>
As a result, four margins; left, right, top and bottom, of individual characters are
identified. These marginal values of each characters contribute for features extraction.<br/><br/>

<b>Feature Extraction</b><br/>
The segmented characters are extracted using the margins to represent a single character image. The extracted
character is then converted to mono-channel and resized to 32x32 from any size. This
helps adjusting the character image to be fit for recognition.<br/><br/>

<b>Recognition</b><br/>
For training and recognition, we have followed the Multilayered Neural Network developed using Tensorflow.<br/>
we have followed gradient descent method. It is used to decrease the cost function which is actually the difference between the predicted value
and the value to be predicted.<br/><br/>

![Digit recognizer process](https://github.com/samirkhanal35/Nepali-digit-recognizer/blob/master/minor_project_process.png)


# Visuals

![Digit recognizer](https://github.com/samirkhanal35/Nepali-digit-recognizer/blob/master/digit_recognizer.png)

# Installation and Execution

Please run the file gui.py to run the program

# Usage
