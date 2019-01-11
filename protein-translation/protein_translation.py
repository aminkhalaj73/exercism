b = {'AUG' : 'Methionine' , 'UUU' : 'Phenylalanine' , 
'UUC' : 'Phenylalanine' , 'UUA' : 'Leucine' , 'UUG' : 'Leucine'
, 'UCU' : 'Serine' , 'UCC' : 'Serine' , 'UCA' : 'Serine' ,
'UCG' : 'Serine' , 'UAU' : 'Tyrosine' , 'UAC' : 'Tyrosine'
, 'UGU' : 'Cysteine' , 'UGC' : 'Cysteine' , 'UGG' : 'Tryptophan'
, 'UAA' : 'Stop' , 'UAG' : 'Stop' , 'UGA' : 'Stop'}


def proteins(strand):
    import re
    import itertools
    from collections import OrderedDict
    s=[]
    if type(strand) == str :
        strand = [strand[i:i+3] for i in range(0, len(strand), 3)]   #break the given protein string to 3 character and move them to a list
        for i in strand:
            s += [value  for (key , value) in b.items() if re.match(key , i) != None]  #this list comprehension find every matching elements of above list with our keys
            z = itertools.takewhile(lambda value : value != 'Stop' , s)
        return list(OrderedDict.fromkeys(z))    
    else : 
        s += [value  for (key , value) in b.items() if re.match(key , (''.join(strand))) != None ] #if the given proteins are in a list ''.join(strand) make string out of every one of them and then we can search for equivalent keys
        z = itertools.takewhile(lambda value : value != 'Stop' , s)
        return list(OrderedDict.fromkeys(z))

#itertools.takewhile(predicted , iterator) ====> by this method I could somehow bring while condition to my list comprehension ,
# by takewhile i could stop returning values when value was equals to 'Stop' , takewhile takes an expression in its first arguments
# as predicted and within this argument we can define a if condition too _ as i did in my code_ and in its second argument
#we should give it a iterator like a string or list or etc.

#orderdict.formkeys() ====> this method is for returning the list in order and avoid elements repitition , we could use set() for eleminating
# repeated elements but set() function does not keep order of our . in fact orderdict.formkeys() does what set() function do but keep the order
    
#





# def test():
#     a1 = ['UUU', 'UUC']
#     a2 = ['UUA', 'UUG']
#     a3 = ['UCU', 'UCC', 'UCA', 'UCG']
#     a4 = ['UAU', 'UAC']
#     a5 = ['UGU', 'UGC']
#     a6 = ['UAA', 'UAG', 'UGA']
#     a7 = 'AUGUUUUGG'
#     a8 = 'UAGUGG'
#     a9 = 'UGGUAG'
#     a10 = 'AUGUUUUAA'
#     a11 = 'UGGUAGUGG'
#     a12 = 'UGGUGUUAUUAAUGGUUU'
#     assert proteins(a1) == ['Phenylalanine']
#     assert proteins(a2) == ['Leucine']
#     assert proteins(a3) == ['Serine']
#     assert proteins(a4) == ['Tyrosine']
#     assert proteins(a5) == ['Cysteine']
#     assert proteins(a6) == []
#     assert proteins(a7) == ['Methionine', 'Phenylalanine', 'Tryptophan']
#     assert proteins(a8) == []
#     assert proteins(a9) == ['Tryptophan']
#     assert proteins(a10) == ['Methionine', 'Phenylalanine']
#     assert proteins(a11) == ['Tryptophan']
#     assert proteins(a12) == ['Tryptophan', 'Cysteine', 'Tyrosine']

#     return "you are green"

# print(test())
        

