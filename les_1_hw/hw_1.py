def palindrom(word):
    if word == word[::1]:
        print('True')
    else:
        print('False')
    
palindrom('absba')
palindrom('fasby')