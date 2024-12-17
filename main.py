import subprocess
import re
import sys
import platform

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
    
    def get_current_mac(self):
        """
        Get the current MAC address of the network interface.

        Returns:
            str: The current MAC address if found.

        Raises:
            RuntimeError: If the MAC address cannot be retrieved.
        """
        
        try:
            # Check the operating system
            system_platform = platform.system().lower()
            
            if system_platform == "linux" or system_platform == "darwin":  # For Linux and macOS
                result = subprocess.check_output(["ifconfig", self.interface], text=True)
                mac_address = re.search(r"ether ([0-9a-fA-F:]{17})", result)
                if mac_address:
                    return mac_address.group(1)
                else:
                    raise RuntimeError(f"Could not read MAC address from {self.interface}")
            
            elif system_platform == "windows":  # For Windows
                result = subprocess.check_output(["ipconfig", "/all"], text=True)
                # Search for the MAC address in the result
                mac_address = re.search(r"([a-fA-F0-9]{2}[-:]){5}[a-fA-F0-9]{2}", result)
                if mac_address:
                    return mac_address.group(0).replace('-', ':')  # Normalize the MAC address
                else:
                    raise RuntimeError(f"Could not read MAC address for {self.interface}")
            
            else:
                raise RuntimeError(f"Unsupported operating system: {system_platform}")

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to retrieve MAC address: {e}")
        
    def change_mac(self):
        """
        Change the MAC address of the network interface.

        Raises:
            RuntimeError: If any system command fails.
        """
        
        # Checking the OS
        system_platform = platform.system().lower()
        
        try:
            if system_platform == "windows":
                print("[INFO] Windows does not natively support changing MAC addresses via command line.")
                print("[INFO] Use third-party tools or manually change MAC address in adapter settings.")
            elif system_platform == "darwin":  # macOS
                print(f"[INFO] Disabling {self.interface}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "down"], check=True)

                print(f"[INFO] Changing MAC address to {self.new_mac}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "ether", self.new_mac], check=True)

                print(f"[INFO] Enabling {self.interface}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "up"], check=True)

                print(f"[SUCCESS] MAC address changed successfully!")
            else:  # Linux
                print(f"[INFO] Disabling {self.interface}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "down"], check=True)

                print(f"[INFO] Changing MAC address to {self.new_mac}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "hw", "ether", self.new_mac], check=True)

                print(f"[INFO] Enabling {self.interface}...")
                subprocess.run(["sudo", "ifconfig", self.interface, "up"], check=True)

                print(f"[SUCCESS] MAC address changed successfully!")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to change MAC address: {e}")
        
    def run(self):
        """
        Execute the MAC Address change process.
        Verifies the new MAC address format, retrieves the current MAC, and updates it.
        """
        
        if not self.validate_mac(self.new_mac):
            print("[ERROR] Invalid MAC address format.")
            sys.exit(1)

        try:
            current_mac = self.get_current_mac()
            print(f"[INFO] Current MAC address: {current_mac}")

            self.change_mac()
            
            system_platform = platform.system().lower()
            
            if system_platform != "windows":
                update_mac = self.new_mac
                if update_mac == self.new_mac:
                    print(f"[SUCCESS] MAC address successfully changed to {update_mac}")
                else:
                    print(f"[ERROR] MAC address change failed.")
        
        except RuntimeError as e:
            print(f"[ERROR] {e}")
            sys.exit(1)
        
        
if __name__ == "__main__":
    print("[INFO] MAC Address Changer")
    interface = input("Enter the interface (e.g., eth0, wlan0): ").strip()
    new_mac = input("Enter the new MAC address (e.g., 00:11:22:33:44:55): ").strip()

    changer = MACAddressChanger(interface, new_mac)
    changer.run()