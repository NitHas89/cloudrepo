import os

print(os.getcwd())
print(os.listdir())
print(os.getenv('MY_ENV'))


for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
