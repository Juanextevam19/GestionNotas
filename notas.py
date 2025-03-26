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


