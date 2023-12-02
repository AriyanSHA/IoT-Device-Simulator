class Dashboard:
    def display_data(self, data):
        print("Time                   SensorData")
        print("---------------------------------")
        for timestamp, value in data:
            print(f"{timestamp}       {value:.2f}")


    def display_analytics(self, data):
        #print(analytics)
        average, minimum, maximum = data
        print("--------------------------------")
        print(f"Average: {average:.2f}")
        print(f"Minimum: {minimum[1]:.2f}")
        print(f"Maximum: {maximum[1]:.2f}")
