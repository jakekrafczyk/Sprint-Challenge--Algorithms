#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) if n = 2, then we have while (a < 8): a = 0 + 4, then a = 4 + 4. if n = 3, then we have while (a < 27): a = 0 + 9, then 9 + 9, then 18 + 9. Each increase in n adds an additional loop so this is 0(n).


b) if n=2, there are two loops for i and two for j. if n = 3, there are three loops for i and six for j. if n=4, there are four for i and eight for j. This is 0(log n) because it starts off as 0(n^c) where c is two but then only has a slight increase at even numbers.


c) the bunny ears function just counts down at increments of one from the original bunnies value until it equals 0, so it would have a runtime of 0(n).

## Exercise II

To minimize broken eggs => starting at 0, i would drop an egg from every floor, moving up 1 by 1 until an egg breaks. That floor would be designated as f.

To minimize dropped eggs => starting at 0, i would drop an egg from every every n/10 floors(10% increments), then when an egg breaks, move down floor by floor until an egg doesnt break, designating the last floor an egg broke on as f.
