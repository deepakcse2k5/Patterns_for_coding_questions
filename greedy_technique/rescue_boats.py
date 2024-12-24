people = [3,4,5,3,4]
limit = 6

def rescue_boats(people, limit):

    people.sort()

    left, right = 0, len(people) -1

    boat = 0

    while left < right:
        if people[left] + people[right] <= limit:
            left +=1
        right -=1
        boat+=1
    return boat

print(rescue_boats(people, limit))

# Time Complexity - O(nlogn)
# Space Complexity - O(n)

