from tkinter import *
from math import gcd

# GUI

root = Tk()
root.title("Rivest Shamir Adleman(RSA)")
root.geometry('400x380')
root.resizable(width=False, height=False)
color = '#20c997'
root.configure(bg=color)


def gen_random_prime_number():
    return 7, 19


p, q = gen_random_prime_number()


def gen_n():
    return p * q


n = gen_n()


def get_m():
    return (p - 1) * (q - 1)


m = get_m()


def gen_public_key():
    for e in range(2, 1000):
        check = gcd(e, m)
        if check == 1:
            return e


e = gen_public_key()


def gen_private_key():
    m = get_m()
    e = gen_public_key()

    for i in range(2, 1000):
        d = (1 + m * i) / 5
        if int(d) == d:
            return int(d)


d = gen_private_key()


def encode(message=None):
    """
        Retun the ascii string of given string.
    """
    return ord(message)


def decode(char=None):
    return chr(char)


def encrypt(message=None):
    if message is None:
        raise ValueError("Message shouldn't be None")

    cipher_char = []
    for char in message:
        encoded_char = encode(char)
        cipher = encoded_char ** gen_public_key() % gen_n()
        cipher_char.append(cipher)

    return ','.join(list(map(lambda char: str(char), cipher_char)))


def decrypt(cipher=None):
    if cipher is None:
        raise ValueError("Cipher shouldn't be None")

    plain_char = []
    cipher_list = cipher.split(',')

    for cipher_char in cipher_list:
        plain = decode(int(cipher_char) ** gen_private_key() % gen_n())
        plain_char.append(plain)
    return ''.join(plain_char)


def get_value_encrypt():
    msg = enter.get("1.0", 'end-1c')
    output.insert("1.0", encrypt(msg))


def get_value_decrypt():
    msg = output.get("1.0", 'end-1c')
    output1.insert("1.0", decrypt(msg))


def get_clear():
    enter.delete("1.0", END)
    output.delete("1.0", END)
    output1.delete("1.0", END)


label_heading = Label(root, text="Rivest Shamir Adleman(RSA)", bg='#17a2b8', fg='white', font=('Helvetica', 15, 'bold'))
label_heading.place(x=60, y=10)

label_entry = Label(root, text="Plain Text:", bg=color, font='Helvetica')
label_entry.place(x=40, y=60)

enter = Text(root, height=2, width=20)
enter.place(x=160, y=55)

label_output = Label(root, text="Encrypted Text:", bg=color, font='Helvetica')
label_output.place(x=40, y=140)

output = Text(root, height=2, width=20)
output.place(x=160, y=135)

label_output1 = Label(root, text="Decrypted Text:", bg=color, font='Helvetica')
label_output1.place(x=40, y=220)

output1 = Text(root, height=2, width=20)
output1.place(x=160, y=215)

button = Button(root, text="Encrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_encrypt(), width=10, height=2,
                font=('Arial',12,'bold'))
button.place(x=30, y=300)

button1 = Button(root, text="Decrypt", bg='#343a40',fg='#f9f9f9', command=lambda: get_value_decrypt(), width=10, height=2,
                 font=('Arial',12,'bold'))
button1.place(x=150, y=300)

button_clear = Button(root, text="Clear", bg='#343a40',fg='#f9f9f9', command=lambda: get_clear(), width=10, height=2, font=('Arial',12,'bold'))
button_clear.place(x=270, y=300)

root.mainloop()

