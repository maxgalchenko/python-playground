def categorize_ratings(ratings):
    low = [x for x in ratings if 1 <= x <= 4]
    medium = [x for x in ratings if 5 <= x <= 7]
    high = [x for x in ratings if 8 <= x <= 10]
    print(f"Low: {len(low)}")
    print(f"Medium: {len(medium)}")
    print(f"High: {len(high)}")
    pass


# Checking your results 
# Calling categorize_ratings([1, 3, 5, 7, 8, 9])
categorize_ratings([1, 3, 5, 7, 8, 9])
print("Expected Output:\nLow: 2\nMedium: 2\nHigh: 2")