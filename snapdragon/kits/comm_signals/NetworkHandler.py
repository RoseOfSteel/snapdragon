import ifcfg
import subprocess 
import bluetooth
import re
from WifiDevice import WifiDevice
from WifiNetwork import WifiNetwork
from BluetoothDevice import BluetoothDevice
from collections import OrderedDict

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
        devices = subprocess.check_output(['netsh','wlan','show','network']) 

        """
        The output looks like this but with multiple networks. Need to split it up
        so we can store information for individual networks.

        EX:
        SSID 12 : NAME_OF_NETWORK
        Network type            : Infrastructure
        Authentication          : WPA3-Personal
        Encryption              : CCMP
        """

        # Use "SSID" as the delimeter
        device = re.split('(SSID)', str(devices))
        fresh_list = []


        first = True
        for item in device:

            """
            Skip first iteration which will contain the header.

            EX:
            Interface name : Wi-Fi 
            There are 1 networks currently visible.

            """
            if first:
                first = False
                continue
            
            # Remove the individual "SSID" entry from the array (result of split function)
            # and then re-add "SSID" to the string
            if item != "SSID":
                fresh_list.append("SSID" + item)


        # Clean the string of networks and store as individual devices
        all_networks = []

        for device in fresh_list:
            # String processing to break out the individual config items
            d = {}

            # Strip white space and new lines
            target = device.replace('\\r\\n', '')

            # Pull the information from the string and store it
            # Need a special regex for the last item since it searches for the end of the string
            d['ssid'] = (re.findall(r"SSID\s+[0-9]+\s+:\s+(.+?)Network",target))[0].strip()
            d['network type'] = (re.findall(r"Network type\s+:(.+?)Authentication",target))[0].strip()
            d['authentication']= (re.findall(r"Authentication\s+:(.+?)Encryption",target))[0].strip()
            d['encryption'] =(re.findall(r"Encryption\s+:\s+(.+?)\s+.*$",target))[0].strip()
        
            # Create an internal network object
            network = WifiNetwork(d)

            # Store all networks
            all_networks.append(network)

        return all_networks

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
