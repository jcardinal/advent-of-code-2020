# Notes

## Part One

Including a bunch of notes on my thought process. Started by trying to define what some useful functions would be, and that list gradually evolved.

### Things I need to do

✅ convert input to a 2-dimensional array (2d list? numpy array? import array module?)  
✅ learn to deep copy that structure (to make a copy, change seats based on rules)  
✅ learn to check equality of this structure (eg; did any seats change or have we stabilized?)

### Wanted functions

~~`get_adjacent(seat)`: given a seat, return the locations of all adjacent seats~~  
~~`all_vacant(seats)`: given a list of seats, return True if all are vacant, or False if any are occupied~~  
~~`count_occupied(seats)`: given a list of seats, return number that are occupied~~  
count_neighbors(seat, array): given a seat and array of seats, count neighbors (occupied adjacent seats)  
`occupancy(seat)`: given a seat location, return the number of occupants in it (0 or 1). A floor space would be zero, as would an out-of-bounds space.

### Counting adjacent occupied seats

given [3][3] (aka: [i][j]), adjacent seats would be:  
[2][2], [2][3], [2][4] (above) aka: [i-1][j-1], [i-1][j], [i-1][j+1]  
[3][2], [3][4] (left and right beside) aka: [i][j-1], [i][j+1]  
[4][2], [4][3], [4][4] (below) aka: [i+1][j-1], [i+1][j], [i+1][j+1]  
UNLESS any of those seats don't exist because we're near an edge
