from addition import add
from substraction import subtract
from multiplication import multiply
from division import division
from modulus import modulus
from intdivision import intdivision
if __name__=="__main__":
    expresion=input("Enter expression:")
    if '+' in expresion:
        e=expresion.split('+')
        print(add(int(e[0]),int(e[1])))
    elif '-' in expresion:
        e=expresion.split('-')
        print(subtract(int(e[0]),int(e[1])))
    elif '*' in expresion:
        e=expresion.split('*')
        print(multiply(int(e[0]),int(e[1])))
    elif '//' in expresion:
        e=expresion.split('//')
        print(intdivision(int(e[0]),int(e[1])))
    elif '%' in expresion:
        e=expresion.split('%')
        print(modulus(int(e[0]),int(e[1])))
    elif '/' in expresion:
        e=expresion.split('/')
        print(division(int(e[0]),int(e[1])))
