from matrix_input import input_matrix

def main():
    print("=== Тест ручного ввода матрицы ===")
    matrix = input_matrix()
    print("\nВведённая матрица:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
