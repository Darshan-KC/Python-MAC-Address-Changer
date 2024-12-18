# Python MAC Address Changer

A cross-platform Python script to change the MAC address of a network interface. This script is helpful for privacy purposes or penetration testing.

## Features
- Supports Linux and macOS for MAC address changes.
- Displays the current MAC address before modification.
- Validates the new MAC address format.
- Provides informative messages for Windows users.
- Implements object-oriented programming (OOP) principles.

## Prerequisites
- **Python**: Ensure Python 3.6 or higher is installed.
- **Administrator Privileges**: The script requires elevated permissions to modify network settings.
- **Linux/macOS Tools**: `ifconfig` utility must be installed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Darshan-KC/Python-MAC-Address-Changer.git
   cd Python-MAC-Address-Changer
   ```
2. Install Python dependencies (if any). This script does not require external libraries.

## Usage

Run the script with Python:

```bash
sudo python3 mac_address_changer.py
```

### Steps:
1. Enter the network interface (e.g., `eth0` for Linux, `en0` for macOS).
2. Enter the new MAC address in the format `00:11:22:33:44:55`.
3. The script will:
   - Display the current MAC address.
   - Attempt to change it to the specified address.
   - Confirm the success of the operation.

### Example:
```text
[INFO] MAC Address Changer
Enter the interface (e.g., eth0, wlan0): eth0
Enter the new MAC address (e.g., 00:11:22:33:44:55): 00:11:22:33:44:55
[INFO] Current MAC address: 84:2A:FD:94:E6:B2
[INFO] Disabling eth0...
[INFO] Changing MAC address to 00:11:22:33:44:55...
[INFO] Enabling eth0...
[SUCCESS] MAC address successfully changed to 00:11:22:33:44:55
```

## Supported Platforms
- **Linux**: Fully supported for disabling, changing, and enabling interfaces.
- **macOS**: Fully supported using `ifconfig` commands.
- **Windows**: Informational messages provided as Windows does not natively support changing MAC addresses via the command line.

## Notes
- On **Windows**, use third-party tools or manually change the MAC address via adapter settings.
- Ensure the `ifconfig` utility is available on Linux/macOS. For Linux, it can typically be installed via:
  ```bash
  sudo apt install net-tools
  ```

## Limitations
- Does not provide a graphical user interface (GUI).
- Requires `sudo` or administrative privileges to run.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository and submit pull requests for new features, bug fixes, or improvements.

## Author
[Darshan KC](https://github.com/Darshan-KC)

---

### Disclaimer
Changing your MAC address might violate the terms of service of your network provider. Use this tool responsibly and only for ethical purposes.

