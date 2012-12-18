
def humanizer(n, d):
    try:
        s = str(n)
        if n > 20:
            n = n % 10
        if n == 1:
            print s + ' ' + d[0]
        elif 1 < n and n < 5:
            print s + ' ' + d[1]
        else:
            print s + ' ' +  d[2]
    except(KeyError):
        print 'Dictionary is not full'
    except:
        print 'Bad input parameters'

d = ('chas', 'chasa', 'chasov')
for x in range(1, 101):
    humanizer(x, d)
