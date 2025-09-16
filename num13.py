count = 1

while True:
    bilet = input().strip()
    if len(bilet) % 2 == 0:
        
        first_half_sum = 0
        second_half_sum = 0
        half = len(bilet)//2
        
        for i in range(half):
            first_half_sum += int(bilet[i])
            
        for i in range(half, len(bilet)):
            second_half_sum += int(bilet[i])
            
        if first_half_sum == second_half_sum:
            print(count)
            break
            
    count += 1
