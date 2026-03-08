# AI-Augmented Task --- Pair Sum Analysis

## 1️⃣ Prompt Used

Write a Python function that finds all pairs in a list that sum to a
target number using list comprehensions.

------------------------------------------------------------------------

## 2️⃣ AI Generated Code

``` python
def find_pairs(nums, target):
    return [(nums[i], nums[j]) 
            for i in range(len(nums)) 
            for j in range(i+1, len(nums)) 
            if nums[i] + nums[j] == target]
```

------------------------------------------------------------------------

## 3️⃣ Testing the Code

### Test Case 1

``` python
print(find_pairs([1,2,3,4,5], 6))
```

Output: \[(1,5), (2,4)\]

### Test Case 2

``` python
print(find_pairs([1,1,1], 2))
```

Output: \[(1,1), (1,1), (1,1)\]

------------------------------------------------------------------------

## 4️⃣ Issues Found

**Duplicate Pairs**\
When the input list contains duplicate numbers, the function produces
repeated pairs such as `(1,1)` multiple times.

**Time Complexity**\
The algorithm checks every pair of elements in the list.

Time Complexity: **O(n²)**

------------------------------------------------------------------------

## 5️⃣ Improved Version (Avoid Duplicate Pairs)

``` python
def find_pairs(nums, target):
    pairs = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                pairs.add(pair)

    return list(pairs)
```

Example:

``` python
print(find_pairs([1,1,1], 2))
```

Output: \[(1,1)\]

------------------------------------------------------------------------

## 6️⃣ Optimal O(n) Solution Using Sets

``` python
def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))

        seen.add(num)

    return list(pairs)
```

Example:

``` python
print(find_pairs([1,2,3,4,5], 6))
```

Output: \[(1,5), (2,4)\]

------------------------------------------------------------------------

## 7️⃣ Improvements Explained

1.  **Removed Duplicate Pairs** using a set of tuples.
2.  **Handled duplicates correctly** by sorting the pair before adding
    it.
3.  **Improved performance** from O(n²) to **O(n)** using a set-based
    approach.

------------------------------------------------------------------------

## Conclusion

The AI-generated solution works for simple cases but produces duplicate
pairs when duplicate numbers exist.\
By improving the algorithm with sets, we removed duplicate pairs and
achieved a more efficient **O(n)** solution.
