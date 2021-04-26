def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Kenny", "lastname": "Miranda"}

    super_list = [
        {"firstname": "Kenny", "lastname": "Miranda"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "García"}
    ]
    
    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}', end="")

if __name__ == '__main__':
    main()
    