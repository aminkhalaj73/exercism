def is_pangram(sentence):
    import string
    count = 0
    count2 = 0
    for i in set(sentence) :
        if 64<ord(i)<91 :
            count += 1
        elif 96<ord(i)<123 :
            count2 += 1
        else :
            pass
    if count2< 26 and count == 26 :
        return True
    elif count < 26 and count2 == 26:
        return True
    elif count < 26 and count2 < 26 and count + count2 >= 26 :
        b=[] 
        for i in set(sentence) :
            if 64<ord(i)<91 :
                b += chr(ord(i)+32)
            elif 96<ord(i)<123 :
                b +=chr(ord(i)) 
            else :
                pass
        if len(set(b)) == 26 :
            return True
        else:
            return False
    else :
        return False
