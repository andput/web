print 'press \'q\' to exit'
while 1:
    try:
        i = raw_input('Please enter a year: ')
        if i == 'q':
            break
        i = int(i)
        if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0):
            print u'vysokosnyi'
        else:
            print u'ne vysokosnyi'
    except(ValueError):
        print "Please, enter a number or \'q\' to exit"
    except Exception, err:
        print "Unexpected error:", err
