def hacer_unicos(arr):
    seen = set()
    operaciones = 0

    for i in range(len(arr)):
        original = arr[i]
        incrementos = 0
        decrementos = 0
        
        # Contar incrementos necesarios para encontrar un número único
        while (original + incrementos) in seen:
            incrementos += 1
        
        # Contar decrementos necesarios para encontrar un número único
        while (original - decrementos) in seen:
            decrementos += 1

        # Escoger la opción con menos operaciones
        if incrementos <= decrementos:
            arr[i] = original + incrementos
            operaciones += incrementos
        else:
            arr[i] = original - decrementos
            operaciones += decrementos

        seen.add(arr[i])
    
    return arr, operaciones

def main():
    import sys
    input = sys.stdin.read
    
    # Leer entrada
    data = input().strip().split()
    
    # Procesar entrada
    N = int(data[0])
    array = list(map(int, data[1:]))
    
    # Hacer los elementos únicos
    resultado, operaciones = hacer_unicos(array)
    
    # Imprimir el resultado
    print(operaciones)

if __name__ == "__main__":
    main()
