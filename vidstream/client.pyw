import vidstream
import threading

# Replace with the IP address of the receiver machine
receiver_ip = 'la-grocery.gl.at.ply.gg'

# Start the screen sharing client
sender = vidstream.ScreenShareClient(receiver_ip, 17306)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("Type 'STOP' to stop sharing: ").upper() != 'STOP':
    continue

sender.stop_stream()
