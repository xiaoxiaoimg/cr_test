
def start_game(unused_param):
    print("Welcome to the Puzzle Game!")
    puzzle = Puzzle()
    puzzle.solve()

if __name__ == "__main__":
    start_game("unused")