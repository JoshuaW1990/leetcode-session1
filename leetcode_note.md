# leetcode_node


## Number of Digit One

There are two different solutions: Dynamic Programming and Maths.

Dynamic Programming:

Use a table named `ones`, `ones[x]` represents the number of `1` in the range `[0, 10^x)`. We traversal from the highest digit to the lowest digit of the number `n`.

Claim that the number on the right side of the current digit `digit` is `n`, and `size` is the number of current digits, `cnt` is the number of `1`.

- If `digit > 1`, then `cnt += digit * ones[size - 1] + 10 ^ (size - 1)`.
- If `digit = 1`, then `cnt += n + ones[size - 1] + 1`

code:

```python
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        # initialize ones
        ones, x = [0], 0
        while 10 ** x <= 0x7FFFFFFF:
            ones.append(ones[x] * 10 + 10 ** x)
            x += 1
        cnt, size = 0, len(str(n))
        for digit in str(n):
            digit = int(digit)
            size -= 1
            n -= digit * 10 ** size
            if digit > 1:
                cnt += digit * ones[size] + 10 ** size
            elif digit == 1:
                cnt += n + ones[size] + 1
        return cnt
```

Maths: https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python

Go through all the digits by using the position multiplier `m`, where `m` is `1`, `10`, `100`, ...

Claim the current digit determined by `m` is `curn`, then the higher part will be `n / m` and the lower part will be `n % m`, `curn` will be `n/m%10`. According to the current digit `curn` is `0`, `1`, or `>=2`, there might be three different situations (`ones` is the number of 1):

- If `curn = 0`, then `ones = (n/m + 8) / 10 * m`
- If `curn = 1`, then `ones = (n/m + 8) / 10 * m + (n % m + 1)`
- If `curn >= 2`, then `ones = (n/m + 8) / 10 * m`

```python
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones
```
