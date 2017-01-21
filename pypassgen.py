import random, string

def generate_password(length, caps=True, numbers=True, symbols=True):
    """
    Secure random password generator
    """
    num_of_nmbrs = random.randint((length)//10, (length)//4) if numbers else 0
    num_of_symbs = random.randint((length)//10, (length)//4) if symbols else 0
    num_of_chars = length - num_of_nmbrs - num_of_symbs

    passwd = []
    chars = string.ascii_lowercase
    if caps:
        chars += string.ascii_uppercase
    for i in range(num_of_chars):
        passwd.append(random.choice(chars))
    if numbers:
        for i in range(num_of_nmbrs):
            passwd.append(random.choice(string.digits))
    if symbols:
        for i in range(num_of_symbs):
            passwd.append(random.choice(string.punctuation))
    
    random.shuffle(passwd)
    return ''.join(passwd)