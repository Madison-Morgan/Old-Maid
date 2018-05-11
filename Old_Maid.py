# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


        


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck





def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

################################################################################
    

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
    
     # because the deck of cards is shuffled previously to this, we can just have the
     # deck of cards appended to our lists

     dealer=deck[:27]
     other=deck[27:]

     return (dealer, other)
 




def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    no_pairs=[]

    # So we sort so that the list is in order, which makes it easy to compare previous, and present elements of the list-
    # as we have already learned this function in the previous lecture, i assumed it was okay to use it
    # I added a random element to the end of the list so that we can append the last pair (if applicable) too the no_pairs list
    # without it, the previous and present elements (of the last pairs of the list) would never not be the same rank as each other and not get appended to the list
    # tmp is a temporary variable that will count how many pairs there are of the same rank, appending a card only if there are an odd number of cards of the same rank
    
    
    l.sort()
    l.append("PlaceHolder")
    i,tmp=0,0
    
    for i in range(1,len(l)):
        if l[i-1][0]==l[i][0]:
            tmp+=1
        else:
            if tmp%2==0:
                no_pairs.append(l[i-1])
                tmp=0
            else:
                tmp=0
  

    random.shuffle(no_pairs)
    return no_pairs




def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for i in range(len(deck)):
        print(deck[i], end=" ")
    print("\n")



    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     print("I have ", n, " cards. If 1 stands for my first card and ", n," for my last card, which of my cards would you like?")
     print("Give me an integer between 1 and", n, ": ", end="")
     ans=input("")
     t=0
     while t<1:
         ans=int(ans)
         if (ans>=1 and ans<=n):
             return ans
         else:
             print("Invalid number. Please enter between 1 and", n, ": ", end="")
             ans=input("")




def formatting(gv):
    '''(num)->string
    Function: returns a string which is a prefix for the number, gv input
    Preconditions: gv must be integer number >= 0
    '''
    if  gv>=4:
        return "th"
    elif gv==1:
        return "st"
    elif gv==2:
        return "nd"
    elif gv==3:
        return "rd"




def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("\nHello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:\n")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()

     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     #turn is even when players turn, odd when robots turn
     turn=0
     temp=0

     while (len(human)> 1 or len(dealer) >1):


         if turn%2==0:
             turn+=1
             print("***********************************************************")
             print("Your turn.\n")
             print("Your current deck of cards is:\n")

             print_deck(human)
             gv=get_valid_input(len(dealer))

             print("You asked for my ", gv,formatting(gv), "card.")
             print("Here it is. It is ", dealer[gv-1], "\n")
             
             human.append(dealer[gv-1])
             
             print("With ", dealer[gv-1], " added, your current deck of cards is:\n")
             print_deck(human)

             print("And after discarding pairs and shuffling, your deck is:\n")
             human=remove_pairs(human)
             print_deck(human)

             dealer.remove(dealer[gv-1])
            
             wait_for_player()
             
         else:
             turn+=1
             print("***********************************************************")
             print("My turn.\n")
             temp=random.randint(1,len(human))
             
             print("I took your",temp,formatting(temp),"card.")
             dealer.append(human[temp-1])
             dealer=remove_pairs(dealer)
             human.remove(human[temp-1])
             wait_for_player()

     print("***********************************************************\n")

     if len(human) == 1 and human[0][0]=="Q":
         print("Ups. I do not have any more cards")
         print("You lost! I, Robot, win")
     else:
        print("Ups. You do not have any more cards")
        print("Congratulations! You, Human, win")

        
# main
play_game()

