d = {'key1':1,'key2':2,'key3':3}
for k in d:
    print(k)
print(list(d))
print(type(list(d)))
while(1):
    print('*******DICTIONARY ITERATION*******')
    print('1.Through dictionary keys()')
    print('2.Through dictonary values()')
    print('3.Through dicionary items()')
    print('4.Exit')
    c = int(input('Enter your choice:'))
    if(c==1):
        for k in d.keys():
            print(k)
        print(d.keys())
        print(type(d.keys()))
        print(list(d.keys()))
        print(type(list(d.keys())))
    elif(c==2):
        for v in d.values():
            print(v)
        print(d.values())
        print(type(d.values()))
    elif(c==3):
        for k, v in d.items():
            print('keys=',k,'Values=',v)
        print(d.items())
        print(type(d.items()))
    elif(c==4):
        break;
