# Prog08: Print how many are odd numbers
numbers = [float(input(f'Enter number {i+1}: ')) for i in range(10)]
odd_count = sum(1 for num in numbers if num % 2 != 0)
print(f'Number of odd numbers: {odd_count}')
