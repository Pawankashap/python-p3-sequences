#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibonacci_list = []
    elif length==1:
        fibonacci_list=[0]
    else:
        fibonacci_list = [0, 1]  
        for i in range(2, length):
            next_fibonacci = fibonacci_list[i - 1] + fibonacci_list[i - 2]  
            fibonacci_list.append(next_fibonacci)  

    print(fibonacci_list)
    #pass