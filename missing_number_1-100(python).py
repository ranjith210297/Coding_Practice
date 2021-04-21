# Python program to find missing number from 1 to 100.

arr = [1,2,3,4,6,7,8,9]
n = len(arr)

#sum of n natural numbers formula
summ = ((n+1)*(n+2))//2

print(summ-sum(arr))

