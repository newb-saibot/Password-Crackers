import string
import subprocess
all = list(string.ascii_letters + string.digits)
password = ""
found = False

while not found:
    for char in all:
        command = f"echo '{password}{character}*' | # place your command here"
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        if "Password confirmed!" in output:
            password += character
            print(password)
            break
        else:
            found = True