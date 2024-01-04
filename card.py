class Card:
    """ 
    Each playing card is represented as a a suit and a rank with
        Suits:  S , C , D , or H
        Value : 2 , 3 , 4, 5, 6, 7, 8, 9, 10, J(11), Q(12) ,K(13) ,A(14)
    """
    suit = None
    value = 0
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    valdict={"A":14, 
              "K":13 , 
              "Q":12, 
              "J":11, 
              "10":10, 
              "9":9, 
              "8":8,
              "7":7 , 
              "6":6,
              "5":5,
              "4":4,
              "3":3,
              "2":2,
              }
    # when passed through as a string, with suit followed by a space then the rank 
    def __init__(self,str):
        x = str.split()
        self.suit = x[0]
        self.value = valdict[x[1]]

    def getVal(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
