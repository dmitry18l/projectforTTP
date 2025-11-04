import threading
from server import Server

def client_thread(client_name):
    server = Server()
    data = None
    result = None

    while True:
        print(f"\n=== Меню {client_name} ===")
        print("1. Ввод матрицы")
        print("2. Генерация матрицы")
        print("3. Поворот матрицы")
        print("4. Вывод результата")
        print("5. Выход")
        choice = input(f"{client_name} выберите пункт: ")

        if choice == '1':
            data = server.process_input_matrix(client_name)
            result = None
        elif choice == '2':
            n = int(input("Введите количество строк: "))
            m = int(input("Введите количество столбцов: "))
            data = server.process_generate_matrix(client_name, n, m)
            result = None
            print(f"{client_name}: сгенерированная матрица:")
            for row in data:
                print(row)
        elif choice == '3':
            if data is None:
                print("Сначала введите или сгенерируйте матрицу!")
            else:
                direction = input("Введите направление ('clockwise' или 'counterclockwise'): ")
                result = server.process_rotate_matrix(client_name, data, direction)
                print(f"{client_name}: повернутая матрица:")
                for row in result:
                    print(row)
        elif choice == '4':
            if result is None:
                print("Сначала выполните алгоритм!")
            else:
                print(f"{client_name}: результат:")
                for row in result:
                    print(row)
        elif choice == '5':
            print(f"{client_name}: завершение работы")
            break
        else:
            print("Неверный выбор")

# Запуск нескольких клиентов в отдельных потоках
if __name__ == "__main__":
    clients = ['Клиент1', 'Клиент2']  # можно добавить больше
    threads = []
    for name in clients:
        t = threading.Thread(target=client_thread, args=(name,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
