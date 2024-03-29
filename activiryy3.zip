import csv

def load_data():
    """
    Function to load data from a CSV file.
    """
    while True:
        csv_file = input("stage 1: load data\n enter the path to your CSV file (or 'exit' to quit): ")
        if csv_file.lower() == 'exit':
            print("exiting the program.")
            return None
        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                data = [row for row in csv_reader]
            return data
        except FileNotFoundError:
            print("file not found. enter correct name.")

def prepare_data(data):
    """
    Function to prepare the loaded data.
    """
    column_choice = input("stage 2: prepare data\nplease choose column: ")
    while column_choice not in ['1', '2', '3', '4']:
        column_choice = input("wrong input, try again: ")
    return data

def analyze_data(data):
    """
    Function to analyze the prepared data.
    """
    sort_choice = input("stage 3: Analyse data\n enter 1 for ascending or 2 for descending order: ")
    pass

def visualize_data(data):
    """
    Function to visualize the analyzed data.
    """
    print("stage 4: visualise data")
    print("column: Units sold")
    print("legend: each '*' represents 5 units")
    for row in data:
        if row[0] != 'Units sold':
            print("*" * int(float(row[-1]) / 5))
    print("Visualisation completed")


def main():
    """
    Main function to orchestrate the CLI
    """
    print("---------------------------------")
    print("Welcome to Data Analysis CLI")
    print("---------------------------------")
    print("Program stages:")
    print("1. Load Data")
    print("2. Clean and prepare data")
    print("3. Analyse Data")
    print("4. Visualize Data")

    data = load_data()
    if data:
        prepare_data(data)
        analyze_data(data)
        visualize_data(data)
        print("Thank you")

if __name__ == "__main__":
    main()
