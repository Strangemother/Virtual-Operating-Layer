
# Python3 implementation of the approach

# Function that prints
# the required sequence
def split(x, n):
    r = ()
    # If we cannot split the
    # number into exactly 'N' parts
    if(x < n):
        return (-1, )

    # If x % n == 0 then the minimum
    # difference is 0 and all
    # numbers are x / n
    if (x % n == 0):
        for i in range(n):
            # print(x//n, end =" ")
            r += (x//n,)
        return r

    # upto n-(x % n) the values
    # will be x / n
    # after that the values
    # will be x / n + 1
    zp = n - (x % n)
    pp = x//n
    for i in range(n):
        v = pp + (i>= zp)
        #print(v, end =" ")
        r += (v, )
    return r


def one(x, n=5):
    v = split(x, n)
    # print(v)
    print('--')
    g=sum(v)
    print('match',g==x)
    print('     ', g)
    print('     ', x)
    return v


# Driver code
x = 93430982389043283094223129837119286304923220987311982730294230942392234903290484363469876
n = 10_000


def print_res(r, x2):
    print('--')
    print(' O Bits:  ', len(str(x2)))
    print(' N Bits:  ', len(str(r[1])))
    print('  parts:  ', len(r))
    print('  item #0:', r[0])

v2 = x*x
r = one(v2, n)
