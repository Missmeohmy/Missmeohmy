#This code will show how to use perameters when defining a function#
def greet(lang):
    if lang == 'es':
        return('Hola')
    elif lang == 'fr':
        return('Bonjour')
    else:
        return('Hello')
print(greet('en') , 'Glenn')
print(greet('es') , 'Sally')
print(greet('fr') , 'Michael')
