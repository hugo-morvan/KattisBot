def find_min_vertices(N, A, K, sightings):
    from scipy.spatial import ConvexHull

    # Find the convex hull of all points including both forest vertices and sightings
    all_points = A + [sightings]
    hull = ConvexHull(all_points)

    # The convex hull indices include all original vertices plus any additional points
    hull_indices = set(hull.vertices)

    # Filter out the original forest vertices that are not part of the convex hull
    min_vertices = [vertex for vertex in A if vertex in hull_indices]

    # The number of minimum vertices is the size of the filtered list
    return len(min_vertices)

# Read input
N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
K = int(input())
sightings = [tuple(map(int, input().split())) for _ in range(K)]

# Calculate and print the result
result = find_min_vertices(N, A, K, sightings)
print(result)
# Generator time: 7.6554 seconds