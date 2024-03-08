"""Exercise 3: Slice list into 3 equal chunks and reverse each chunk
Given:"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def ex_3(sample_list):
    chunk_size = int(len(sample_list) / 3)
    print("Actual List: ", sample_list)
    # Actual Logic of dividing the samle list into 3 equal parts
    start_pointer = 0
    end_pointer = chunk_size
    for x in range(3):
        chunks = sample_list[start_pointer:end_pointer]
        print(x + 1, "List", chunks)
        print("Reversed List ", chunks[::-1])
        start_pointer = end_pointer
        end_pointer += chunk_size


if __name__ == "__main__":
    ex_3(sample_list)
