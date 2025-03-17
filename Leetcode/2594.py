ranks = [1,1,3,3]
cars = 74

left, right = 1, min(ranks) * cars * cars

def can_repair(time):
    total_repaired = 0
    for rank in ranks:
        repaired_cars = int((time/rank) ** 0.5)
        total_repaired += repaired_cars
    if total_repaired >= cars:
        return True
    return False

while left < right:
    mid = left + (right - left) // 2
    if can_repair(mid):
        right = mid
    else:
        left = mid + 1

print(left)

