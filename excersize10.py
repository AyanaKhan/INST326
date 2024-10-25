# Excersize10
# Ayana Khan (driver and navigatior)
def get_path():
    while True:
        file_path = input("Enter the file path: ")
        try:
            with open(file_path, "r") as file:
                return file_path
        except FileNotFoundError:
            print("Sorry, I couldn't find that file.")

def read_values(file_path):
    values = []
    with open(file_path, "r") as file:
        for line in file:
            label, number = line.strip().split(',')
            values.append((int(number), label))
    return values

def print_values(values):
    for number, label in values:
        print(f"{label}: {number}")

def main():
    file_path = get_path()
    values = read_values(file_path)
    values.sort(reverse=True)
    print_values(values)

if __name__ == "__main__":
    main()