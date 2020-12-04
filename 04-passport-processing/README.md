# Notes

Part 1 solution...feeling fine?

I was feeling smart with my dicts from part 1, and using ranges for my numeric validation tests in part 2, but I learned a couple things:

1. ranges are inclusive of the first value and exclusive of the second
2. you need to think carefully about if/else logic when using it to return a bool to exit a function; I forgot an else to return False, allowing the function to continue executing until all other tests passed and it incorrectly returned True for some passports.
