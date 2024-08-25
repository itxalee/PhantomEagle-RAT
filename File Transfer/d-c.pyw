import socket
import os
import sys

def upload_file(server_ip, port, filepath):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))

    filename = os.path.basename(filepath)
    client.send(filename.encode() + b'\n')  # Send the filename followed by a newline character

    with open(filepath, 'rb') as file:
        client.sendfile(file)

    print(f"File '{filepath}' uploaded successfully.")
    client.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python upload_file.py <PUBLIC_SERVER_IP> <PORT> <LOCAL_FILE_PATH>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    filepath = sys.argv[3]

    upload_file(server_ip, port, filepath)
