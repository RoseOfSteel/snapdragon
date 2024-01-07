from snapdragon.utils.DatabaseManager import DatabaseManager
from root_path import db_path


class SensorHandler:
    """
    Constructor.
    """
    def __init__(self):
        pass

    """
    Retrieve the code needed to describe an object.

    name(str): Name of the object.
    sensor_type(str): The type of sensory description (e.g., smell or touch).

    return: Code that can be used to command the hardware that will describe the object.
    """
    def retrieve_code(self, name, sensor_type):
        dm = DatabaseManager(db_path)
        dm.connect()
        result = dm.query_sensor_data(name, sensor_type)
        dm.close()

        # Clean up the result assuming there is something there
        if len(result) > 0:
            result = dm.clean_query_result(result)
        return result

# Test the Sensor Handler
# Test for a good description
sensor_handler = SensorHandler()
result = sensor_handler.retrieve_code("fruit", "smell")
print(result)

# Test for a missing description
result = sensor_handler.retrieve_code("fruit", "touch")
print(result)
