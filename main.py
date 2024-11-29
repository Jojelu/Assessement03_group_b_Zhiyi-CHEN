"""
Blackjack
"""


def calculate_score(x: int, y: int, z: int):
    sum = x + y + z
    list = [x, y, z]
    if sum <= 21:
        return sum
    elif 11 in list:
        sum -= 10
        if sum > 21:
            return "BUST"
        else:
            return sum
    else:
        return "BUST"



# Provide your solution here

"""
Even Numbers

"""


def even_positive_numbers(even_list: [int]):
    new_list = []
    for i in even_list:
        if i > 0 and i % 2 == 0:
            new_list.append(i)
    return new_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

    result = calculate_score(9,9,9)
    print(result)

    result = calculate_score(2,8,11)
    print(result)

    result = calculate_score(3,8,11)
    print(result)

    result = calculate_score(11,11,11)
    print(result)

    mylist_a = even_positive_numbers([1,2,3])
    print(mylist_a)

    mylist_b = even_positive_numbers([10, 22, 31, 24, 35, 36])
    print(mylist_b)

    mylist_c = even_positive_numbers([-10, -22, 31, 24, 35, 36])
    print(mylist_c)