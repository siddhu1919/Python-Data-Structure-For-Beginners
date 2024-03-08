"""Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

Given:"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_dictionary = {}



def ex_5(sample_list):
    print("Actual List : ", sample_list)
    for x in sample_list:
        if x in count_dictionary:
            count_dictionary[x] += 1
        else:
            count_dictionary[x] = 1
    print(count_dictionary)

if __name__ == "__main__":
    ex_5(sample_list)
