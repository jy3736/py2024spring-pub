### List Interleaving

Create a Python function that merges two lists of the same length by alternating their elements. The function should work with lists of any data type, interlacing them into a new list. For instance, combining `[a, b, c]` and `[1, 2, 3]` should yield `[a, 1, b, 2, c, 3]`.

**Input Requirements:**

- Two parameters: `list1` and `list2`. Both are lists of equal length, containing elements that can be of any data type.

**Output Requirements:**

- A list containing the elements of `list1` and `list2` interleaved, starting with the first element of `list1`.

**Sample Solution:**

```python
def interleave_lists(list1, list2):
    # replace pass with your solution
    pass

if __name__ == '__main__':
    list1 = input("Enter elements of the first list separated by spaces: ").split()
    list2 = input("Enter elements of the second list separated by spaces: ").split()
    print(interleave_lists(list1, list2))
```