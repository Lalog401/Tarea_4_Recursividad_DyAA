def suma(arr):
    if len(arr) == 0:        # Caso base
        return 0
    return arr[0] + suma(arr[1:])  # Caso recursivo


numeros =  [15,25,45,401,777]

# Llama a la función
resultado = suma(numeros)

print("Lista:", numeros)
print("Suma:", resultado)
