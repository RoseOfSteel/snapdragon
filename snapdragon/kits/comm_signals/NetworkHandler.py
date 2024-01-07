import ifcfg
from WifiDevice import WifiDevice

"""
This class handles retrieving and managing network data.
"""
class NetworkHandler():

    """
    Constructor.
    """
    def __init__(self):
        pass

    """
    Retrieve information for wifi devices.

    return: List of devices and their details.
    """
    def get_wifi_device_details(self):
        devices = []
        for name, interface in ifcfg.interfaces().items():
            device = WifiDevice(interface)
            # Update the list of devices
            devices.append(device)
        return devices

    """
    Print details for all identified wifi devices on the network.

    devices(list): List of identified network devices.
    """
    def print_all_wifi_device_details(self, devices):
        for device in devices:
            device.print_interface()


nd = NetworkHandler()
devices = nd.get_wifi_device_details()
nd.print_all_wifi_device_details(devices)
