def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    dp = [0]*n
    dp[0] = 1
    curr = 0
    for i in range(delay, n):
        if i-forget >= 0:
            curr -= dp[i-forget]

        curr += dp[i-delay]

        dp[i] = curr

    return sum(dp[n-forget:]) % (10**9+7)


print(peopleAwareOfSecret(6, 2, 4))
