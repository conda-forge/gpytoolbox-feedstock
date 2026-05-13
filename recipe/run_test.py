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
