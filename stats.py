import sys
import pandas

class DataSet:
    def __init__(self, num_list: [float]) -> None:
        self.series = pandas.Series(data=num_list, dtype='float',name="Input List", copy=True)
        self.input_list = num_list

    # Missing values currently include the mode, variance


    
    def extra(self):
        answer = ""
    
    def advanced(self) -> str:
        return self.series.describe()

    def basic(self) -> str:
        """
        gets the count, Max, Min, Mean, and Median of the data

        Returns: str
        """
        answer = f"Amount: {self.series.count()}\nMax: {self.series.max()}\nMin: {self.series.min()}\nMean: {self.series.mean()}\nMedian: {self.series.median()}"
        return answer

    def __str__(self) -> str:
        return f'In.  Val. \n{self.series.to_string()}'
    
    def __repr__(self) -> str:
        return f'{self.input_list}'


def read_input(filename: str) -> [float]:
    with open(filename, 'r', encoding='utf-8') as input_file:
        read_text = input_file.read().replace("\n", " ")
        read_list = read_text.split(" ")
        read_list = [float(x) for x in read_list]
    input_series = pandas.Series(read_list)
    return input_series


def trigger_case(trigger: str, data: DataSet) -> int:
    match trigger:
        case "basic":
            print(data.basic())
            return 0
        case "b":
            print(data.basic())
            return 0
        case "advanced":
            print(data.advanced())
            return 0
        case "a":
            print(data.advanced())
            return 0
        case "string":
            print(data)
            return 0
        case "s":
            print(data)
            return 0
        case _:
            return -1


def main():
    if len(sys.argv) == 2:
        input_filename = sys.argv[1]
    elif len(sys.argv >= 3):
        print("Usage: stats.py <filename>")
        exit()
    else:
        input_filename = input("Filename? ").strip()
    if input_filename[0] == "\"":
        input_filename = input_filename[1:]
    if input_filename[-1] == "\"":
        input_filename = input_filename[:len(input_filename)]
    input_list = read_input(input_filename)
    data = DataSet(input_list)
    while True:
        u_input = input("Action? ")
        result = trigger_case(u_input, data)
        if result == -1:
            break

main()
