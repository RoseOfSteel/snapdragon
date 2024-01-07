from snapdragon.utils.DatabaseManager import DatabaseManager
from root_path import db_path
import cv2 

class Identifier:
    """
    Constructor.
    """
    def __init__(self):
        # List of cascades that can be used to identify an object
        self.cascades = ["haarcascade_eye.xml",
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

    """
    Identify an object in an image.

    raw_img(str): The path to the image that needs to be identified.
    return: The name of the haar cascade that was used to identify the image (or None if the image was not identified.
    """
    def identify_img(self, raw_img):
        # Read in the image 
        img = cv2.imread(raw_img) 
  
        # Convert image to grayscale 
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Iterate through the cascades
        found = None
        for cascade in self.cascades:
            # Load the haar
            haar_cascade = cv2.CascadeClassifier("resources/haars/"+cascade)
            
            # Search for item in grayscale image using the haar cascade
            identified_items = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

            # Report if the haar detected an image
            if len(identified_items) == 0:
                print("Found Nothing!")
            else:
                print("Found Something! " + "(" + cascade +")")
                found = cascade
                break

        # The name of the cascade or "None" if nothing was found
        return found


    """
    Find details on the identified item using the cascade that identified the image.

    cascade(str): The name of the cascade used to identify the image.
    return: List of the database results (the item name and definition).
    """
    def query_item_data(self, cascade):
        dm = DatabaseManager(db_path)
        dm.connect()
        result = dm.query_identifier(cascade)
        dm.close()
        return result

# Test the Identifier 
identifier = Identifier()
item = identifier.identify_img("test_img.png")
from_db = identifier.query_item_data(item)
name = from_db[0][0]
definition = from_db[0][1]
print("You found a " + name + ". And here is some more information: " + definition)


