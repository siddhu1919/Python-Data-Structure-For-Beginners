"""Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2."""

# Given
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


def ex_1(l1, l2):
    odd_elements = l1[1::2]
    even_elements = l2[0::2]
    l3 = []
    l3.extend(odd_elements)
    l3.extend(even_elements)
    return l3


if __name__ == "__main__":
    print(ex_1(l1, l2))
