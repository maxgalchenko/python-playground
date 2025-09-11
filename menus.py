def display_name():
    return 3


def quicksort(cards):
    if len(cards) < 2:
        return cards  # Base case: Already sorted if 0 or 1 element
    else:
        pivot = cards[0]  # Choose first card as pivot
        less = [i for i in cards[1:] if i <= pivot]

        greater = [i for i in cards[1:] if i > pivot]
        print(greater, quicksort(greater))

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 2, 5, 8, 91, 2, 34, 6, 324, 324, 6, 1, 5, 67]))
