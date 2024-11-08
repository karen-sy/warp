import numpy as np

import warp as wp

wp.clear_kernel_cache()
# wp.init()

num_points = 1024


@wp.kernel
def length(points: wp.array(dtype=wp.vec3), lengths: wp.array(dtype=float)):
    # thread index
    tid = wp.tid()

    # compute distance of each point from origin
    lengths[tid] = wp.length(points[tid])


# allocate an array of 3d points
points = wp.array(np.random.rand(num_points, 3), dtype=wp.vec3)
lengths = wp.zeros(num_points, dtype=float)

# launch kernel
wp.launch(kernel=length, dim=len(points), inputs=[points, lengths])

np_lengths = np.linalg.norm(points.numpy(), 2, axis=-1)

assert np.allclose(
    lengths.numpy(), np_lengths
), f"Numpy and Warp outputs do not match: {lengths.numpy()} vs {np_lengths}"
print("Sanity check completed successfully.")
