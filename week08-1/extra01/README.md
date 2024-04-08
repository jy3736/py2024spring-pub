## Finding the Index of the Largest Element in a Sequence

Write a program that identifies the index of the largest integer in a given sequence of numbers. The sequence terminates when a 0 is encountered, signaling the end of input. Should there be more than one occurrence of the maximum value, the program should return the index of its first appearance.

### Python Solution (`main.py`)

```python
def find_index_of_max(sequence):
    # replace pass with your code
    pass

if __name__ == "__main__":
    sequence = list(map(int, input("Enter the sequence of numbers ending with 0: ").split()))
    print("The index of the largest element is:", find_index_of_max(sequence))
```