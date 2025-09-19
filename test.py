def send_discount(books_purchased, discount_threshold, bonus_threshold):
    if (books_purchased >= bonus_threshold): print('Big discount applied!')
    elif (books_purchased >= discount_threshold): print('Discount applied!')
    else: print('No discount.')
    pass

# Checking your results 
send_discount(3, 5)  # Should print No discount.
send_discount(7, 5)  # Should print Discount applied!