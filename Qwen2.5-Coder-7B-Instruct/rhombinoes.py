def max_rhombinoes(W, H, K, dead_triangles):
    live_triangles = [(x, y) for x in range(W) for y in range(H) if (x, y) not in dead_triangles]
    
    def is_valid_triangle(triangle):
        return triangle in live_triangles
    
    def can_place_rhombino(t1, t2):
        return is_valid_triangle(t1) and is_valid_triangle(t2) and (t1[0] == t2[0] or t1[1] == t2[1])
    
    def place_rhombino(t1, t2):
        live_triangles.remove(t1)
        live_triangles.remove(t2)
    
    rhombinoes = 0
    
    for i in range(len(live_triangles)):
        for j in range(i + 1, len(live_triangles)):
            if can_place_rhombino(live_triangles[i], live_triangles[j]):
                place_rhombino(live_triangles[i], live_triangles[j])
                rhombinoes += 1
                break
    
    return rhombinoes

W, H, K = map(int, input().split())
dead_triangles = [tuple(map(int, input().split())) for _ in range(K)]

print(max_rhombinoes(W, H, K, dead_triangles))
# Generator time: 9.6053 seconds