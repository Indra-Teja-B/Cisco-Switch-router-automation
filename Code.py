from netmiko import ConnectHandler

# Define multiple devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.159.10",
        "username": "admin",
        "password": "Cisco"
    },
]

# Configuration commands
config_commands = [
    "hostname AutoRouter",

    # VLAN creation
    "vlan 10",
    "name Users",
    "vlan 20",
    "name Servers",

    # Assign IPs to VLAN interfaces (SVIs)
    "interface vlan 10",
    "ip address 10.10.10.10 255.255.255.0",
    "no shutdown",
    "interface vlan 20",
    "ip address 10.20.10.10 255.255.255.0",
    "no shutdown",

    # Add static route
    "ip route 0.0.0.0 0.0.0.0 192.168.159.254"
]

# Loop through devices
for device in devices:
    print(f"\nConnecting to {device['ip']}...")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.save_config()
    net_connect.disconnect()
    print(f"Configuration applied successfully on {device['ip']}")
