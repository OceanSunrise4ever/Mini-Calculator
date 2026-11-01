**Welcome to the Desmos Replica!**

This is a mini calculator I built using python.

It allows users to perform basic arithmetic operations or analyze the key features of rational functions using advanced algebra rules.

The project uses the sympy library to handle complex calculus and algebra symbols automatically.


## What it does

1. Arithmetic Mode

  Performs quick math calculations using these operators:

    - + Addition
    - - Subtraction
    - * Multiplication
    - / Division (with built-in crash protection for dividing by zero!)
    - ** Exponents (Power)
    - // Floor Division
    - % Modulo (Remainder)
    - & Bitwise AND

2. Graphing & Function Analysis Mode

  Input a rational function in standard math notation (like f(x) = (2*x**2 + 3*x - 5) / (x - 1)) to instantly discover:

    - Zeros: Where the numerator equals zero.
    
    - Vertical Asymptotes: Where the denominator equals zero.
    
    - Horizontal Asymptotes: Calculated by comparing the highest exponents on the top and bottom.
    
    - Y-Intercept: The value of the function when \(x = 0\).
    
    - Holes: Points where the graph breaks.


## How it works

When the user first enters an equation, the code asks you what mode you would like to use and what you want to find. From there, you can keep asking follow-up questions.

## Built with

- **Sympy** - symbolic mathematics (used so that it can perform algebra and equation solving)

## What I learned

The most challenging part of building this project was understanding how sympy works. I'm used to coding without using libraries so using libraries was a new experience for me.



Libraries: sympy
