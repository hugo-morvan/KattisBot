
    def vis_perc(buildings):
        buildings = [(x_2-x_1, y_2-y_1) for x_1, y_1, x_2, y_2 in buildings]
        max_val = 0
        for i in range(len(buildings)):
            for j in range(i + 1, len(buildings)):
                minx = max(buildings[i][0], buildings[j][0])
                maxx = min(buildings[i][0]+buildings[i][1], buildings[j][0]+buildings[j][1])
                miny = max(buildings[i][1], buildings[j][1])
                maxy = min(buildings[i][1]+buildings[i][0], buildings[j][1]+buildings[j][0])
                if minx <= maxx and miny <= maxy:
                    max_val = max(max_val, (minx + maxx - max(buildings[i][0], buildings[j][0])) / (buildings[i][0] + buildings[j][0]))
        return max_val

# Generator time: 7.7840 seconds