<h2><a href="https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1">Union and Intersection of Two Sorted Arrays</a></h2>
<h3>Easy</h3>
<hr>

<p>Given two sorted arrays <code>arr1[]</code> and <code>arr2[]</code> of sizes <code>n</code> and <code>m</code> respectively, find their <strong>Union</strong> and <strong>Intersection</strong>.</p>

<ul>
    <li><strong>Union:</strong> A sorted array containing all <strong>distinct</strong> elements present in either of the two arrays.</li>
    <li><strong>Intersection:</strong> A sorted array containing the elements that are present in <strong>both</strong> arrays.</li>
</ul>

<p><strong>Note:</strong></p>

<ul>
    <li>Both input arrays are sorted in non-decreasing order.</li>
    <li>The Union should contain only unique elements.</li>
    <li>The Intersection should contain the common elements of both arrays.</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]

<strong>Union:</strong>
[1, 2, 3, 4, 5]

<strong>Intersection:</strong>
[1, 2, 3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [2, 2, 3, 4, 5]
arr2 = [1, 1, 2, 3, 4]

<strong>Union:</strong>
[1, 2, 3, 4, 5]

<strong>Intersection:</strong>
[2, 3, 4]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [4, 5, 6, 7]
arr2 = [1, 5, 6, 8]

<strong>Union:</strong>
[1, 4, 5, 6, 7, 8]

<strong>Intersection:</strong>
[5, 6]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= arr1[i], arr2[i] &lt;= 10<sup>9</sup></li>
    <li>Both arrays are sorted in non-decreasing order.</li>
</ul>

<p><strong>Expected Time Complexity:</strong> <code>O(n + m)</code></p>

<p><strong>Expected Auxiliary Space:</strong> <code>O(1)</code> (excluding the output array)</p>