"""Exercise 2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:"""

list1 = [54, 44, 27, 79, 91, 41]


def ex_2(l1):
    print("Actual List :\n",l1)
    print("Removing the element from index - 4")
    popped_element = l1.pop(4)
    print("Popped Element : ",popped_element)
    print(l1)
    print("Adding the element to 2nd possition")
    l1.insert(2,popped_element)
    print(l1)
    print("Adding the element to Last possition")
    l1.append(popped_element)
    print(l1)




if __name__ == "__main__":
    ex_2(list1)
