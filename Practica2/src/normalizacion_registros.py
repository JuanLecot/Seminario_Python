def eliminar_nombre_invalido(estudiantes):
    resultado =[]
    for registro in estudiantes:
        nombre = registro["name"]
        if nombre is None or not nombre.strip():
            continue
        resultado.append(registro)
    return resultado

def eliminar_nota_invalida(estudiantes):
    resultado=[]
    for registro in estudiantes:
        nota = registro["grade"]
        if nota is None or nota.strip() == "":
            continue
        
        es_valida = True
        for caracter in nota:
            if not caracter.isdigit() and caracter != ".":
                es_valida = False
                break
        
        if not es_valida:
            continue

        resultado.append(registro)

    return resultado

def normalizar_nombres(estudiantes):
    resultado = []
    for registro in estudiantes:
        nombre = registro["name"].title().strip()
        estado = registro["status"].title().strip()

        resultado.append({"name":nombre,"grade":registro["grade"],"status":estado})
    
    return resultado

def eliminar_duplicados(estudiantes):
    resultado = []
    for registro in estudiantes:
        nombre = registro["name"]
        nota = int(registro["grade"])

        encontrado = False
        for registro2 in resultado:
            if registro["name"] == registro2["name"]:
                encontrado = True
                
                if int(registro2["grade"]) < nota:
                    registro2["grade"] = registro["grade"]
                break

        if not encontrado:
            resultado.append(registro)

    return resultado

def ordenar_registros (estudiantes):
    return sorted(estudiantes, key = lambda registro: registro["name"].lower())
        

def limipiar_datos(estudiantes):
    resultado = eliminar_nombre_invalido(estudiantes)
    resultado = eliminar_nota_invalida(resultado)
    resultado = normalizar_nombres(resultado)
    resultado = eliminar_duplicados(resultado)
    resultado = ordenar_registros(resultado)
    return resultado