import hashlib
password = 'Welcome to the de-y"s personal CDN' + input("password") + 'aviance SALT.'
password = hashlib.sha3_512(password.encode()).hexdigest()
print(password)