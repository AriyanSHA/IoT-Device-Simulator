import statistics

class DataProcessor:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_average(data):
        if not data:
            raise ValueError("Input data is empty.")
        sum = 0
        count = 0
        for i in data:
            sum = sum + i[1]
            count = count + 1
            
        return sum/count

    @staticmethod
    def get_maximum(data):
        if not data:
            raise ValueError("Input data is empty.")
        mymax = (0, -999.9)
        for i in data:
            if i[1] > mymax[1]:
                mymax = i
        return mymax
        #return max(data)

    @staticmethod
    def get_minimum(data):
        if not data:
            raise ValueError("Input data is empty.")
        mymin = (0, +999.9)
        for i in data:
            if i[1] < mymin[1]:
                mymin = i
        return mymin
        #return min(data)