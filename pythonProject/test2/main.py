import getpass
#print(getpass.getuser())
def whoami():
    print('your name is')
    print(getpass.getuser())
    print(getpass.getuser().lower())
    print(getpass.getuser().title())
whoami()
whoami()

whoami()