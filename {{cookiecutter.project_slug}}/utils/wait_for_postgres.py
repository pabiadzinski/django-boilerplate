import random
import socket
import time

if __name__ == "__main__":
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(("postgres", 5432))
                print("Postgres is ready!")
                break
        except socket.error:
            print("Postgres isn't ready. Waiting for")
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
