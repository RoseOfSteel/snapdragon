from snapdragon.utils.DatabaseManager import DatabaseManager
from root_path import db_path

"""
This class manages functions needed to manage product delivery instructions.
"""
class DeliveryManager:
    """
    Constructor.
    """
    def __init__(self):
        pass

    """
    Retrieve the instructions to deliver a particular product.

    name(str): Name of the object you need instructions for.
    software(bool): True if you want the software deliverable instructions. False if not.
    hardware(bool): True if you want the hardware deliverable instructions. False if not.
    documentation(bool): True if you want the documentation deliverable instructions. False if not.

    return: List with instructions retrieved from the database.
    """
    def retrieve_delivery_instructions(self, name, software, hardware, documentation):
        dm = DatabaseManager(db_path)
        dm.connect()
        result = dm.query_delivery_instructions(name, software, hardware, documentation)
        dm.close()
        return result

# Test the Delivery Handler
delivery_manager = DeliveryManager()
result = delivery_manager.retrieve_delivery_instructions("cubesat", True, True, False)
print(result)

delivery_manager = DeliveryManager()
result = delivery_manager.retrieve_delivery_instructions("AI Software", True, True, True)
print(result)
    
