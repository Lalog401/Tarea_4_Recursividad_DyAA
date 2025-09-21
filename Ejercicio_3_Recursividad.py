def eliminar_medio(p, n):
    if n == len(p):
        n //= 2
    if len(p) <= 2:
        return
    if n == 0:
        p.pop()
        return

    t = p.pop()

    eliminar_medio(p, n - 1)

    p.append(t)


# Prueba de la función
pila = [1,2,3,4,5,6,7,8,9,10]
tam = len(pila)
eliminar_medio(pila, tam)
print(pila)
