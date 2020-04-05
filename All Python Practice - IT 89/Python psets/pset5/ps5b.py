def update_hand(hand,word) :

    Hand = {}

    for i in word :
        for j in hand.keys() :

                if i == j : hand[j] = hand.get(j,0) - 1

    for i in hand :

        if hand[i] > 0 :
            Hand[i] = Hand.get(i,0) + hand[i]

    return Hand
