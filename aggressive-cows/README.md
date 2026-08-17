<h2><a href="https://www.geeksforgeeks.org/problems/aggressive-cows/1">Aggressive Cows</a></h2>

<h3>Hard</h3>

<hr>

<p>Given an integer array <code>arr</code>, where each element represents the position of a stall. All stall positions are distinct. There are <code>k</code> aggressive cows.</p>

<p>Assign the cows to the stalls such that the <strong>minimum distance</strong> between any two cows is <strong>maximized</strong>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,4,8,9], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The cows can be placed at positions 1, 4, and 8.

The distances are:
4 - 1 = 3
8 - 4 = 4

Therefore, the minimum distance between any two cows is 3,
which is the maximum possible minimum distance.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,1,2,7,5], k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> After sorting the stall positions:

[1,2,5,7,10]

The cows can be placed at positions 1, 5, and 10.

The distances are:
5 - 1 = 4
10 - 5 = 5

Therefore, the minimum distance between any two cows is 4,
which is the maximum possible minimum distance.
</pre>

<p>&nbsp;</p>

<p><strong>Approach:</strong></p>

<p>This problem can be solved using <strong>Binary Search on Answer</strong>.</p>

<p>Instead of directly searching for the positions of the cows, binary search the <strong>minimum possible distance</strong> between two cows.</p>

<p><strong>Search Space:</strong></p>

<ul>
	<li>Minimum possible distance = <code>1</code></li>
	<li>Maximum possible distance = <code>max(arr) - min(arr)</code></li>
</ul>

<p>For every possible distance <code>mid</code>, check whether it is possible to place <code>k</code> cows such that every two consecutive cows have at least <code>mid</code> distance between them.</p>

<p><strong>Greedy Check:</strong></p>

<ol>
	<li>Sort the stall positions.</li>
	<li>Place the first cow at the first stall.</li>
	<li>For every subsequent stall, if the distance from the last placed cow is at least <code>mid</code>, place another cow.</li>
	<li>If at least <code>k</code> cows can be placed, then <code>mid</code> is possible.</li>
	<li>Try a larger distance.</li>
	<li>Otherwise, try a smaller distance.</li>
</ol>

<p><strong>Binary Search Logic:</strong></p>

<pre>
If distance is possible:
    try a larger distance
    low = mid + 1

If distance is not possible:
    try a smaller distance
    high = mid - 1

At the end:
    high represents the maximum possible minimum distance.
</pre>

<p>&nbsp;</p>

<p><strong>Complexity:</strong></p>

<ul>
	<li>Sorting: <code>O(n log n)</code></li>
	<li>Each feasibility check: <code>O(n)</code></li>
	<li>Binary Search: <code>O(log(max(arr) - min(arr)))</code></li>
	<li>Overall: <code>O(n log n + n log(max(arr) - min(arr)))</code></li>
	<li>Space: <code>O(1)</code> excluding the space used by the sorting algorithm.</li>
</ul>