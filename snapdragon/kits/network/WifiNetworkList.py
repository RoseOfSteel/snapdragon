import re
from WifiNetwork import WifiNetwork

"""
This class manages a list of networks.

Note:
A key portion of this class handles cleaning up a network list and storing the data into
a usable object. This is neeed because the subprocess output used to retrieve the network
information returns a string (rather than a list of network items with details on their
configurations).
"""
class WifiNetworkList:
    
    # Network configuration names
    SSID = 'ssid'
    NETWORK_TYPE = 'network type'
    AUTHENTICATION = 'authentication'
    ENCRYPTION = 'encryption'

    """
    Constructor.

    wifi_networks(str): Raw string of wifi networks (from subprocess output).
    """
    def __init__(self, wifi_networks):
        # Current state of the wifi network list
        self.current = wifi_networks

    """
    The output looks like this but with multiple networks. Need to split it up
    so we can store information for individual networks. This methos is the first
    step of the process needed to prep the data by splitting the string and putting information
    for each network into its own list index.

    EX:
    SSID <#> : <Name of Network>
    Network type            : <Infrustructure Type>
    Authentication          : <Authentication Type>
    Encryption              : <Encryption Type>

    Final result is the list with all network information put into their own indices. 
    """
    
    def extract_networks_from_receiver_output(self):
        # Use "SSID" as the delimeter to get each network description into it's own list index,
        # and update the network list.
        self.current = re.split('(SSID)', str(self.current))
        

    """
    Remove as much clutter as possible from the list of wifi networks and prep the list.
    """
    def remove_network_clutter(self):
        first = True
        prepped_list = []
        for network in self.current:

            """
            Skip first iteration which will contain the header.

            EX:
            Interface name : Wi-Fi 
            There are 1 networks currently visible.

            """
            if first:
                first = False
                continue
            
            """
            Remove the individual "SSID" entry from the array (result of split function)
            and then re-add "SSID" to the string.
            """
            if network != "SSID":
                prepped_list.append("SSID" + network)

        # Update the network list
        self.current = prepped_list

    """
    Go through all the stored data (strings at this point), pull individual network configurations,
    and store them to an object that is easier to use.
    """
    def pull_network_config_info_from_raw_string(self):
        # Clean the string of networks and store as individual devices
        all_networks = []

        for network in self.current:
            # String processing to break out the individual config items
            d = {}

            # Pull the information from the string and store it
            # Need a special regex for the last item since it searches for the end of the string
            SSID_REG = r"SSID\s+[0-9]+\s+:\s+(.+?)Network"
            NETWORK_TYPE_REG = r"Network type\s+:(.+?)Authentication"
            AUTHENTICATION_REG = r"Authentication\s+:(.+?)Encryption"
            ENCRYPTION_REG = r"Encryption\s+:\s+(.+?)\s+.*$"

            # Store the config information in a dictionary
            # so we can easily pass it off and create an actual network object
            d[self.SSID] = self.pull_config_from_network_string(SSID_REG,network)
            d[self.NETWORK_TYPE] = self.pull_config_from_network_string(NETWORK_TYPE_REG,network)
            d[self.AUTHENTICATION]= self.pull_config_from_network_string(AUTHENTICATION_REG,network)
            d[self.ENCRYPTION] = self.pull_config_from_network_string(ENCRYPTION_REG,network)
        
            # Create an internal network object
            network = WifiNetwork(d)

            # Store all networks
            all_networks.append(network)

        # Update the network list
        self.current = all_networks

    """
    Get the config information from a string using a regex.

    network(str): String with the network information in it.

    return: Single string with config information in it
    """
    def pull_config_from_network_string(self, regex, network):

        # Get the substring with the config
        regex_result = re.findall(regex,network)

        # Remove the data from the list created by regex and strip whitespace
        raw_config = regex_result[0].strip()

        # Remove carriage return and whitespace characters
        return raw_config.replace('\\r\\n', '')

    """
    Pull all the data from raw network output and store to an object that is easier to use.

    return: Clean list of network objects
    """
    def save_all_networks_from_raw_network_output(self):
        self.extract_networks_from_receiver_output()
        self.remove_network_clutter()
        self.pull_network_config_info_from_raw_string()
        return self.current

