def ghost() :

    word = ''
    CHECK = True

    print '\nWelcome to Ghost!'
    print 'Player 1 goes first.'
    print 'Current word fragment:' , word
    
    p_1 = raw_input('Player 1 says letter: ')

    if p_1 in string.ascii_letters :

        p_1 = string.upper(p_1)
        word += p_1

        while CHECK == True :

            print '\nCurrent word fragment:' , word
            print "Players 2's turn."

            p_2 = raw_input('Player 2 says letter: ')

            if p_2 in string.ascii_letters :

                p_2 = string.upper(p_2)
                word += p_2
                        
            else :

                print 'Player 2 loses because input not a alphabetic character!'

                return

            check = False
            Word = string.lower(word)
            
            if len(word) > 2 :

                for i in word_list :

                    if i == Word :

                        print '\nCurrent word fragment:' , word
                        print "Player 2 losses because '" , word , "' is a word!"
                        print 'Player 1 wins!'

                        return
                    
                    elif i[0:len(word)] == Word : check = True

                if check == False :

                    print '\nCurrent word fragment:' , word
                    print "Player 2 losses because no word begins with'" , word , "'"
                    print 'Player 1 wins!'

                    return

            print '\nCurrent word fragment:' , word
            print "Players 1's turn."
            
            p_1 = raw_input('Player 1 says letter: ')

            if p_1 in string.ascii_letters :

                p_1 = string.upper(p_1)
                word += p_1

            else :

                print 'Player 1 loses because input not a alphabetic character!'

                return

            check = False
            Word = string.lower(word)

            if len(word) > 2 :

                for i in word_list :

                    if i == Word :

                        print '\nCurrent word fragment:' , word
                        print "Player 1 losses because '" , word , "' is a word!"
                        print 'Player 2 wins!'

                        return
                    
                    elif i[0:len(word)] == Word : check = True

                if check == False :

                    print '\nCurrent word fragment:' , word
                    print "Player 1 losses because no word begins with'" , word , "'"
                    print 'Player 2 wins!'

                    return

    else : print 'Player 1 loses because input not a alphabetic character!'
