# Goudi Dwaish
# COT4500-23Spring 0001
# JAN 25, 2023
# Assignment 1
# Professor Juna Parra

binary = "010000000111111010111001"

#convert to decimal from binary
decimal = int(binary,2)
print("{:.5f}".format(decimal))
print("\n")

# Three-digit chopping
print('%.3f'% decimal)
print("\n")

# Three-digit rounding
print(round(decimal,3))
print("\n")

#Absolute error and Relative error
rounded_value=round(decimal,3)
absolute_error=decimal-rounded_value
relative_error=(absolute_error/decimal)*100
print("Absolute error:",absolute_error)    
print("Relative error:",relative_error)   
