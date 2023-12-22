# Binary Search

This algorithm is used to find a value in a **sorted** array by repeatedly dividing the search interval in half. The idea is to begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

## Complexity

### Time Complexity

`O(log n)` - since we are dividing the array in half every time.

Consider the following example: let's say the size of the array is `n = 8`. 

The initial size of the search interval will be `8`. After the first iteration, the size of the search interval will be `4`. After the second iteration, the size of the search interval will be `2`. After the third iteration, the size of the search interval will be `1`. 

This means that we have either found the value or the value does not exist in the array.

So, the maximum number of iterations that the algorithm will do is `3` or `log 8`.

#### Refresher on Logarithms

A logarithm is the power to which a number must be raised in order to get some other number. For example, the base `2` logarithm of `4` is equal to `2`, because `2` raised to the power of `2` is `4`:

```
log2(4) = 2
```

In this case, we are interested in the base `2` logarithm, because we are dividing the array in half every time.

---
**NOTE**

When analyzing the time complexity of an algorithm, the base of the logarithm doesn't matter. The reason is that logarithms with different bases are related by a constant factor.

The most common bases used in algorithmic analysis are base 2 and base 10. The logarithmic time complexity is typically denoted as `O(log n)`, where n is the size of the input. Whether the logarithm is base 2 or base 10 doesn't affect the big-O notation because logarithms of different bases are proportional to each other by a constant factor.

In the context of algorithmic analysis, the constant factor introduced by the base of the logarithm is usually ignored because big-O notation focuses on the growth rate of the function as the input size approaches infinity. The growth rate remains the same regardless of the base of the logarithm, so it doesn't impact the classification of the algorithm's efficiency.

---