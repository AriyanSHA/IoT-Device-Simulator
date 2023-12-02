from Sensor import Sensor
from DataProcessor import DataProcessor
from Communication import Communication
from Device import Device
from Dashboard import Dashboard

def main():
    temperature_sensor = Sensor(0, 100)
    data_processor = DataProcessor(temperature_sensor)
    communication = Communication("https://central-server.example.com")

    device = Device(temperature_sensor, data_processor, communication)

    dashboard = Dashboard()

    device.collect_data(100)
    processed_data = device.process_data()

    device.send_data_to_server(processed_data)
    device.receive_data_from_server()
    dashboard.display_data(device.data)
    dashboard.display_analytics(processed_data)


if __name__ == "__main__": # why this line is needed? It checks whether the current script is being executed as the main program or if it is being imported as a module into another program.
    main()
