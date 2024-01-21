def check_second_and_third_largest(lst):
    # Find the three largest numbers in the list
    sorted_numbers = sorted(set(lst), reverse=True)
    
    # Check if the second and third largest numbers are the same and no more copies exist, or if they are unique
    if len(sorted_numbers) >= 3 and ((sorted_numbers[1] == sorted_numbers[2] and lst.count(sorted_numbers[1]) == 1) or len(sorted_numbers) >= 4):
        return True  # Second and third largest numbers are either the same and unique or they are unique
    else:
        return False  # Second and third largest numbers are not meeting the conditions

# Example usage
my_list = [10, 5, 8, 15, 12, 12, 8, 20]
result = check_second_and_third_largest(my_list)

if result:
    print("The second and third largest numbers are either the same and unique or they are unique.")
else:
    print("The conditions are not met.")
