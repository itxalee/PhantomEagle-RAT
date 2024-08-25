import socket

def receive_file(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on {host}:{port}...")

    conn, addr = server.accept()
    print(f"Connection established with {addr}")

    # Receive the filename, which ends with a newline character
    filename = b''
    while True:
        part = conn.recv(1)
        if part == b'\n':
            break
        filename += part
    filename = filename.decode()  # Convert from bytes to string

    print(f"Receiving file: {filename}")

    # Create a new file with the received filename
    with open(f"received_{filename}", 'wb') as file:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            file.write(data)

    print(f"File '{filename}' received successfully.")
    conn.close()
    server.close()

if __name__ == "__main__":
    host = '127.0.0.1'  # Listen on all available interfaces
    port = 9443

    receive_file(host, port)
