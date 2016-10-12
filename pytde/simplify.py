#!/usr/bin/env python
f = open('CalcTriStrains.py','r')
string = f.read()
lines = string.split('\n')

def find_all(string,sub):
  all_idx = []
  idx = -1
  while True:
    idx = string.find(sub,idx+1)
    if idx == -1:
      break
    all_idx += [idx]  
      
  return all_idx


def find_parentheticals(string):
  # find the indices of all open parenthesis
  open_idx = find_all(string,'(')
  open_sign = [0]*len(open_idx)
  close_idx = find_all(string,')')
  close_sign = [1]*len(close_idx)
  idx = open_idx + close_idx    
  sign = open_sign + close_sign
  idx_sign = zip(idx,sign)
  idx_sign.sort()
  idx = [i[0] for i in idx_sign]
  sign = [i[1] for i in idx_sign]
  pairs = []             
  while (sign.count(1)>0) & (sign.count(0)>0):
    a = sign.index(1) - 1
    pairs += [(idx.pop(a),idx.pop(a))]
    sign.pop(a)
    sign.pop(a)
  
  out = []
  for pa,pb in pairs:
    out += [string[pa+1:pb]] 

  return out

e11 = lines[186][8:]
e22 = lines[186][8:]
e33 = lines[186][8:]
e12 = lines[186][8:]
e13 = lines[186][8:]
e23 = lines[186][8:]
all = '+'.join([e11,e22,e33,e12,e13,e22])

terms = find_parentheticals(string)
unique_terms = list(set(terms))
blerg = []
for t in unique_terms:
  c = terms.count(t)
  blerg += [(c,t)]

blerg.sort()
print(blerg)



