def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def main():
    num = input('Ingresa un número: ')
    
    is_a_number = True if num.isnumeric() else False
    is_positive = True if int(num) > 0 else False
    
    assert is_positive, "Debes ingresar números naturales... " 
    assert is_a_number, "Debes ingresar un número..."
    
    print(divisors(int(num)))
    print('Terminó mi programa ...')
    
if __name__ == '__main__':
    main()
    