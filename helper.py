from manim import *


def points_to_bezier_curve(points):
    obj = Circle()
    obj.set_points_smoothly(points)
    return obj
