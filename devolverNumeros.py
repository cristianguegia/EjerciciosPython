def devolver_distintos():
    # Pedir al usuario que ingrese los números
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    
    suma = num1 + num2 + num3
    
    print("La suma de los tres números es:", suma)
    
    if suma > 15:
        return max(num1, num2, num3)# devuelve el numero mayor
    elif suma < 10:
        return min(num1, num2, num3) # devuelve el numero menor
    else:
        return sorted([num1, num2, num3])[1]  #organiza de menor a mayor y se imprime la posicion deseada

# Ejemplo de uso:
resultado = devolver_distintos()
print("Número devuelto:", resultado)
