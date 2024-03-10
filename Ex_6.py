"""Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set"""

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

def ex_6(first_set,second_set):
    print(f"First Set : {first_set}\nSecond Set : {second_set}")
    temp = first_set.intersection(second_set)
    for x in temp:
        first_set.remove(x)
    return first_set

if __name__ == "__main__":
    print(ex_6(first_set,second_set))
