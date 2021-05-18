def isPrimenumber(number):
    isPrime = True
    if number > 1:
        for k in range(2, number):
            if (number % k) == 0:
                isPrime = False
                break
    return isPrime

def first20Prime():
    primeNumbers = []
    b = 0
    for k in range(2,99):
        if(b == 20):
            break
        if isPrimenumber(k):
            b = b + 1
            primeNumbers.append(k)
    print("First 20 Prime Numbers: ",primeNumbers)
    return primeNumbers

def first19FakePrime(c):
    fakePrimeNumbers = []
    for k in range(1,20):
        fakePrimeNumber = c[k]*c[k-1]
        fakePrimeNumbers.append(fakePrimeNumber)
    print("First (Fake) 19 Prime Numbers: ",fakePrimeNumbers)
    return fakePrimeNumbers

first19FakePrime(first20Prime())