def read():
    numbers = list()
    file = "./archivos/numbers.txt"
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Maria", "Fernanda"]
    file = "./archivos/names.txt"
    with open(file, mode="a", encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write("\n")
    

def main():
    write()

if __name__ == '__main__':
    main()
    