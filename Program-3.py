num = int(input("Enter the number:\n"))
for i in range(num):
    if num%2==0:
        num = num-1;

        res = 2*i +1

        print(res)



"""Output: (examples)
1) if a = 1, then output : 1
2) if a = 2, then output : 1
3) if a = 3, then output : 1, 3, 5
4) if a = 4, then output : 1, 3, 5
5) if a = 5, then output : 1, 3, 5, 7, 9
6) if a = 6, then output : 1, 3, 5, 7, 9"""