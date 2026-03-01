class Solution:
	# Approach 2/3: Direct Placement with Two Phases
	# Time Complexity: O(n) - Two linear passes through array (2*n = O(n))
	# Space Complexity: O(1) - In-place modification, only counter variable
	#
	# Algorithm: Separates logic into two distinct phases
	# Phase 1 (For loop): Scan array and place all non-zero elements at front
	# Phase 2 (For loop): Fill remaining positions with zeros
	# This approach prioritizes clarity and explicit logic separation
	def pushZerosToEnd(self, arr):
		last_free = 0  # Tracks position where next non-zero should be placed
		
		# Phase 1: Collect all non-zero elements to the front
		for a in arr:
			if a:
				# Place non-zero element at position last_free
				# This compacts all non-zeros at the beginning
				arr[last_free] = a
				last_free += 1
		
		# Phase 2: Fill remaining positions with zeros
		# After phase 1, last_free points to first position after all non-zeros
		# All positions from last_free to end MUST be zeros
		for i in range(last_free, len(arr)):
			arr[i] = 0
		# Array now has all non-zeros at front in original relative order, 
		# with all zeros at the end