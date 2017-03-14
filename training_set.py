import os                                                                       # import for taking the imagePaths
import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
from PIL import Image                                                           # for Image.open(imagePath).convert('L')

recognizer = cv2.createLBPHFaceRecognizer()                                     # Local Binary Patterns Histograms
path = './dataset'                                                              # Folder where faces are saved

def getImagesWithID(path):      
    imageFolders = [os.path.join(path, f) for f in os.listdir(path)]    # Joining './dataset' and '<image names>'
    faces = []                                                                  # Empty array for faces
    Ids = []
    for imageFolder in imageFolders:
        imagePaths = [os.path.join(imageFolder, f) for f in os.listdir(imageFolder)]
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')        # Converting colored and GrayScale images into bilevel images using Floyd-Steinberg dither
            faceNp = np.array(faceImg, 'uint8')                                     # Converting face array into numpy array
            ID = int(os.path.split(imagePath)[-1].split('.')[1])                    # Check this again
            faces.append(faceNp)                                                    # adding the dilevel face into faces array
            Ids.append(ID)                                                          # index of ID and faceNp is same in both arrays
            cv2.imshow("Training", faceNp)                                          # Showing the faces which are getting trained
            cv2.waitKey(10)
                                                                        # Empty array for Person Ids
                                                             # Waiting time id 10 milisecond
    return Ids, faces

Ids, faces = getImagesWithID(path)                                              # Calling the function
recognizer.train(faces, np.array(Ids))                                          # Training the faces
recognizer.save('./recognizer/trainingData.yml')                                # Saving the yml file
cv2.destroyAllWindows()                                                         # Closing all the opened windows
