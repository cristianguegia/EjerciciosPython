def letras_unicas_en_orden(palabra):
    letras_unicas = list(set(palabra))  # Elimina las repeticiones y convierte a lista
    # letras_unicas.sort()  # Ordena alfabéticamente
    return letras_unicas

palabra = (input("digite una palabra : "))
resultado = letras_unicas_en_orden(palabra)
print(resultado)
