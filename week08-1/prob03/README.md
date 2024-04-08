## Lost card

Imagine you have a complete set of cards numbered from 1 to N. However, one card has gone missing. You're provided with the numbers on the remaining cards, which are distinct integers within the range from 1 to N, excluding the missing card's number. Your task is to identify and return the number of the missing card.

### Python Solution (`main.py`):

```python
def find_missing_card(n, cards):
    # replace pass with your code
    pass

if __name__ == "__main__":
    # Example case: Given 5 cards with one missing
    n = 5
    cards = [1, 2, 4, 5]  # Missing card is 3
    print(find_missing_card(n, cards))  # Expected output: 3

    # Another example case
    n = 10
    cards = [1, 2, 3, 4, 6, 7, 8, 9, 10]  # Missing card is 5
    print(find_missing_card(n, cards))  # Expected output: 5
```