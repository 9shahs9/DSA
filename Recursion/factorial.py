def factorial (n):
    if n == 1: return 1
    return n* factorial(n-1)

print("="*40)
print(factorial(80))
print("="*40)