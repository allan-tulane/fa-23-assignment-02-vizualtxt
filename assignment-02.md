# CMPS 2200 Assignment 2

**Name:** Ali Sulehria

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  W(n) = O(n)
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  W(n) = O(n^log_4(5)) , leaf dominated and exists below the upper bound *O(n^2)*
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  This tree is balanced. The work function should be below the upper limit O(nlog(n)) as it has log_7(n) levels and work of n at each level.
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  
.  Below upper bound O(n^(2) * log(n)) (log(n) bounded levels, n^2 work at each)
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  Similar to above, but n^3 work at each level. Bounded on upper side by O(log(n) * n^3)
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.   root-dominated!
.  
.  Work of n^1.5 * log(n)^2, existing below O(n^2 * log(n)), (although it may also exist under O(n^1.5 * log(n)^2)...)
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  balanced - ish?
.  total work, because work decreases by 1 each recurrence and each level has a cost of 2, should be about 2 * 0.5n * 2, so n.
.  As such, upper bound is O(n),
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.  
.  there will be n-1 levels, with n^c work done at each, so the total work done should be bounded 
.  by O(n^(c+1))
.  
  * $W(n)=W(\sqrt{n})+1$

. this is heavily root-dominated, and the levels will be bounded by O(log(n))

2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    A. W = 5W(n/2) + O(n) // O(5^log_2(n)) = O(n^log_2(5)) ~= O(n^2.322) exists on O(n^3)

    B. W = 2W(n-1) + 1 // O(2^n)

    C. W = 9W(n/3) + O(n^2) // O(log(n) * n^2)

    I would choose algorithm A, as it has the best runtime for n approaching infinity.




3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


