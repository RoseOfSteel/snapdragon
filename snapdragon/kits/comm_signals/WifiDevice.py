"""
Model for a WiFi device.
"""

class WifiDevice:

    # Configuration names
    DEVICE = 'device'
    INET = 'inet'
    INET4 = 'inet4'
    INET6 = 'inet6'
    NETMASK = 'netmask'
    NETMASKS = 'netmasks'
    BROADCAST = 'broadcast'
    BROADCASTS = 'broadcasts'
    
    """
    Constructor.

    interface(Interface): WiFi interface object that contains network details.
    """
    def __init__(self, interface):
        self.interface = interface

    """
    Get the name of the device.

    return: Device name
    """
    def get_name(self):
        return self.interface[self.DEVICE]

    """
    Get the first identified IP address.

    return: IP address
    """
    def get_inet(self):
        return self.interface[self.INET]

    """
    Get the list IPv4 addresses.

    return: List of IPv4 addresses.
    """
    def get_inet4(self):
        return self.interface[self.INET4]

    """
    Get the list IPv6 addresses.

    return: List of IPv6 addresses.
    """
    def get_inet6(self):
        return self.interface[self.INET6]

    """
    Get the first identified netmask.

    return: Netmask
    """
    def get_netmask(self):
        return self.interface[self.NETMASK]

    """
    Get the list of netmasks.

    return: List of netmasks
    """
    def get_netmasks(self):
        return self.interface[self.NETMASKS]

    """
    Get the first identified broadcast address.

    return: Broadcast address
    """
    def get_broadcast(self):
        return self.interface[self.BROADCAST]

    """
    Get the list of broadcast addresses.

    return: List of broadcast addresses
    """
    def get_broadcasts(self):
        return self.interface[self.BROADCASTS]

    """
    Prints a single configuration for this Wifi device.

    name(str): Name of the configuration.
    config: Configuration to print
    """
    def print_config(self, name, config):
        print(name.upper() + " : " + str(config))

    """
    Prints all configurations for this Wifi device.
    """
    def print_full(self):
        self.print_config(self.DEVICE, self.get_name())
        print("*******************************")
        self.print_config(self.INET, self.get_inet())
        self.print_config(self.INET4, self.get_inet4())
        self.print_config(self.INET6, self.get_inet6())
        self.print_config(self.NETMASK, self.get_netmask())
        self.print_config(self.NETMASKS, self.get_netmasks())
        self.print_config(self.BROADCAST, self.get_broadcast())
        self.print_config(self.BROADCASTS, self.get_broadcasts())
        print("\n")
