def squares_nums():
    nums = [x**2 for x in range(101) if x%3!=0]
    return nums

def reto():
    nums = [x for x in range(1,100000) if x%36 == 0]
    return nums

if __name__ == '__main__':
    out = reto()
    print(out)