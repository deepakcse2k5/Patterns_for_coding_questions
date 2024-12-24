def sort_color(colors):
    if len(colors)==0:
        return []
    start, current = 0, 0
    end = len(colors) - 1
    while current < end :
        if colors[current] ==1:
            current+=1
        elif colors[current] == 0:
            colors[start], colors[current] = colors[current] , colors[start]
            start+=1
            current+=1
        elif colors[current] ==2:
            colors[current], colors[end] = colors[end], colors[current]
            end -=1
    return colors


print(sort_color(colors=[1,0,1,0,2,1,0]))
            

