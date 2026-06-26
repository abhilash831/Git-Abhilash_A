#input list
numbers=list(map(int,input("Enter the numbers into list : ").split()))
#filter for multiple of 7
multiple_of_seven=filter(lambda x: x%7==0 ,numbers)
print(list(multiple_of_seven))