def analyze_numbers(numbers):
    if not numbers:
        return None

    total = sum(numbers)

    return {
        "count": len(numbers),
        "sum": total,
        "average": total / len(numbers),
        "maximum": max(numbers),
        "minimum": min(numbers),
        "range": max(numbers) - min(numbers)
    }


def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


def get_odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]


def find_number(numbers, target):
    if target in numbers:
        return numbers.index(target)
    return -1


def display_statistics(numbers):
    result = analyze_numbers(numbers)

    if result is None:
        print("No numbers available.")
        return

    print("\n--- Statistics ---")
    print(f"Count   : {result['count']}")
    print(f"Sum     : {result['sum']}")
    print(f"Average : {result['average']:.2f}")
    print(f"Maximum : {result['maximum']}")
    print(f"Minimum : {result['minimum']}")
    print(f"Range   : {result['range']}")


def display_numbers(numbers):
    print("\nNumbers:", numbers)
    print("Sorted :", sorted(numbers))
    print("Even   :", get_even_numbers(numbers))
    print("Odd    :", get_odd_numbers(numbers))


def add_numbers(numbers):
    try:
        value = float(input("Enter a number: "))

        if value.is_integer():
            value = int(value)

        numbers.append(value)
        print(f"{value} added successfully.")

    except ValueError:
        print("Invalid input.")


def search_number(numbers):
    try:
        target = float(input("Enter number to search: "))

        if target.is_integer():
            target = int(target)

        position = find_number(numbers, target)

        if position == -1:
            print(f"{target} was not found.")
        else:
            print(f"{target} found at index {position}.")

    except ValueError:
        print("Invalid input.")


def main():
    numbers = [10, 20, 15, 30, 25]

    while True:
        print("\n========== NUMBER ANALYZER ==========")
        print("1. Display numbers")
        print("2. Display statistics")
        print("3. Add number")
        print("4. Search number")
        print("5. Sort numbers")
        print("6. Remove number")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_numbers(numbers)

        elif choice == "2":
            display_statistics(numbers)

        elif choice == "3":
            add_numbers(numbers)

        elif choice == "4":
            search_number(numbers)

        elif choice == "5":
            numbers.sort()
            print("Numbers sorted successfully.")

        elif choice == "6":
            try:
                value = float(input("Enter number to remove: "))

                if value.is_integer():
                    value = int(value)

                if value in numbers:
                    numbers.remove(value)
                    print(f"{value} removed.")
                else:
                    print("Number not found.")

            except ValueError:
                print("Invalid input.")

        elif choice == "7":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()