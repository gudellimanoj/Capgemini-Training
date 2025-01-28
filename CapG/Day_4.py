# def get_input():
#     n=int(input("enter the size of the arr: "))
#     arr=[]
#     for i in range(n):
#         arr.append(input("Enter the element : "))
#     return arr
# def main():
#     arr=get_input()
#     print(arr)
# main()

# L1[]
# print("1. An array list:", L1)
# L2 = [0,1,2,3]

# print("2. An array list:", L2)
# L3=['abc', ['def', 'ghi']]
# print("3. An array list:", L3)
# L4=list('spam')
# print("4. List created from string'spam':", L4)
# L5=list(range(-4,4))
# print("5. List created from range(-4,4):", L5)
# L6=[10,20,30,40]
# print("6. element at index 2 of L6:", L6[2])
# L7=['x',[10,20,30], 'y']
# print("7. element at L7[1][2](nested list):", L7[1][2])
# L8=[0,1,2,3,4,5]
# print("8. Slicing L8[1:3]:", L8[2:5])
# print("9. Length of L8:", len(L8))

# #demonstrating nested indexing ans slicing together
# L9=[10,[100,200,300,400],50]
# print("10. Elment at L9[1]:", L9[1])
# print("10a. Element at L9[1]:", L9[1])
# print("10b. Element at L9[1][3]:", L9[1][3])
# print("10c. Sliceing sublist L9[1][3][1:3]:", L9[1][1:3])

# #summary of output

# print("L1:", L1)
# print("L2:", L2)
# print("L3:", L3)
# print("L4:", L4)
# print("L5:", L5)
# print("L6:", L6)
# print("L7:", L7)
# print("L8:", L8)
# print("L9:", L9)

# def sum_of_list(L):
#     sum=0
#     for i in L:
#         sum+=i
#     return sum
# L=[1,2,3,4,5]
# print("Sum of list L:", sum_of_list(L))

# finding the maximum  and min element in the list without using max() and min() functions
# def max_of_list(L):
#     max=L[0]
#     for i in L:
#         if i>max:
#             max=i
#     return max
# def min_of_list(L):
#     min=L[0]
#     for i in L:
#         if i<min:
#             min=i
#     return min
# L=[1,2,3,4,5]
# print("Maximum element in the list L:", max_of_list(L))
# print("Minimum element in the list L:", min_of_list(L))

# def max_min_of_list(L):
#     L.sort()
#     return L[0], L[-1]
# L=[1,2,3,4,5]
# print("Maximum and minimum element in the list L:", max_min_of_list(L))
# print("max",L[4])
# print("min",L[0])

# finding prime numbers in a given range and Also finding the maximum and minimum element in the list of prime numbers
# def prime_or_not(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1): 
#         if n % i == 0:
#             return False
#     return True  
# def max_min_of_list(L):
#     max_value = L[0]
#     min_value = L[0]
#     for i in L:
#         if i > max_value:
#             max_value = i
#         if i < min_value:
#             min_value = i
#     return min_value, max_value

# def prime_numbers_in_range():
#     start = int(input("Enter the starting range: "))
#     end = int(input("Enter the ending range: "))
#     prime_numbers = []
#     for i in range(start, end + 1):
#         if prime_or_not(i):
#             prime_numbers.append(i)
#     return prime_numbers

# L = prime_numbers_in_range()
# print("List of prime numbers:", L)
# max_value, min_value = max_min_of_list(L)
# print("Minimum and maximum element in the list of prime numbers:", max_value, min_value)


# palindrome or not using list
# def palindrome_or_not(s):
#     L = list(s)
#     if L == L[::-1]:
#         return True
#     return False
# s = input("Enter the string: ")
# print("Palindrome or not:", palindrome_or_not(s))

# code to remove the spaces in the string avoiding the spaces more than one without using the split() function

def remove_spaces(s):
    L = list(s)
    i = 0
    while i < len(L):
        if L[i] == ' ' and L[i + 1] == ' ':
            L.pop(i)
        else:
            i += 1
    return ''.join(L)
s = input("Enter the string: ")
print("String after removing extra spaces:", remove_spaces(s))
def palindrome_or_not(s):
    L = list(s)
    if L == L[::-1]:
        return True
    return False
print("Palindrome or not:", palindrome_or_not(s))




