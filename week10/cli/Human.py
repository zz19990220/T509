class Human:
    def __init__(self, label="O", name="Human player"): #Default Human player is  O
        self.label = label
        self.name = f"{name} - {label}"

    def move(self, left_position):
        choice = input(f"Human player - {self.label}, choose a number from the board:\n>")
        return int(choice)