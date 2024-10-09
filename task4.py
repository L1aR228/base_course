n = int(input())
summ1 = 1
summ2 = 1
print(summ2, end=' ')
for i in range(n):

    print(summ2, end=' ')
    summ1, summ2 = summ2, summ1 + summ2
    
    
