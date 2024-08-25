import vidstream
import threading

# Start the server
receiver = vidstream.StreamingServer('127.0.0.1', 9443)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("Type 'STOP' to stop the server: ").upper() != 'STOP':
    continue

receiver.stop_server()
