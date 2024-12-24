word = "internationalization" 
abbr = "13iz4n"

def validate_word_abbreviation(word, abbr):
    # edge case
    word_index, abbr_index = 0, 0
    while abbr_index < len(abbr):
        if abbr[abbr_index].isdigit():
            if abbr[abbr_index]=='0':
                return False
            num = 0
            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index+=1
            word_index+=num
        else :
            if word_index> len(word) and word[word_index] != abbr[abbr_index]:
                return False
            word_index+=1
            abbr_index+=1
    return word_index==len(word) and abbr_index==len(abbr)


print(validate_word_abbreviation(word, abbr))


        
        
        
