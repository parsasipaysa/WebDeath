import os

os.system("pip3 install colorama")
os.system("pip3 install pyfiglet")

try:
    import colorama
except:
    print()
    print("not installed colorama!")
    print("please install colorama")

try:
    import pyfiglet
except:
    print()
    print("not installed pyfiglet!")
    print("please install pyfiglet")
