"""
Model for a Bluetooth device.
"""

class BluetoothDevice:
    
    # Configuration names
    NAME = 'name'
    ADDR = 'address'
    
    """
    Constructor.
    """
    def __init__(self, device):
        self.device = device

    """
    Get the name of the device.
    Note: Original information in a tuple (addr, name)

    return: Device name
    """
    def get_name(self):
        return self.device[1]

    """
    Get the device address.
    Note: Original information in a tuple (addr, name)

    return: Device address
    """
    def get_addr(self):
        return self.device[0]

    """
    Prints a single configuration for this Bluetooth device.

    name(str): Name of the configuration.
    config: Configuration to print
    """
    def print_config(self, name, config):
        print(name.upper() + " : " + str(config))


    """
    Prints all configurations for this Bluetooth device.
    """
    def print_full(self):
        self.print_config(self.NAME, self.get_name())
        print("*******************************")
        self.print_config(self.ADDR, self.get_addr())
        print("\n")

    
