import random
import timeit


def generate_random_list(size, bound):
    """Create a list of 'size' floating point numbers in the range [-bound, bound]"""
    return [random.uniform(-bound, bound) for _ in range(size)]


def update_coords(xs, ys, zs, vx, vy, vz):
    """Update position by velocity, one time-step"""
    for i in range(len(xs)):
        xs[i] = xs[i] + vx[i]
        ys[i] = ys[i] + vy[i]
        zs[i] = zs[i] + vz[i]


def update_locations(size, iters):
    """Main"""
    random.seed(size)
    xs = generate_random_list(size, 1000.)
    ys = generate_random_list(size, 1000.)
    zs = generate_random_list(size, 1000.)
    vx = generate_random_list(size, 1.)
    vy = generate_random_list(size, 1.)
    vz = generate_random_list(size, 1.)
    t = timeit.timeit(stmt=f"update_coords({xs}, {ys}, {zs}, {vx}, {vy}, {vz})",
                      setup="from update_locations import update_coords",
                      number=iters)
    return 1000000 * t / (size * iters)
