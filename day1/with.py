with open("yesterday",'r',encoding = 'utf-8') as f:
    print(type(f))
    for line in f:
        print(line.strip())