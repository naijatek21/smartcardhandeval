class Card:
    """ 
    Each playing card is represented as a a suit and a rank with
        Suits:  S , C , D , or H
        Ranks : A , 2 ,3, 4, 5, 6, 7, 8, 9, 10, J, Q ,K
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # when passed through as a string, with suit followed by a space then the rank 
    def __init__(self,str):
        x = str.split()
        self.suit = x[0]
        self.rank = x[1]

        
