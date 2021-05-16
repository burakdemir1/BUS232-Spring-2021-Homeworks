def fakePrimes():
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    for i in range(len(primes)-1):
        fakePrime=primes[i]*primes[i+1]
        print(f'Fake prime in position {i+1} is {fakePrime}. It is generated using {primes[i]} and {primes[i+1]}.')
fakePrimes()