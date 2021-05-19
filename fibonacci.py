def fib(n):
    ans = [0, 1]
    for i in range(1, n-1):
        ans.append(ans[i] + ans[i-1])
    return ans

print(fib(6))



