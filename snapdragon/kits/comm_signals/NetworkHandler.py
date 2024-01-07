import ifcfg
import subprocess 
import bluetooth

from WifiDevice import WifiDevice
from WifiNetworkListManager import WifiNetworkListManager
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

    """
    Get list of discovered wifi networks.

    return: List of wifi networks
    """
    def get_wifi_networks(self):
        discovered_devices = subprocess.check_output(['netsh','wlan','show','network'])
        networks = WifiNetworkListManager(discovered_devices)
        return networks.save_all_networks_from_raw_network_output()

        
    """
    Print details for all identified wifi networks.

    networks(list): List of identified wifi networks.
    """
    def print_wifi_networks(self, networks):
        for network in networks:
            network.print_full()

# Test the Network Handler
nd = NetworkHandler()

"""
# Test Wifi Devices
wifi_devices = nd.get_wifi_device_details()
nd.print_wifi_devices(wifi_devices)

# Test Bluetooth Signals
bluetooth_devices = nd.get_bluetooth_device_details()
nd.print_bluetooth_devices(bluetooth_devices)
"""

# Test Retrieving Wifi Networks
networks = nd.get_wifi_networks()
nd.print_wifi_networks(networks)
