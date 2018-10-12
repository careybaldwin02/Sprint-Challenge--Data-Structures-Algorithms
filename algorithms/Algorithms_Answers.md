Add your answers to the Algorithms exercises here.

a) 

I'm thinking of n as the length of a list.  As n increases the number of operations increases proportionally.  If this is correct, then the runtime complexity of the above code should be O(n).  

b) 

My understanding is that each time we loop over a set number of n elements we increase the number of operations by a factor of n.  So this looks to have time complexity O(n^3) because there are three loops that loop over the n items.

c)

This looks to be a recursive function where each subsequent call of the function has an input that is reduced by one.  This suggests to me that the time complexty would be O(n!).

# I need to discuss why this is O(n) complexity

d) 

We discussed some examples similar to this in lecture.  This sounds a lot like looking for a word in the dictionary.  I think the best approach would be to start by setting f as the midpoint to see if the egg breaks.  If it breaks on the first drop, we would try dropping from the midpoint of the lower half of the building, if it doesn't break on the first drop, we would try dropping it from the midpoint of the upper half of the building.  We would continue operate in this way until we have located the highest point from which we can drop the egg without breaking it.  This would have time complexity O(log(n)) since each comparison reduces the operations by half. 