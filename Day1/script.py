import sys
import requests


print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

name = input("Your name? ")
print("Hello ,",name)