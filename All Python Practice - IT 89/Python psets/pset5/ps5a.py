def get_word_score(word,n) :

    Score = int()

    for i in word :

        Score += SCRABBLE_LETTER_VALUES[i]

    if len(word) == n : return Score + 50
    else : return Score
