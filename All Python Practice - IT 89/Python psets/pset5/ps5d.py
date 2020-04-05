def play_hand(hand, word_list):

    scores = 0
    score = 0
    word = ''

    while not word == '.' :

        check = False

        while not check :

            print 'Current Hand:'

            display_hand(hand)

            word = raw_input('Enter word, or a . to indicate that you are finished: ')

            if word == '.' :

                print 'Total score:' , scores , 'points'
                return

            isvalid = is_valid_word(word,hand,word_list)

            if isvalid == True : check = True
            else : print 'Invalid word, please try again.'

        score = get_word_score(word,len(hand))
        scores += score
        hand = update_hand(hand,word)

        print word , 'earned' , score , 'points. Total:' , scores , 'points'

        if hand == {} :

            print 'Total score:' , scores , 'points'
            return
