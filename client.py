import socket
import sys

def start_client():
    print("Digit Sum Client Started")
    
    server_ip = input("Server IP >> ")
    server_port = int(input("Server Port >> "))
    starting_string = input("Digit Sum starting string >> ")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((server_ip, server_port))
        current_string = starting_string
        
        while True:
            client_socket.send(current_string.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            
            if response == "ERROR":
                print("\nServer returned error, Exiting Client Application")
                break
                
            print(f"Received Digit Sum result: {response}")
            
            if len(response) == 1:
                print("\nServer returned a single digit result, Exiting Client Application")
                break
                
            print(f"Sending {response} to Digit Sum Server")
            current_string = response

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
