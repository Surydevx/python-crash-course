# okay assume that this code is a 6 digit password-keepper adn wants you to find the passsword.

main_password = [1, 2, 3, 4, 5, 6]
print("you have three attempts at entering the password")
counter = 3


def get_digit_by_position(number: int, position: int) -> int:
    """
    Returns the digit at a specific position of a non-negative integer.
    Position is 1-indexed from right to left (1 = ones place, 2 = tens place, etc.)
    """
    # Strictly enforce that inputs are integers
    if type(number) is not int or type(position) is not int:
        raise TypeError("Both 'number' and 'position' must be strictly integers.")

    # Enforce non-negative number and valid position
    if number < 0:
        raise ValueError("The number must be non-negative.")
    if position <= 0:
        raise ValueError("Position must be a positive integer starting from 1.")

    # Graceful handling: If the position requested is longer than the number of digits
    # 10 ** (position - 1) gives the minimum value for that position (e.g., pos 3 needs at least 100)
    if number < 10 ** (position - 1):
        print(f"Warning: Position {position} exceeds the length of the number.")
        return 0

    # Pure math approach to extract the digit
    return (number // 10 ** (position - 1)) % 10


while counter > 0:
    e_p = int(input("please enter your passsword"))
    pass_length = len(str(e_p))
    if pass_length == 6:
        hardened_pass = [get_digit_by_position(e_p, 6),get_digit_by_position(e_p, 5),get_digit_by_position(e_p, 4),get_digit_by_position(e_p, 3),get_digit_by_position(e_p, 2),get_digit_by_position(e_p, 1)]
        if hardened_pass == main_password:
            print("your password is correct!")
            break
        else:
            print("password is incorrect, go away!")
        counter -= 1
    else:
        print("your password is incorrect, go away!")
        counter -= 1 