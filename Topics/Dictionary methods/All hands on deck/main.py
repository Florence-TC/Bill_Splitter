card_ranks = {'2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              '10': 10,
              'Jack': 11,
              'Queen': 12,
              'King': 13,
              'Ace': 14}

total_value = 0
for _ in range(6):
    total_value += card_ranks[input()]

print(total_value / 6)
