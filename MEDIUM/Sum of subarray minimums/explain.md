##Hint 1: Think in terms of contribution

Instead of enumerating all subarrays, ask:
For each element arr[i], in how many subarrays is it the minimum?
If you can count that, then its contribution to the total sum is simply:
arr[i] * (number of subarrays where arr[i] is minimum)


Hint 2: Boundaries of influence
For each element, you need to know:
- How far left you can extend before hitting a smaller element.
- How far right you can extend before hitting a smaller element.
That defines the range of subarrays where arr[i] is the minimum.


Hint 3: Use monotonic stacks
To find those boundaries efficiently:
- Use a monotonic stack to compute the previous smaller element for each index.
- Use another monotonic stack to compute the next smaller element for each index.




# Now, some COMMON QUESTIONS: 

## 1. Can I use extra arrays for this problem? 

I will need two arrays for precomputing the prev smaller and next smaller, right?
Will I still need a 'stack' then?

## ANSWER:
Absolutely, you will need to use arrays for precomputation.
That's why, the required auxiliary space is O(n).
Yes, you will still need a 'stack'!
The efficient way to fill them is with a monotonic stack. 
The stack is just the tool that lets you build those arrays in O(n).
So the stack isn’t the end goal 
— it’s the mechanism to populate the arrays you want.

## 2. Can't I use variables to store prev smaller and next smaller instead of using stacks?

## ANSWER:
You can try to use just variables, but here’s the catch:
- For each element, you need to know how far left and how far right you can extend before hitting something smaller.
- If you only keep a single variable for “previous smaller” or “next smaller,”
   you’ll lose track of the correct boundary for each index. 
- You’d end up re‑scanning the array multiple times, 
   which pushes you back toward O(n²).

- So, you will need to use a 'stack'
   no matter how much you hate it! XD