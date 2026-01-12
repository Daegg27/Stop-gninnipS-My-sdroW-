def spin_words(sentence):
    
    
    new_list = []
    single_word = ""
    final_string = ""
    
    if sentence.find(" ") == -1 and len(sentence) < 5: 
        return sentence
    elif sentence.find(" ") == -1 and len(sentence) >= 5:
        return sentence[::-1]
    else:
        for i in range(len(sentence)):
            
            
            if sentence[i] != " ":
                single_word += sentence[i]
            else: 
                new_list.append(single_word)
                single_word = ""
            
            if i == len(sentence) - 1: # Adds the final word, which wouldn't get added due to the abscense of a space, before exiting the loop
                new_list.append(single_word)
        
        for word in new_list:
            if len(word) < 5:
                final_string += word
                final_string += " "
            else:
                final_string += word[::-1]
                final_string += " "
                
        return final_string.rstrip() # Removes the trailing space off the string