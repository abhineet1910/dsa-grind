<h2><a href="https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1">Union of Two Sorted Arrays</a></h2>
<h3>Easy</h3>
<hr>

<p>Given two sorted arrays <code>arr1[]</code> and <code>arr2[]</code> of sizes <code>n</code> and <code>m</code> respectively, return the <strong>union</strong> of the two arrays.</p>

<p>The union of two arrays is a sorted array containing all <strong>distinct</strong> elements that are present in either of the arrays.</p>

<p><strong>Note:</strong> The resulting array should not contain duplicate elements.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]

<strong>Output:</strong>
[1, 2, 3, 4, 5]

<strong>Explanation:</strong>
The union contains all unique elements present in both arrays.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [2, 2, 3, 4, 5]
arr2 = [1, 1, 2, 3, 4]

<strong>Output:</strong>
[1, 2, 3, 4, 5]

<strong>Explanation:</strong>
Duplicate elements are included only once in the union.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong>
arr1 = [4, 5, 6, 7]
arr2 = [1, 5, 6, 8]

<strong>Output:</strong>
[1, 4, 5, 6, 7, 8]
</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= arr1[i], arr2[i] &lt;= 10<sup>9</sup></li>
    <li>Both arrays are sorted in non-decreasing order.</li>
</ul>