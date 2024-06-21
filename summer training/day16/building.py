#input:[3,5,9,6,8,10]
#output:from lift side sun will fall on 3,5,9,10 and from right side it has only sun fall on 10def find_buildings_with_sunlight(heights):
arr = [2, 5, 2, 3, 6, 7, 1, 0, 5, 7]
sunrise=0
max_mrng=0
for height in arr:
    if height>max_mrng:
        sunrise+=1
        max_mrng=height
sunset=0
max_evng=0
for height in reversed(arr):
    if height>max_evng:
        sunset+=1
        max_evng=height
print(sunrise)
print(sunset)