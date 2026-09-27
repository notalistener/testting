def analyze_numbers(numbers):
    if not numbers:
        return None

    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "maximum": max(numbers),
        "minimum": min(numbers)
    }


values = [10, 20, 15, 30, 25]

result = analyze_numbers(values)

for key, value in result.items():
    print(f"{key.capitalize()}: {value}")