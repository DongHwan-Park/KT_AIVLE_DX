for i in range(10):
    globals()['s{}'.format(i)] = i
    
print(s1)
print(s2)