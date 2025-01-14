def glyph_recognition(sample_points):
    n = len(sample_points)
    inner = []
    outer = []
    for i in range(n):
        if sample_points[i][0] == 0 and sample_points[i][1] == 0:
            continue
        else:
            inner.append((-sample_points[i][0], -sample_points[i][1]))
            outer.append(sample_points[i])
    if len(inner) == 1:
        score = 1
    else:
        p1 = inner[0]
        p2 = inner[-1]
        area_inner = abs((p1[0] * p2[1] - p1[1] * p2[0])) / 2
        p1 = outer[0]
        p2 = outer[-1]
        area_outer = abs((p1[0] * p2[1] - p1[1] * p2[0])) / 2
        score = area_inner / area_outer
    return score

if __name__ == "__main__":
    input_num = int(input())
    for _ in range(input_num):
        sample_points = []
        for _ in range(int(input())):
            x, y = map(float, input().split(" "))
            sample_points.append((x,y))
        print(glyph_recognition(sample_points))
# Generator time: 9.8928 seconds