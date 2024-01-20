import braillelib

#buttons:
#   automatic
#   rate
#   capture

# overall text to braille conversion.
# input is text in the form of a string
def text_to_braille(text):
    words = text.split()
    max_len = get_max_len() #number of braille blocks
    automatic = get_automatic() #true if in automatic mode
    update_rate = get_update_rate() #update rate if any
    
    i=0
    while i < len(words):
        curr_word = words[i]
        if len(curr_word)>max_len:
            disp_word = curr_word[:max_len]
            remaining = curr_word[max_len:]
            words.pop(i)
            words.insert(i, remaining)
        else:
            disp_word = curr_word
            i+=1
        braille_display_word(disp_word)
        # either automatically shift after specified update rate
        # or wait for button press to shift
        if automatic:
            pass
        else:
            pass

# takes in a single word
# displays it by repeatedly calling 
# braille_character on a vector of 1s and 0s representing the braille version
# of the current character
def braille_display_word(word):
    #parse the word into char
    arr_braille = []
    for letter in word:
        arr_braille.append(braille_character(letter))
    # print(arr_braille)
    return arr_braille
        

def braille_character(bchar):
    char = braillelib.braille_dict.get(bchar)
    # print(char)
    return char


# braille_character(":")
braille_display_word("hello;'")