
with open('config.txt', 'r') as file:
    config = file.read()


if config is not None:
    print("Config loaded")


try:
    # some code
except:  
    handle_error()  


def start_game():
    count = 0  
    while count < game_constants.MAX_ZOMBIES:
        count += 1
        if count is not None:  
            print(f"Zombie {count} spawned")

if __name__ == "__main__":
    start_game()