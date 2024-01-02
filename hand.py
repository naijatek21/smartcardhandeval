class Hand:
    cards = []
    ranking = None
    leadCard  = 0
    def __init__(self,cards):
           self.cards = cards
           
    def getCards(self):
          return self.cards
    
    def assignRanking(self,r):
        self.ranking = r

    def assignLeader(self,lead):
         self.leadCard = lead
          
          
 