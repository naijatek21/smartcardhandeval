import card
import hand
from enum import Enum;

class Rank(Enum):
    STRAIGHT_FLUSH = 9  
    FOUR_OF_A_KIND = 8 
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1

def evaluate(hand,comm_cards):
    cardList=[]
    for card in comm_cards:
       new_card= card.__init__(card)
       cardList.add(new_card)
    hashed_cards= hand.getCards() + comm_cards

    #Check for matches
    straight_check = set(hashed_cards.sort(card.getVal))
    
    matches = list.ones(len(hashed_cards))
    suitMatches = {"S":0, "H":0, "C":0 , "D":0}
    for c1 in range(len(hashed_cards)):
     for c2 in range(c1,len(hashed_cards)):
        if hashed_cards[c1].value == hashed_cards[c2].value:
           matches[c1] +=1
        if hashed_cards[c1].suit == hashed_cards[c2].suit:
            suitMatches[hashed_cards[c1].suit]+=1        
    pair = False
    trips = False
    for match in matches:
        if match == 4:
            hand.assignRanking(Rank.FOUR_OF_A_KIND)
            break
        if match == 2:
            if pair:
                hand.assignRanking(Rank.TWO_PAIR)
                break
            else:
                pair=True
        if match == 3:
            trips = True
    if trips and not pair:
        hand.assignRanking(Rank.THREE_OF_A_KIND)
    if pair:
        if trips:
            hand.assignRanking(Rank.FULL_HOUSE)
        else:
            hand.assignRanking(Rank.PAIR)
    for sM in suitMatches:
        if sM == 5:
            hand.assignRanking(Rank.FLUSH)
            break 

    
    

          
          



          

    

     


        

  
