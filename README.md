# Traffic Sign Recognition
This is my first project about training a deep learning algorithm for road traffic signs recognition and was mostly inspired by the Traffic Signs detection competition in Kaggle : https://www.kaggle.com/c/traffic-sign-recognition/overview

For this project, I used the German Traffic Sign dataset from the Institut Fur Neuroinformatik :  https://benchmark.ini.rub.de/

_J. Stallkamp, M. Schlipsing, J. Salmen and C. Igel, "The German Traffic Sign Recognition Benchmark: A multi-class classification competition," The 2011 International Joint Conference on Neural Networks, San Jose, CA, 2011, pp. 1453-1460, doi: 10.1109/IJCNN.2011.6033395.

## Dataset structure

This dataset consists in 43 classes of more than 50 000 images using for training, validation and test. The datasets are divided as follow :

*34799 images for the training set.
*4410 images for the validation set.
*12630 images for the test set.*

The images' shapes are (32, 32, 3).

The training set archive is structured as follows :
*One directoy per class 
*Each directory contains one **Comma Separated Value (CSV)** file with annotations (GT-ClassID.csv), as well as the training images.
*Training images are grouped by tracks.
*Each tracks contains 30 images of one single physical traffic sign.*
  
## Image format

The image format is structured as follows:

*The images contain one traffic sign each.
*Images contain a border of 10% around the actual traffic sign (cropped to at least 5 pixels) to allow for edge-based approaches.
*They are stored in Picle format. (PPM format).
*Images sizes vary from 15x15 to 250x250 and aren't necessarily squared.
*Some of the traffic sign are not necessarily centered within the image. This is only valid for images that were close to the image border in the before-cropped image.*

The 43 different classes are :

*0,Speed limit (20km/h)
*1,Speed limit (30km/h)
*2,Speed limit (50km/h)
*3,Speed limit (60km/h)
*4,Speed limit (70km/h)
*5,Speed limit (80km/h)
*6,End of speed limit (80km/h)
*7,Speed limit (100km/h)
*8,Speed limit (120km/h)
*9,No passing
*10,No passing for vehicles over 3.5 metric tons
*11,Right-of-way at the next intersection
*12,Priority road
*13,Yield
*14,Stop
*15,No vehicles
*16,Vehicles over 3.5 metric tons prohibited
*17,No entry
*18,General caution
*19,Dangerous curve to the left
*20,Dangerous curve to the right
*21,Double curve
*22,Bumpy road
*23,Slippery road
*24,Road narrows on the right
*25,Road work
*26,Traffic signals
*27,Pedestrians
*28,Children crossing
*29,Bicycles crossing
*30,Beware of ice/snow
*31,Wild animals crossing
*32,End of all speed and passing limits
*33,Turn right ahead
*34,Turn left ahead
*35,Ahead only
*36,Go straight or right
*37,Go straight or left
*38,Keep right
*39,Keep left
*40,Roundabout mandatory
*41,End of no passing
*42,End of no passing by vehicles over 3.5 metric tons

