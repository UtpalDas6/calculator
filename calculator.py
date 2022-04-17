from addition import add
from substraction import subtract
if __name__=="__main__":
    expresion=input("Enter expression:")
    if '+' in expresion:
        e=expresion.split('+')
        print(add(int(e[0]),int(e[1])))
    if '-' in expresion:
        e=expresion.split('-')
        print(subtract(int(e[0]),int(e[1])))
