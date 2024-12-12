import subprocess
import re
import sys

class MACAddressChanger:
    """
    A class to manage and change the MAC address of a network interface.
    
    Attributes:
        interface (str): The network interface to modify (e.g., 'eth0', 'wlan0').
        new_mac (str): The new MAC address to set.
    """
    
    def __init__(self, interface:str, new_mac:str):
        """
        Initialize the MACAddressChanger with the interface ande new MAC address.
        
        Args:
            interface (str): The network interface to modify.
            new_mac (str): The new MAC address to set.
        """
        self.interface = interface
        self.new_mac = new_mac
        
    @staticmethod
    def validate_mac(mac):
        """
        Validate the MAC address format.
        
        Args:
            mac (str): The MAC address to validate.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
        return re.match(pattern,mac) is not None