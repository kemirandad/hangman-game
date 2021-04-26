def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def main():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError('Oops! ha ocurrido un error...')
            elif len(num) == 0:
                raise Exception('Oops! ha ocurrido un error...')
            print(divisors(num))
            print('Terminó mi programa ...')
            break
        except ValueError as ve:
            print('\nNot a number')
            print(ve)
        except Exception as e:
            print("\nDebes ingresar un número...")
            print(e)
    
if __name__ == '__main__':
    main()
    