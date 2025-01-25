import re

def alphanumeric_sort(input_str):
    # Extract numbers and treat them as integers
    numbers = sorted(re.findall(r'\d+', input_str), key=int)

    # Extract lowercase, uppercase, and other characters
    lower_chars = sorted(filter(str.islower, input_str))
    upper_chars = sorted(filter(str.isupper, input_str))
    others = sorted(filter(lambda x: not x.isalnum(), input_str))

    # Combine the sorted components
    result = ''.join(numbers) + ''.join(lower_chars) + ''.join(upper_chars) + ''.join(others)
    return result


if __name__ == "__main__":
    input_str = input("Enter a string to sort: ")
    print(f"Sorted string: {alphanumeric_sort(input_str)}")
