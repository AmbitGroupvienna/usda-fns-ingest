import argparse
import string
import secrets

def generate_secret(length):
    secret = ''
    choice = string.digits + string.ascii_letters + string.punctuation
    choice = choice.replace("'", "")
    choice = choice.replace('"', '')
    for i in range(length):
        secret += secrets.choice(choice)

    return secret

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate a secret key/password.  The string will include digits, letters, and punctuation, and has a default length of 50.")
    parser.add_argument("-l", "--length", help="Specify secret length", type=int, default=50)

    args = parser.parse_args()
    print(generate_secret(args.length))