import random, string

#string plano y digitos
def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    print(chars)
    return ''.join(random.choice(chars) for _ in range(size))