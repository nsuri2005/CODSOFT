class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def run(self):
        print("Welcome to the calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            choice = input("Enter your choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                if choice == '1':
                    print(f"The result is: {self.add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {self.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {self.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {self.divide(num1, num2)}")
            else:
                print("Invalid choice. Please choose a valid operation.")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation != 'yes':
                print("Thank you for using the Python Calculator. Goodbye!")
                break

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
