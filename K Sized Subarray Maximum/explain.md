This problem screams for an efficient way to keep track of the maximum element as we slide a window of size k across the array.  A priority queue (max-heap) feels like a natural fit here, allowing us to effortlessly maintain the largest element at the top while dynamically adjusting the contents as the window moves.

Intuition : 

We'll use a priority queue to store elements within the current window, along with their indices in the original array.
As we slide the window, we'll:
Add the new element entering the window to the priority queue.
Remove elements that are no longer within the window (based on their index).
The top of the priority queue will always hold the maximum element in the current window.

Pseudo Code : 

1. Initialize an empty priority queue 'pq' (max-heap).
2. For the first 'k' elements (0 to k-1):
    * Add (arr[i], i) to 'pq'.
3. Output the top element of 'pq'. // Maximum of the first window
4. For the remaining elements (k to n-1):
    * Add (arr[i], i) to 'pq'.
    * While the index of the top element of 'pq' is less than or equal to i-k:
        * Remove the top element from 'pq'.
    * Output the top element of 'pq'. // Maximum of the current window