import re

def alphanumeric_sort(input_string):
    # Separate numbers, lowercase, uppercase, and other characters
    numbers = re.findall(r'\d+', input_string)
    lowercase = [ch for ch in input_string if ch.islower()]
    uppercase = [ch for ch in input_string if ch.isupper()]
    others = [ch for ch in input_string if not ch.isalnum()]

    # Sort each group
    sorted_numbers = sorted(numbers, key=int)
    sorted_lowercase = sorted(lowercase)
    sorted_uppercase = sorted(uppercase)
    sorted_others = sorted(others)

    # Combine results
    result = ''.join(sorted_numbers + sorted_lowercase + sorted_uppercase + sorted_others)
    return result

if __name__ == "__main__":
    print("Welcome to the Alphanumeric Sorter!")
    while True:
        user_input = input("Enter a string to sort (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        sorted_result = alphanumeric_sort(user_input)
        print(f"Sorted Output: {sorted_result}")
