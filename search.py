# Get input from the user
main_string = input("Enter the main string: ")
search_string = input("Enter the string to search for: ")

# Search for the substring
position = main_string.find(search_string)

# Display result
if position != -1:
    print(f"'{search_string}' found at position {position}")
else:
    print(f"'{search_string}' not found in the main string.")
