import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_ships(board, num_ships):
    for _ in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        while board[ship_row][ship_col] == "O":
            ship_row = random.randint(0, len(board) - 1)
            ship_col = random.randint(0, len(board[0]) - 1)
        board[ship_row][ship_col] = "O"

def main():
    board_size = 5
    num_ships = 3

    print("Добро пожаловать в игру Морской бой!")
    
    board = [["~" for _ in range(board_size)] for _ in range(board_size)]
    generate_ships(board, num_ships)

    print_board(board)

    for turn in range(5):
        print(f"Ход {turn + 1}")

        guess_row = int(input("Введите номер строки: "))
        guess_col = int(input("Введите номер столбца: "))

        if board[guess_row][guess_col] == "O":
            print("Поздравляем! Вы потопили корабль!")
            board[guess_row][guess_col] = "X"
        else:
            if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
                print("Вы ввели неверные координаты.")
            elif board[guess_row][guess_col] == "X":
                print("Вы уже стреляли в эту клетку.")
            else:
                print("Промах!")
                board[guess_row][guess_col] = "X"

        print_board(board)

    print("Игра окончена!")

if __name__ == "__main__":
    main()
