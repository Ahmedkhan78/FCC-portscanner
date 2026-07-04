import socket
import ipaddress
from common_ports import ports_and_services as ps


def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Step 1: Resolve hostname → IP
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        # Step 2: If DNS fails, check if it's a valid IP
        try:
            ipaddress.ip_address(target)
            return "Error: Invalid IP address"
        except ValueError:
            return "Error: Invalid hostname"

    # Step 3: Scan ports (IMPORTANT: use IP, not target)
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)

    # Step 4: Non-verbose mode
    if not verbose:
        return open_ports

    # Step 5: Get hostname (reverse lookup)
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        display_host = hostname if hostname != ip else target
    except socket.herror:
        display_host = target if ip != target else ip

    # Step 6: Build output EXACT format
    if display_host and display_host != ip:
        header = f"Open ports for {display_host} ({ip})"
    else:
        header = f"Open ports for {ip}"

    lines = [header, "PORT     SERVICE"]

    for port in open_ports:
        service = ps.get(port, "unknown")
        lines.append(f"{port:<9}{service}")

    return "\n".join(lines)
