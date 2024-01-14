from snapdragon.interfaces.MicrocontrollerInterface import MicrocontrollerInterface

"""
Model for an RFID device.
"""

class RfidHandler:

    # Create the microcontroller interface
    mci = MicrocontrollerInterface()
    
    """
    Constructor.
    """
    def __init__(self):
        pass


    """
    Read the data from the RFID tag.

    return: Data from the RFID tag
    """
    def read_tag(self):
        controller_output = self.mci.receive_output_only()
        return controller_output


# Test reading the RFID tag
rh = RfidHandler()
output = rh.read_tag()
print(output)
    

    
    
