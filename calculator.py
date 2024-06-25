import sys

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        print("Pipe test")
        sys.exit(1)

    result = multiply(num1, num2)
    print(f"The result of multiplying {num1} by {num2} is {result}")
