def soe(n):
    # creates a boolean array of 0...n to sieve thru
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # if prime[p] is not changed, it remains True => prime
        if prime[p] == True:
            # updates all mutliples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p += 1
    prime[0] = False
    prime[1] = False
    # print all primes
    for p in range(n + 1):
        if prime[p]:
            print(p)


# driver program
if __name__ == "__main__":
    n = 16
    print("the following are <= to ", n)
    soe(n)
