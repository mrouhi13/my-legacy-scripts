def is_valid_word(word,hand,word_list) :

    check = False
        
    for i in word_list :

        if i == word : check = True

    if check == True : True
    else : return False

    Hand1 = hand.copy()
    Hand2 = {}

    for i in word :

        Hand2[i] = Hand2.get(i,0) + 1

    for i in Hand2 :

        check = False

        for j in Hand1 :

            if j == i : check = True

    if check == True : True
    else : return False
    
    for i in Hand2 :

        if Hand1[i] >= Hand2[i] : check = True
        else : return False

    return True
