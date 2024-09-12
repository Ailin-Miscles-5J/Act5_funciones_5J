print("Ejemplo de Funciones")
#declaradndo funciones
def hola():
    print("Alguien uso la funcion hola")
def chat(mensa):
    print(f"chat: {mensa}")
def ellacontesta(mensa):
    print(f"Chat ella: {mensa}")
def escribenombre(ap,n):
    print(f"Tu nomre completo es: {n} {ap}")
def suma(a,b):
    s=a+b
    return s
def resta(c,d):
    r=c-d
    return r
def multi(e,f):
    m=e*f
    return m
def div(g,h):
    d=g/h
    return d

# llamadas a funciones 
hola()
chat("Que bonita esta")
ellacontesta("graciass")
escribenombre("Ruvalcaba","Ailin")
print("Operacion suma")
c1=int(input("Ingres un numero:"))
c2=int(input("Ingrese otro numero:"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c3=int(input("Ingres un numero:"))
c4=int(input("Ingrese otro numero:"))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion multiplicacion")
c5=int(input("Ingres un numero:"))
c6=int(input("Ingrese otro numero:"))
damemulti=multi(c5,c6)
print(f"La multiplicacion de {c5} x {c6} = {damemulti}")

print("Operacion division")
c7=int(input("Ingres un numero:"))
c8=int(input("Ingrese otro numero:"))
damedivision=div(c7,c8)
print(f"La division de {c7} / {c8} = {damedivision}")