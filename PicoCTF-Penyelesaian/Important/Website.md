What is pipe
http://www.linfo.org/pipes.html

rockstar lenguange
https://codewithrockstar.com/online

integer limit
Notice that `total_cost` is declared as an `int`. This is specifically a _Signed Integer_, which has a range between `-2,147,483,648` to `2,147,483,647`. Signed integers use the first bit to store whether it is negative or positive, `0` indicating positive and `1` indicating negative. What happens if you add `1` to `2,147,483,647` and store the result in a signed integer? Well the first bit goes from `0` to `1`, meaning that the number is now negative! In fact, due to the way [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement), the method used to represent negative numbers in binary, works, it actually wraps around to the most negative integer: `-2,147,483,648`.

This is what is known as an Integer Overflow. We can use this to overflow the `total_cost` variable and increase our account balance. We need a `total_cost` that is a large negative number, but not too large that it also overflows our `account_balance`. `3000000` works nicely as the number of fake flags to buy: