import numpy as np

import gpytoolbox


vertices = np.array(
    [
        [-1.0, -1.0],
        [-1.0, 1.0],
        [1.0, 1.0],
        [1.0, -1.0],
    ]
)
edges = gpytoolbox.edge_indices(vertices.shape[0], closed=True)
sample_points = np.array([[0.3, 0.0], [1.2, 0.0]])

sqr_d, _, _ = gpytoolbox.squared_distance(
    sample_points,
    vertices,
    F=edges,
    use_cpp=True,
)

np.testing.assert_allclose(np.asarray(sqr_d).reshape(-1), [0.49, 0.04])

mesh_vertices = np.array(
    [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 0.0],
    ]
)
mesh_faces = np.array([[0, 1, 2], [0, 2, 3]], dtype=np.int32)
ray_origins = np.array([[0.25, 0.25, 1.0]])
ray_directions = np.array([[0.0, 0.0, -1.0]])
times, face_ids, barycentric = gpytoolbox.ray_mesh_intersect(
    ray_origins,
    ray_directions,
    mesh_vertices,
    mesh_faces,
)
np.testing.assert_allclose(times, [1.0])
assert face_ids[0] in (0, 1)
np.testing.assert_allclose(np.sum(barycentric, axis=1), [1.0])
