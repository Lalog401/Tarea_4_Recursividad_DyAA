def cant_num(numero):
    if(numero == 0):
        return 0
    
    return cant_num(numero // 10) + 1



# Ejemplo de uso

entero = 152545401777
res = cant_num(entero)
print(res)