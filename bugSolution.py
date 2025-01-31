def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage demonstrating the fix
data = []
print(calculate_average(data))  # Output: 0
data = [10, 20, 30]
print(calculate_average(data))  # Output: 20.0