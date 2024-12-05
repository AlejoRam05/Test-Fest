import socket


class Server:

    def __init__(self):
        self.db = []


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    SERVER_IP, PORT = "localhost", 8000

    s.bind((SERVER_IP, PORT))
    s.listen(100)

    conn, addr = s.accept()

    with conn:

        print(f"connected by {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            conn.sendall(data)


if __name__ == "__main__":
    pass