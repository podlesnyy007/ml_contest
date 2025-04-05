m, k = map (int, input ().split ())
d1 = {14: 'ace', 13: 'king', 12: 'queen', 11: 'jack',
      10: 'ten', 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six'}

d2 = {1: 'spades', 2: 'clubs', 3: 'diamonds', 4: 'hearts'}

print (f"the {d1.get (k)} of {d2.get (m)}")
