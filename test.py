test_performance = {
    "John": 87,
    "List": 90,
    "Mary": 75,
    "Chris": 100,
    "Linda": 100,
    "Matt": 70,
}

scores = list(test_performance.values())

print(scores)


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


sorted_scores = bubble_sort(scores)
print(sorted_scores)  # Output: [70, 75, 87, 90, 100, 100]

### YOUR CODE HERE ###
highest_score = max(sorted_scores)
lowest_score = min(sorted_scores)
print(lowest_score, highest_score)


def average_class_score(class_list, scores_list):
    try:
        if not class_list or not scores_list:
            raise ValueError("Class list or scores list is empty.")
        return sum(scores_list) / len(scores_list)
    except Exception as e:
        print(f"Error: {e}")
        return None
