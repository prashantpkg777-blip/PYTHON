s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(s,len(s)) # length is 2 because 20==20.0