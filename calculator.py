from addition import add
if __name__=="__main__":
    expresion=input("Enter expression:")
    if '+' in expresion:
        e=expresion.split('+')
        print(add(int(e[0]),int(e[1])))
