class Card:
    """ 
    Each playing card is represented as a a suit and a rank with
        Suits:  S , C , D , or H
        Value : 2 , 3 , 4, 5, 6, 7, 8, 9, 10, J, Q ,K ,A
    """
    suit = None
    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # when passed through as a string, with suit followed by a space then the rank 
    def __init__(self,str):
        x = str.split()
        self.suit = x[0]
        self.value = x[1]

    def getVal(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
