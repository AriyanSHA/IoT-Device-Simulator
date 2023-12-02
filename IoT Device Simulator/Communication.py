class Communication: #Creating Class Communication
    def __init__(self, server_url): #Creating a constructor with server_url parameter
        self.server_url = server_url

    def send_data(self, data): #Showing user we are sending input
        print(f"\nSending data BELOW to {self.server_url}: ")
        print(data, "\n")

    def receive_data(self): #Showing user we are receiving output
        print(f"Receiving data from {self.server_url}\n")