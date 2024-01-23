import sys
import pandas

class DataSet:
    def __init__(self, num_list: [float]) -> None:
        self.series = pandas.Series(data=num_list, dtype='float',name="Input List", copy=True)
        self.input_list = num_list

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
        return f'In.  Val. \n{self.series.to_string(float_format=True)}'
    
    def __repr__(self) -> str:
        return f'{self.input_list}'


def read_input(filename: str) -> [float]:
    with open(filename, 'r', encoding='utf-8') as input_file:
        read_text = input_file.read().replace("\n", " ")
        read_list = read_text.split(" ")
        read_list = [float(x) for x in read_list]
    input_series = pandas.Series(read_list)
    return input_series


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
        if u_input == "basic" or u_input == "b":
            print(data.basic())
        elif u_input == "advanced" or u_input == "a":
            print(data.advanced())
        elif u_input == "str" or u_input == "s":
            print(data)
        else:
            break

main()