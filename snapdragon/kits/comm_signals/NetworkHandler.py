import ifcfg
import bluetooth
from WifiDevice import WifiDevice
from BluetoothDevice import BluetoothDevice

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

        # Convert discovered devices to an internal type (easier to access)
        for name, interface in ifcfg.interfaces().items():
            device = WifiDevice(interface)
            
            # Update the list of devices
            devices.append(device)
            
        return devices

    """
    Print details for all identified wifi devices on the network.

    devices(list): List of identified wifi devices.
    """
    def print_wifi_devices(self, devices):
        for device in devices:
            device.print_full()

    """
    Retrieve information for Bluetooth devices.

    return: List of devices and their details.
    """
    def get_bluetooth_device_details(self):
        devices = []
        discovered_devices = bluetooth.discover_devices(lookup_names=True)

        # Convert discovered devices to an internal type (easier to access)
        for device in discovered_devices:
            bt_device = BluetoothDevice(device)

            # Update the list of devices
            devices.append(bt_device)
        
        return devices

    """
    Print details for all identified bluetooth devices on the network.

    devices(list): List of identified bluetooth devices.
    """
    def print_bluetooth_devices(self, devices):
        for device in devices:
            device.print_full()

# Test the Network Handler
nd = NetworkHandler()

#Test Wifi
wifi_devices = nd.get_wifi_device_details()
nd.print_wifi_devices(wifi_devices)

# Test Bluetooth
bluetooth_devices = nd.get_bluetooth_device_details()
nd.print_bluetooth_devices(bluetooth_devices)
