def main():
    import re
    from random import randrange

    list_of_words = ['ASLI','ALMUTH', 'SALVADOR', 'SARRA','HRISTO', 'RASIKA', 'ATTILA', 'ELENI', 'OSVEH', 'PIA', 'ZUBEYDE', 'VICTOR', 'GIAN', 'MOHAMMED']
    word = list_of_words[randrange(len(list_of_words))]
    print('Lets play the hangman!')
    print('You have 5 chances to guess the word\n Lets start!')
    lngt = len(word)
    hidden = '_'*lngt
    w = 0
    rep = []
    x = 0
    y = 5
    hm_steps = ['________\n  |\n', '________\n  |\n  O\n', '________\n  |\n  O\n  | \n', '________\n  |\n  O\n /|\\ \n', '________\n  |\n  O\n /|\\ \n  |\n', '________\n  |\n  O\n /|\\ \n  |\n / \\ \n']
    sl = ('==============================================') 

    while x < y and w < lngt: # noticed i left the five instead of putting the y
        print(sl)
        print(f'here is the secret word: ', hidden)
        print(hm_steps[x])
        print('Write a letter or the full "word": ')
        guess = input().upper()

        if guess == word:
            print(sl)
            print('CONGRATULATIONS! You guessed the word')
            print('The hidden word was: ' + word)
            print('  __    __\n'+'  |__|  |__|\n'+'       >\n' +'   :      :\n'+'    :....:\n')
            w = lngt + 1
            restart = input('Do you want to start again? (type yes:) ').lower()
            if restart == 'yes':
              main()
            else:
              exit()
        elif len(guess) > 1:
            print('Only one letter character or full word allowed!')

        if guess not in word and x < y:
            x = x + 1
            if not re.match("^[A-Z]*$", guess):
                print('Only letters allowed')
            print('wrong guess now you have '+ str(y-x) + ' chances!\n')

        if guess in rep:
            print('REPEATED LETTER!')
        elif guess in word and len(guess) < 2 and len(guess) > 0:
            w = w + word.count(guess)
            rep.append(guess)
            for nl in range(lngt): #THIS WAS MY HEADACHE for the numer of letters in the range of the lenght of the hidden word
                if word[nl] == guess: #IF a letter in the WORD to guess on that range matches 
                    hidden = hidden[:nl] + guess + hidden[nl + 1:] # hidden(variable) is changed taking the first characters till the number of the matching letter
            print(f'Correct! The word contains {guess}')           #then adding the letter that was introduced and then adding the rest of the characters after the match

        if guess not in word and x < y and len(guess) < 2:
           rep.append(guess)

        if x == y:
            print(sl)
            print(hm_steps[x])
            print('You lose!')
            print('x       x\n'+'  x   x\n'+'    x\n'+'  x   x\n'+'x       x\n')
            x = x + 1
            restart = input('Do you want to start again? (type yes:) ').lower()
            if restart == 'yes':
              main()
            else:
              exit()
        
        if w == lngt:
            print(sl)
            print('Congratulations you guessed the word and won the game!')
            print('The hidden word was: ' + word)
            print('  __    __\n'+'  |__|  |__|\n'+'       >\n' +'   :      :\n'+'    :....:\n')
            restart = input('Do you want to start again? (type yes:) ').lower()
            if restart == 'yes':
              main()
            else:
              exit()

main()
