from SparseSet import SparseSet

def interactive_sparse_set():
    sparse_set = None

    print("\nComandos:")
    print("  size <n>: Cambiar el tamaño del Sparse Set.")
    print("  insert <x>: Agregar un elemento x al Sparse Set.")
    print("  remove <x>: Eliminar un elemento x del Sparse Set.")
    print("  contains <x>: Verificar si x está en el Sparse Set.")
    print("  exit: Salir de la sesión.\n")

    while True:
        command = input("Introduce un comando: ").strip().lower()
        if command.startswith("size"):
            try:
                n = int(command.split()[1])
                if n <= 0:
                    print("El tamaño debe ser un número positivo.")
                else:
                    sparse_set = SparseSet(n)
                    print(f"Sparse Set iniciado con tamaño {n}.")
                    sparse_set.visualize("Initialize")
            except (IndexError, ValueError):
                print("Formato de comando inválido. Uso: size <n>")
        elif command.startswith("insert"):
            if sparse_set is None:
                print("Primero inicializa el Sparse Set con el comando size.")
                continue
            try:
                x = int(command.split()[1])
                if x < 0 or x >= sparse_set.n:
                    print(f"Error: {x} está fuera de los límites (0 a {sparse_set.n - 1}).")
                else:
                    sparse_set.insert(x)
                    print(f"Insertado {x}.")
                    sparse_set.visualize(f"Insert({x})")
            except (IndexError, ValueError):
                print("Formato de comando inválido. Uso: insert <x>")
        elif command.startswith("remove"):
            if sparse_set is None:
                print("Primero inicializa el Sparse Set con el comando size.")
                continue
            try:
                x = int(command.split()[1])
                if x < 0 or x >= sparse_set.n:
                    print(f"Error: {x} está fuera de los límites (0 a {sparse_set.n - 1}).")
                else:
                    sparse_set.remove(x)
                    print(f"Eliminado {x}.")
                    sparse_set.visualize(f"Remove({x})")
            except (IndexError, ValueError):
                print("Formato de comando inválido. Uso: remove <x>")
        elif command.startswith("contains"):
            if sparse_set is None:
                print("Primero inicializa el Sparse Set con el comando size.")
                continue
            try:
                x = int(command.split()[1])
                if x < 0 or x >= sparse_set.n:
                    print(f"Error: {x} está fuera de los límites (0 a {sparse_set.n - 1}).")
                else:
                    result = sparse_set.contains(x)
                    print(f"{x} está {'en' if result else 'no está en'} el Sparse Set.")
                    subtitle = f"{x} is {'present' if result else 'absent'}"
                    sparse_set.visualize(f"Contains({x})", subtitle)
            except (IndexError, ValueError):
                print("Formato de comando inválido. Uso: contains <x>")
        elif command == "exit":
            print("Saliendo. ¡Adiós!")
            break
        else:
            print("Comando inválido. Intenta de nuevo.")

if __name__ == "__main__":
    interactive_sparse_set()
