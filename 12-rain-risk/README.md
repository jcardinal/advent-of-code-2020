# Notes

## Part One

I confirmed that all of the L and R lines in the example and input data were divisible by 90, meaning we're always facing one of the four cardinal directions. The code I've written relies on that being true.

This feels like an excessive number of `elif`s, but the first few ideas I had to avoid that didn't feel right. I also wonder if it'd be better to replace `northsouth` and `eastwest` with a two-item list or a dict. It'd also probably be cleaner to parse out the letter and the number from each line at the start of the for loop instead of repeatedly slicing and casting on every line.
