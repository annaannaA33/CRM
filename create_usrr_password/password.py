import bcrypt

def main():
    password = 'apassword'.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)

    # Преобразуем хешированный пароль из байтов в строку, чтобы его можно было записать в CSV-файл
    hashed_password_str = hashed_password.decode('utf-8')


    print(hashed_password_str)

main()
 