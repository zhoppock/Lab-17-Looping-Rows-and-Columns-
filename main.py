# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down. 
# Input:  None
# Output: Prints the letter E.

NUM_ACROSS = 3 # Number of asterisks to print across
NUM_DOWN = 5 # Number of asterisks to print down

# Write a loop to control the number of rows.
while NUM_DOWN > 0:
    # Write a loop to control the number of columns
          # Decide when to print an asterisk in every column.
  if NUM_DOWN == (5) or NUM_DOWN == (3) or NUM_DOWN == (1):
    print("geeks", end =" ") 
    print("geeksforgeeks") 
        # Decide when to print asterisk in column 1.  
  elif NUM_DOWN == (4) or NUM_DOWN == (2):
    print("*")
        # Decide when to print a space instead of an asterisk.   
        
        # Figure out where to place this statement that prints a newline.
  NUM_DOWN -= 1  
