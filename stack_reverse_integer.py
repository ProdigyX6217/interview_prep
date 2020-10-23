#!Write a function that will reverse a integer using a stack return the reversed number as an integer

st = []; 
  
# Function to push digits to stack 
def push_digits(number): 
  
    while (number != 0):  
        st.append(number % 10); 
        number = int(number / 10); 
  
# Function to reverse number 
def reverse_number(number): 
      
    # Function call to push number's digits to stack 
    push_digits(number); 
      
    reverse = 0; 
    i = 1; 
      
    # Popping digits and forming reversed number 
    while (len(st) > 0):  
        reverse = reverse + (st[len(st) - 1] * i); 
        st.pop(); 
        i = i * 10; 
      
    # Return reversed number  
    return reverse; 
  
# Driver Code 
number = 3479; 
  
# Function call to reverse number 
print(reverse_number(number)); 