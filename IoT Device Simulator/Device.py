class Device:
    def __init__(self, sensor, data_processor, communication):
        self.sensor = sensor
        self.data_processor = data_processor
        self.communication = communication
        self.data = []
        

    def collect_data(self, num_samples):
        try:
            for _ in range(num_samples):
                self.data.append(self.sensor.read_data())
        except Exception as e:
            print(f"Error collecting data: {e}")

    def process_data(self):
        try:
            #print(self.data)
            average = self.data_processor.get_average(self.data)
            minimum = self.data_processor.get_minimum(self.data)
            maximum = self.data_processor.get_maximum(self.data)
            #print(f"Average: {average}, Minimum: {minimum}, Maximum: {maximum}")
            return average, minimum, maximum
        except Exception as e:
            print(f"Error processing data: {e}")

    def send_data_to_server(self, processed_data):
        try:
            self.communication.send_data(processed_data)
        except Exception as e:
            print(f"Error sending data to server: {e}")

    def receive_data_from_server(self):
        try:
            self.communication.receive_data()
        except Exception as e:
            print(f"Error receiving data from server: {e}")