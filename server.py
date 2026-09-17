import socket

def calculate_digit_sum(numeric_string):
    """Calculates the sum of all digits in a string."""
    return str(sum(int(digit) for digit in numeric_string))

def start_server():
    # Correct indentation inside the function
    HOST = '127.0.0.1'  
    PORT = 5555        

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        
        print("Digit Sum Server Started")
        print(f"Listening on TCP {PORT}")
        
        client_socket, client_address = server_socket.accept()
        
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
                
            print(f"Received string �{data}�")
            
            if not data.isdigit():
                print("\nInvalid Input, Exiting Server Application")
                client_socket.send("ERROR".encode('utf-8'))
                break
            
            result = calculate_digit_sum(data)
            print(f"Sending Digit Sum result: {result}")
            client_socket.send(result.encode('utf-8'))
            
            if len(result) == 1:
                print("\nDigit sum is a single digit, Exiting Server Application")
                break
                
        client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
