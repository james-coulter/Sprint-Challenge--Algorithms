#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear Time || Initially the while loop compares a with n^3 (O(n^3)),
 but then adds a to n^2, making the problem linear.


b) O(n^2) - Exponential || Nested for loop with dependence on the size of n


c) O(n) - Linear || Even though it is recursive, I still think it
is linear because it depends on how many bunnies are passed in.

## Exercise II

I would use a Binary Search where I checked the middle point and
if broken_egg = True move to the middle 'downwards' and check. If
broken_egg = False move 'upwards'. Repeat. O(log n) worst case.
