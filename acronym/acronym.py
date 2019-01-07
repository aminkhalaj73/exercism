
def abbreviate(words):
    import re
    justchar = re.sub('[-]' , ' ' , words) #remvoing any non-Character or digits from string
    first_letters = "".join(re.findall('^\w|\s\w' , justchar)) #finding first character of words joining them in a string  
    acronym = (re.sub('\s' , '' , first_letters)).upper()  #removing additional whitspaces between frist characters and converting them to uppercase letters
    return acronym


# def test() :
#     l1 = 'Portable Network Graphics'
#     l2 = 'Ruby on Rails'
#     l3 = 'First In, First Out'
#     l4 = 'GNU Image Manipulation Program'
#     l5 = 'Complementary metal-oxide semiconductor'
#     l6 = "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
#     l7 = 'Something - I made up from thin air'
#     l8 = "Halley's Comet"
#     assert abbreviate(l1) == 'PNG'
#     assert abbreviate(l2) == 'ROR'
#     assert abbreviate(l3) == 'FIFO'
#     assert abbreviate(l4) == 'GIMP'
#     assert abbreviate(l5) == 'CMOS'
#     assert abbreviate(l6) == "ROTFLSHTMDCOALM"  #ROTFLSHTMDCOALM
#     assert abbreviate(l7) == 'SIMUFTA' #SIMUFTA
#     assert abbreviate(l8) ==  'HC'

#     return "you are green"

# print(test())


# l1 = 'Portable Network Graphics'
# l2 = 'Ruby on Rails'
# l3 = 'First In, First Out'
# l4 = 'GNU Image Manipulation Program'
# l5 = 'Complementary metal-oxide semiconductor'
# l6 = "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
# l7 = 'Something - I made up from thin air'
# l8 = "Halley's Comet"

# a = re.sub('[-_()/?.><;:"]' , ' ' , l8)
# b = "".join(re.findall('^\w|\s\w' , a))
# s= (re.sub('\s' , '' , b)).upper()
# print(a)
# print(b)
# print(s)

