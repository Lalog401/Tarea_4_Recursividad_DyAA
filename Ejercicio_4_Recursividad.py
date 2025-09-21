def palindromo(txt, i, j):
    if i >= j:
        return True
    if txt[i] != txt[j]:
        return False
    return palindromo(txt, i+1, j-1)


#Ejemplo de uso
pal = "spectre"
print(palindromo(pal, 0, len(pal)-1))

pal2 = "radar"
print(palindromo(pal2, 0, len(pal2)-1))
