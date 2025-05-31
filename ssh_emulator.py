import socket
import threading
from datetime import datetime
from honeynet.logger import log_attempt

FAKE_BANNER = "SSH-2.0-OpenSSH_4.3\r\n"

def handle_client(client_socket, addr):
    ip = addr[0]
    print(f"[SSH] Connection from {ip}")
    try:
        client_socket.sendall(FAKE_BANNER.encode())
        user_agent = "SSH Scanner or Client"
        log_attempt(ip, "ssh-connection", "N/A", user_agent)
    except Exception as e:
        print(f"[SSH] Error: {e}")
    finally:
        client_socket.close()

def run_ssh_emulator(port=2222):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[SSH] Fake SSH server running on port {port}")
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()
