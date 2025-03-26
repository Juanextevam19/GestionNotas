notas={}
usuarios=[]
#Funcionn de registro
def Registrar():
    print("Registro de Usuario")
    nombre = input("Ingrese su nombre")
    contraseña=input("Ingrese su contraseña")
    tipo = input("Tipo (estudiante/profesor):").lower()
    if tipo not in ["estudiante","profesor"]:
        print("Tipo de usuario invalido")
        return
    #Guardar usuario en la lista 
    usuarios.append({"nombre": nombre, "contraseña": contraseña, "tipo": tipo})
    if tipo == "estudiante":
        notas[nombre]={} #Crear una lista de notas para este usuario
    print("Usuario registrado con exito")


def iniciar_sesion():
    print("Inicio de sesion")
    nombre = input("Ingrese su nombre de usuario")
    contraseña=input("Ingrese su contraseña")
    for user in usuarios:
        if user["nombre"]==nombre and user["contraseña"]==contraseña:
            print("Sesion iniciada con exito")
            return user
    print("Usuario o contraseña incorrectos")
    return None

def agregar_nota():
    estudiante = input("Ingrese el nombre del estudiante")
    if estudiante in notas:
        materia = input("Ingrese la materia")
        nota = float(input("Ingrese la nota"))
        notas[estudiante].setdefault(materia, []).append(nota)
        print("Nota agregada con exito")
    else:
        print("Estudiante no encontrado")

def ver_notas():
    estudiante = input("Ingrese el nombre del estudiante")
    if estudiante in notas and notas[estudiante]:
        for materia, lista_notas in notas[estudiante].items():
            print(f"{materia}: {lista_notas}")
    else:
        print("Estudiante no encontrado o sin notas registradas")
        

def ver_promedio():
    nombre = input("Ingrese el nombre del estudiante")
    if nombre in notas and notas[nombre]:
        total, cantidad = sum(sum(n) for n in notas[nombre].values()), sum(len(n) for n in notas[nombre].values())
        print("Promedio:", round(total / cantidad, 2) if cantidad > 0 else "No tienes notas para calcular el promedio.")
        
    else:
        print("No tienes notas")



def menu_profesor():
    while True:
        opcion = input("1. Agregar nota\n2. Ver nota\n3. Salir\n")
        if opcion == "3":
            break
        {"1": agregar_nota, "2": ver_notas}.get(opcion, lambda: print("Opcion invalida"))()
#


def menu_estudiante():
    while True:
        opcion = input("1. Ver mis notas\n2. Ver promedio\n3. Salir\n")
        if opcion == "3":
            break
        {"1": ver_notas, "2": ver_promedio}.get(opcion, lambda: print("Opcion invalida"))()



def menu():
    while True:
        opcion = input("1. Registrar\n2. Iniciar sesion\n3. Salir\n")
        if opcion == "1":
            Registrar()
        elif opcion == "2":
            user = iniciar_sesion()
            if user:
                (menu_profesor if user["tipo"] == "profesor" else menu_estudiante)()
        elif opcion == "3":
            break
        else:
            print("Opcion invalida")

menu()


