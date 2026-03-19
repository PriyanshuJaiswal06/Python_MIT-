heights = [1,1,4,2,1,3]
count = 0
expected = heights
expected.sort()
for i in range(len(heights)):
    if  expected[i] != heights[i]:
        count += 1
print(count)
print(expected)

print("Just something to push to save the streak ")