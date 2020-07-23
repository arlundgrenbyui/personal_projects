This project currently finds loops that exist within a range of numbers based on a function.
Some functions have finite outputs for a given range of inputs. For example, the function:
  f(x): x = x ^ 2 % 100
repeated over and over within the range 2-101 with some inputs will produce a loop.

f(16) => 56; 
f(56) => 36; 
f(36) => 96; 
f(96) => 16; 
f(16) => 56 ...

And so on. This python program explores three different functions and uses the GraphViz Library
to generate images of each loop that exists in the range 2-101 (without duplicate loops)
