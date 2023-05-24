def fibonacciSeries(term):
    if term == 0:
        return 0
    elif term == 1:
        return 1
    first_term= 0
    second_term = 1
    for i in range(term):
        print(first_term)
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
fibonacciSeries(5)        

