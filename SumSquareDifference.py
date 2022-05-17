
sum_of_the_squares = 0
sum = 0

for i in range(1, 101):
    sum_of_the_squares += i*i
    sum += i

square_of_the_sum = sum*sum
difference = square_of_the_sum - sum_of_the_squares
print(difference)
