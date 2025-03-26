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

