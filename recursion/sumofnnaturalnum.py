def sum_natural(n):
    if n==0:
        return 0 # returning 0 to cal sum.
    return sum_natural(n - 1) + n

sum=sum_natural(5)
print(sum)