"""
Model for Wifi Networks.
"""

class WifiNetwork():

    # Network configuration names
    SSID = 'ssid'
    NETWORK_TYPE = 'network type'
    AUTHENTICATION = 'authentication'
    ENCRYPTION = 'encryption'
    
    """
    Constructor.

    network: Wifi network in the form of a dictionary
    """
    def __init__(self, network):
        self.network = network

    """
    Get the SSID.

    return: SSID
    """
    def get_ssid(self):
        return self.network[self.SSID]

    """
    Get the network type.

    return: Network type
    """
    def get_network_type(self):
        return self.network[self.NETWORK_TYPE]

    """
    Get the authentication type.

    return: Authentication type
    """
    def get_authentication(self):
        return self.network[self.AUTHENTICATION]

    """
    Get the encryption type.

    return: Encryption type
    """
    def get_encryption(self):
        return self.network[self.ENCRYPTION]

    """
    Prints a single configuration for this Wifi network.

    name(str): Name of the configuration.
    config: Configuration to print
    """
    def print_config(self, name, config):
        print(name.upper() + " : " + str(config))

    """
    Prints all configurations for this Wifi network.
    """
    def print_full(self):
        self.print_config(self.SSID, self.get_ssid())
        print("*******************************")
        self.print_config(self.NETWORK_TYPE, self.get_network_type())
        self.print_config(self.AUTHENTICATION, self.get_authentication())
        self.print_config(self.ENCRYPTION, self.get_encryption())
        print("\n")
