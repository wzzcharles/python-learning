import random as rd

if __name__=='__main__':
    f=open(r'E:\work\python\test3\name.txt')
    name = f.read()
    name = name.split()
    name1 = [rd.choice(name) for i in range(100)]
    name2 = [rd.choice(name) for i in range(100)]
    name3 = set(name1) & set(name2)
    name4 = set(name1) ^ set(name2)
    name5 = set(name1) and set(name2)

    print(name3)
    print(name4)
    print(name5)