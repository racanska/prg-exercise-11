import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers.copy()
    length = len(numbers)

    for i in range(length):
        smallest = i
        start = smallest + 1

        for j in range(start,length):
            if numbers[j] < numbers[smallest]:
                smallest = j

        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

    return numbers

import matplotlib.pyplot as plt

def bubble_sort(numbers):
    numbers = numbers.copy()
    length = len(numbers)

    plt.ion()
    plt.show()

    for i in range(length):
        end = length - i - 1
        for j in range(0, end):

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    plt.ioff()
    plt.show()

    return numbers

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    short_num = [5, 1, 4, 2, 8]
    random_num = random_numbers(20)

    print(selection_sort(short_num))
    print(selection_sort(random_num))

    print(bubble_sort(short_num))