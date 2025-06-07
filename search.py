class search:
    def __init__(self):
        self.mstr = None
        self.sstr = None
    def input(self):
        self.mstr = input("Enter the main string: ")
        self.sstr = input("Enter the string to search for: ")
    def position(self):
        pos = self.mstr.find(self.sstr)
        if pos != -1:
            print(f"'{self.sstr}' found at position {pos}")
        else:
            print(f"'{self.sstr}' not found in the main string.")
s = search()
s.input()
s.position()