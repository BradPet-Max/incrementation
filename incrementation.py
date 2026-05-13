
# 1.2 - Return the lowest and second lowest numbers in a list

def lowest_two(numbers):
    """
    Takes a list of numbers and returns a tuple (lowest, low) where:
        - lowest : the smallest number in the list
        - low    : the second smallest number in the list
    Returns None if the list has fewer than 2 elements.
    """
    if len(numbers) < 2:
        return None

    # Initialise lowest and second lowest using first two elements
    if numbers[0] < numbers[1]:
        lowest = numbers[0]
        low    = numbers[1]
    else:
        lowest = numbers[1]
        low    = numbers[0]

    # Walk through the rest of the list with a while loop
    i = 2
    while i < len(numbers):
        current = numbers[i]

        if current < lowest:
            low    = lowest      # old lowest becomes second lowest
            lowest = current     # new number becomes lowest
        elif current < low:
            low = current        # new number is second lowest only

        i += 1

    return (lowest, low)


# --- Example usage ---
print("1.2 - lowest_two()")

samples = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [10, 20, 30, 40, 50],
    [7, 7, 7, 7],
    [42, 13],
    [99],
]

for s in samples:
    print(f"  Input: {str(s):<35} -> {lowest_two(s)}")