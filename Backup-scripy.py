from netmiko import ConnectHandler
import datetime
import os

# Folder where backups will be saved
backup_folder = r"C:\Cisco_Backups"   
os.makedirs(backup_folder, exist_ok=True)

# Device inventory (add more switches here)
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.159.33",
        "username": "admin",
        "password": "Cisco",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.159.34",   
        "username": "admin",
        "password": "Cisco",      
    },
]

# Timestamp for filenames
date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

for device in devices:
    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show running-config")

        filename = os.path.join(
            backup_folder, f"{device['ip']}_backup_{date}.txt"
        )

        with open(filename, "w") as f:
            f.write(output)

        print(f"✅ Backup saved: {filename}")
        net_connect.disconnect()
    except Exception as e:
        print(f"❌ Failed to backup {device['ip']}: {e}")
