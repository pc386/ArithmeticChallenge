import sys

sys.set_int_max_str_digits(5127919)

x = 3 * 5678193
 
result = 2 ** x
result = result - 1 

result = result // 7 
result_str = str(result)

# Write the result to a file
with open("result", "w") as file:
    file.write(result_str)
