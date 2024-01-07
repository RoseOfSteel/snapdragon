from snapdragon.utils.DatabaseManager import DatabaseManager
from root_path import db_path

# Capture image
# Identify and put a name to an image
# Look for the image name in the database
# Save the image description from the database
# Return the image information to the console
# Image processing library

import cv2 

cascades = ["haarcascade_eye.xml",
"haarcascade_eye_tree_eyeglasses.xml",
"haarcascade_frontalcatface.xml",
"haarcascade_frontalcatface_extended.xml",
"haarcascade_frontalface_alt.xml",
"haarcascade_frontalface_alt2.xml",
"haarcascade_frontalface_alt_tree.xml",
"haarcascade_frontalface_default.xml",
"haarcascade_fullbody.xml",
"haarcascade_lefteye_2splits.xml",
"haarcascade_licence_plate_rus_16stages.xml",
"haarcascade_lowerbody.xml",
"haarcascade_profileface.xml",
"haarcascade_righteye_2splits.xml",
"haarcascade_russian_plate_number.xml",
"haarcascade_smile.xml",
"haarcascade_upperbody.xml"]

class Identifier:

    """
    Constructor.
    """
    def __init__(self):
        pass

    def find_img(self, raw_img):
        # Reading the image 
        img = cv2.imread(raw_img) 
  
        # Converting image to grayscale 
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Iterate through the cascades
        found = None
        for cascade in cascades:
            # Load the haar
            haar_cascade = cv2.CascadeClassifier("resources/haars/"+cascade)
            
            # Search for item in grayscale image 
            identified_items = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

            # Report if the haar detected an image
            if len(identified_items) == 0:
                print("Found Nothing!")
            else:
                print("Found Something! " + "(" + cascade +")")
                found = cascade
                break

        return found


    def find_item_data(self, classifier):
        dm = DatabaseManager(db_path)
        dm.connect()
        result = dm.query_identifier(classifier)
        dm.close()
        return result

identifier = Identifier()
item = identifier.find_img("test_img.png")
from_db = identifier.find_item_data(item)
name = from_db[0][0]
definition = from_db[0][1]
print("You found a " + name + ". And here is some more information: " + definition)


