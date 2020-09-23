# RSA
A RSA Key Generation Algorithm. Does not have encryption.

## What is RSA?

RSA is a *public key algorithm* used to secret keys on public channels.

## How Does it Work?
You can read the [Wikipedia article](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) for more information
but the **basic** description is as follows:
>RSA is a algorithm based on the difficulty of prime
>factorizing numbers. 
>- Find two large primes.
>- Multiply the primes to get your public key
>- Calculate the Euler's Totient Function of your public key.
>- Create a private key by calculating the modular-inverse of a number that is co-prime to the totient of your public key, and the totient of your public key.

## :warning: IMPORTANT :warning:

This is not a fully-secure version of RSA.

