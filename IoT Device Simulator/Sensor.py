import random
from datetime import datetime
class Sensor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def read_data(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return (now, random.uniform(self.min_value, self.max_value))