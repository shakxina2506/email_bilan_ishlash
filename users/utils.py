from  random import randint

def generate_activation_code():
    return randint(1000, 9999)


print(generate_activation_code())