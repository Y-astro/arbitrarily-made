class search:
<<<<<<< HEAD
    def __init__(self, main_string = None, search_string = None):
        self.main_string = main_string
        self.search_string = search_string
    def get_input(self):
        if self.main_string == None:
            self.main_string = input("Enter the main string: ")
        if self.search_string == None:
            self.search_string = input("Enter the string to search for: ")
    def perform_search(self):
        position = self.main_string.find(self.search_string)
        if position != -1:
            return(f"'{self.search_string}' found at position {position}")
        else:
            return(f"'{self.search_string}' not found in the main string.")
if __name__ == "__main__":
    s = search()
    s.get_input()
    result = s.perform_search()
    print(result)
=======
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
>>>>>>> 09b2586729cc72d33220e4ab7919364191896bf4
