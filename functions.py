def print_list(words):
    for i in words:
        print(i)

def concatenate(words):
    """ This function takes a list of words and combines them into one string

    Arguments: 
        words {List} -- strings to be concatenated

    Returns
        String -- concatenated string, words separated by space
    """

    # variable container for concatenated words
    full_string = ""

    for i in words:
        full_string = full_string + i + " "
    
    return full_string

class Room:
    def __init__(self, price, room_open):
        self.price = price
        self.room_open = room_open
    
    def close_room(self):
        self.room_open = False
    
    def open_room(self):
        self.room_open = True
        
    def get_status(self):
        if self.room_open:
            print("open")
        else:
            print("closed")


