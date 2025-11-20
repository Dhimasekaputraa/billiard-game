import math
import numpy as np
import config


def distance_less_equal(p1, p2, dist):
    dist_diff = p1 - p2
    return (dist_diff[0] ** 2 + dist_diff[1] ** 2) <= dist ** 2


def ball_collision_check(ball1, ball2):
    return distance_less_equal(ball1.pos, ball2.pos, 2 * config.ball_radius) and \
           np.count_nonzero(np.concatenate((ball1.velocity, ball2.velocity))) > 0 and \
           np.dot(ball2.pos - ball1.pos, ball1.velocity - ball2.velocity) > 0


