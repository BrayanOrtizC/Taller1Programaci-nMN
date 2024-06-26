import sys

def interact():
    try:
        # Leer el valor de N desde la entrada estándar
        N = int(input().strip())
        sequence = [0] * N

        # Hacer una única consulta inicial con todos ceros
        print('Q', ' '.join(map(str, sequence)))
        sys.stdout.flush()
        
        # Leer la respuesta del Troll para la consulta inicial
        correct_bits = int(input().strip())

        queries = 1  # Contamos la consulta inicial

        for i in range(N):
            if queries >= N + 1:
                break  # Asegurar que no hacemos más de N + 1 consultas

            # Cambiar el bit en la posición i
            sequence[i] = 1
            
            # Hacer una consulta con el bit cambiado
            print('Q', ' '.join(map(str, sequence)))
            sys.stdout.flush()
            
            # Leer la respuesta del Troll para la consulta cambiada
            new_correct_bits = int(input().strip())
            queries += 1
            
            # Si la cantidad de bits correctos no aumenta, revertir el cambio
            if new_correct_bits <= correct_bits:
                sequence[i] = 0
            else:
                correct_bits = new_correct_bits
        
        # Enviar la respuesta final
        print('A', ' '.join(map(str, sequence)))
        sys.stdout.flush()
    
    except EOFError:
        print("EOFError: No se pudo leer la entrada. Asegúrate de proporcionar todas las entradas necesarias.")
    except ValueError:
        print("ValueError: Entrada no válida. Asegúrate de que todas las entradas sean números enteros.")

if __name__ == "__main__":
    interact()
input("Presiona Enter para salir...")