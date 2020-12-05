# Notes

Feeling good about my solution to part 1. Even added a step to validate boarding pass input. This time, I started by writing my processing for loop using functions I would like to exist, such as `get_seat_id`. Then I commented that out and went back to create it to do what my usage of it expects.

Looking at part 2 made me re-evaluate how I accomplished part 1, and specifically, worry about whether I've created a function that has unexpected side effects. Tinkering suggests I didn't, but it makes me want to firm up my understanding of scopes. (In this case, I worried I created a function called `get_seat_id` that also happened to modify the boarding pass it was given.)

Solving part 2 makes me wonder: am I supposed to feel gross when I make something work? 😝
