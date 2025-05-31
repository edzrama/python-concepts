n = 1123581321  # Example input
#Given a positive input integer n, create a while loop that utilizes arithmetic to store the frequency of each digit present in n in a dictionary frequency_map. 
#The input number n will be provided as a numeric data type, not a string. 
#For each loop iteration, must update frequency_map before reducing n.
frequency_map = {}

while n > 0:
    digit = n % 10  # Get the last digit
    frequency_map[digit] = frequency_map.get(digit, 0) + 1
    n = n // 10  # Remove the last digit

print(frequency_map)