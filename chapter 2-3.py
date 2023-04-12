n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(n)]

best_card = []

for card in cards:
    minimum_card = min(card)
    best_card.append(minimum_card)

print(max(best_card))
