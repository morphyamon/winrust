import socket
import os
import sys

# Ensure correct usage
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <server_ip> <server_port>")
    sys.exit(1)

# Set up server details from command-line arguments
server_ip = sys.argv[1]  # IP of the receiving PC
server_port = int(sys.argv[2])  # Port number

# Path to the screenshot
screenshot_path = ".\screenshot.png"

# Check if the file exists
if os.path.exists(screenshot_path):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Open the file and send it
    with open(screenshot_path, "rb") as f:
        while True:
            # Read the file in chunks and send
            data = f.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    # Close the connection
    client_socket.close()
    print("[*] File sent successfully.")
else:
    print(f"[!] File {screenshot_path} does not exist.")
