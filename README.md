# Role-playing game using Artificial Intelligence
<b>Author: Almudena Ramírez</b>

This project consists of a role-playing game that can interact with a d20 die.
It was divided into two parts:
1. A neural network is trained to identify the number of a d20 die with a camera. 
2. The detected number would modify, depending on its value, a story presented through streamlit. 

## Workflow
1. Preparation of the dataset
2. Exploratory analysis of the data
3. Configuration of the model
4. Training of the data
5. Creation of the history and its different parts
6. Creation of the dashboard

## 1. Preparation of the dataset
### Database
The database used for this project are the d20 images: https://www.kaggle.com/datasets/ucffool/dice-d4-d6-d8-d10-d12-d20-images. Most of the off-angle pictures were not considered for this project because the idea is to recognice the number of the dice from above.
Since important data was missing, I had to add some photos manually. All the images were classified in train/ test folders and manually classified in sub-folders.

### Augmentation of database
The photos added manually did not have any variations (e.g.: rotations), so at first I did that manually, which took me a lot of time. Later on the project I discovered that this job could be done using https://www.educba.com/keras-imagedatagenerator/ or https://roboflow.com/.

### Labeling
The parts of the dice that contained information was labelled using https://labelstud.io/. After every image was labelled I exported the data as XML, which I converted into csv and TFrecord with https://roboflow.com/ since the code that does that was not working properly.

## 2. Exploratory analysis of the data
As I worked with the dataset manually, I took care of most of the pictures that were blurry and off-angle, making it difficult even for a person to detect which number was on top. By the time everything was classified I used a jupyter notebook to separate each picture's path in a dataframe. This was useful to know how the data was distributed and made me realize I had to augmentate the dataset of photos I took myself.

## 3. Configuration of the model
### Mobilenet V2
The first pre-trained model I tried was Mobilenet (https://keras.io/api/applications/mobilenet/). I did this in a Google Collab file (https://colab.research.google.com/drive/1wkf-3po4DG9aOADKbDNF4P-lu8BZFMdC#scrollTo=rg1gJmaf0Hfm) and everything worked just fine. I got to train my dataset with this model but the results were very bad so I decided to try another model.

### Faster RCNN
#### Faster RCNN Inception V2
After the first try I followed a tutorial that was very similar to my goal (https://towardsdatascience.com/calculating-d-d-damage-with-tensorflow-88db84604f0a). I got this pre-trained model from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md. However, I had a lot of issues with my code and getting some files from the model I did not understand.

#### Faster RCNN Resnet-101 V1
At this point we considerated that the problem might be resolved using Windows. I installed everything I needed and prepared Windows so I could start over. This time I followed a more extensive tutorial (https://www.youtube.com/watch?v=SJRP0IRfPj0&t=0s) that used Faster RCNN Resnet-101  V1. When everything was ready to run the training, several protoc-related issues appeared, and I still have not found a solution for the last one.

The new repository using Windows is https://github.com/Almudena607/bdml_final_project.
