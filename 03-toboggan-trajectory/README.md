# Notes

Again, functional, but unsure of best practices. eg; maybe I should rename `i` and `j` to something like `y_pos` and `x_pos`. More descriptive, but I personally appreciate the shorter lines of code when dealing with this relatively simple problem.

I was a little unsure of a couple of my choices in part 1, and part 2 confirmed those concerns. Had to replace a few hard-coded values with variables and derive the values from the input, which is probably what I should have done from the start.

Inspired by some friends' solutions, I updated my code to use map reduce instead of a for loop to multiply the counts of trees encountered on various slopes. It feels a little more complicated, but I like the fact that I'm not introducing `product = 1` and instead am just multiplying the actual values.
