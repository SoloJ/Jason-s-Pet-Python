import game_engine

def gameplay():
    color_decoder = {"1":"red", "2":"blue", "3":"yellow", "4":"green", "5":"purple", "6":"black" }
    difficulty = input("Input your level of difficulty...")
    mastermind = game_engine.GameEngine(difficulty, color_decoder)
    mastermind.SequenceGen()
    mastermind.ColorKey()
    mastermind.UserInput()

    print(3)




gameplay()