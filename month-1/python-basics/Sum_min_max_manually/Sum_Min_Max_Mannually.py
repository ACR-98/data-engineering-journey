#Does the Sum, min and max of a list without built in functions
def sum_max_min(numbers): #The parameter should be a list
    sum=0
    max=min=numbers[0] #We start with the first element
    for num in numbers: #Sums and compares every number to get the values.
        sum += num
        if num > max:
            max = num
        if num < min:
            min = num
    return sum, max, min
#Gets a valid list as input
def input_valid_list():
    while True: #Infinite bucle if not valid input
        user_input = input("Enter the numbers separated by a space: ").strip()
        #We get the input and clean it with strip
        if not user_input:
            print("Please input the numbers separated by a space")
            continue #If emtpy we go back to the beginning.

        try:
            #We convert the input to a list
            numbers = [float(num) for num in user_input.split()]
            #Verifies if numbers are int or float
            if all(isinstance(num, (int, float)) for num in numbers):
                return numbers
            else:
                print("Please input the numbers separated by a space")

        except ValueError:
            print("Please input only numbers separated by a space")

if __name__ == "__main__":
    numbers = input_valid_list()
    sum, max, min = sum_max_min(numbers)
    print(f"Suma: {sum} Min: {min} Max: {max}")