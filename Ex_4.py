"""Exercise 5: Create a Python set such that it shows the element from both lists in a pair

Given:"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]


def ex_4(first_list, second_list):
    print("First List :", first_list)
    print("Second List :", second_list)
    result = zip(first_list, second_list)
    result = set(result)
    print("Result Set :", result)


if __name__ == "__main__":
    ex_4(first_list, second_list)
