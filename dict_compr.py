def dict_comp():
    nums_dict = {i: i**3 for i in range(1,101) if i%3 != 0}
    for key, value in nums_dict.items():
        print(key,': ', value)

def reto():
    nums_dict = {i: round(i**0.5,2) for i in range(1,1001)}
    for key, value in nums_dict.items():
        print(key,': ', value)




if __name__ == '__main__':
    reto()
    
