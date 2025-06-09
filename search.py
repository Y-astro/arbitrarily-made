class search:
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