#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(num):
    count = 0
    x = [int(d) for d in str(num)]
    print(x)
    for n in x:
        if n == 1:
            count += 1
    return count

print(hammingWeight(1000001))