import NemAll_Python_Geometry as geo
from maxlab3beam import *


def addition_top_part_1(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1] - data[2] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[0], data[6] -
                     (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0], -(data[6] - data[1]) /
                     2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0], data[2] +
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[0], data[1] - data[2] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1] - data[2] -
                       (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    dir += geo.Point3D(data[8] - data[0], data[1] -
                       data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_top_part_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4] + data[5])
    p += geo.Point3D(data[8] - data[0] - data[9], data[1] -
                     data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2, data[1] - (
        data[1] - data[2] * 2 - data[3]) / 2 + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0] - (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4] + data[5])
    dir += geo.Point3D(data[8] - data[0] +
                       10, data[1] - data[2] - 10, data[4] + data[5] + 10)

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_top_part_3(build_ele, sign=0):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(sign, data[2], data[4] + data[5])
    p += geo.Point3D(sign, data[1] - data[2], data[4] + data[5])
    p += geo.Point3D(sign, data[1] +
                     (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(sign, -(data[6] - data[1]) /
                     2, data[4] + data[5] + data[7])
    p += geo.Point3D(sign, data[2], data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(sign, data[2], data[4] + data[5])
    dir += geo.Point3D(sign + data[0], data[2], data[4] + data[5])

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_top_part_4(build_ele, minus_1=0, minus_2=0, digit=-10):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[1] -
                     data[2] - minus_1, data[4] + data[5])
    p += geo.Point3D(data[8] - data[0], data[6] -
                     (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0] - (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] + (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0], data[1] -
                     data[2] - minus_1, data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0],
                       data[1] - data[2] - minus_1, data[4] + data[5])
    dir += geo.Point3D(data[8] - data[0],
                       data[1] - data[2] + digit - minus_1, data[4] + data[5])
    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_top_part_2_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[2], data[4] + data[5])
    p += geo.Point3D(data[8] - data[0] - data[9],
                     data[2] + (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2,
                     (data[1] - data[2] * 2 - data[3]) / 2 - (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0] - (data[1] - data[2] *
                                          2 - data[3]) / 2, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[8] - data[0],  data[2], data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[2], data[4] + data[5])
    dir += geo.Point3D(data[8] - data[0] +
                       10, data[2] + 10, data[4] + data[5] + 10)

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_top_part_2_3(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1] - data[2], data[4] + data[5])
    p += geo.Point3D(data[0] + data[9], data[1] -
                     data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2, data[1] - (
        data[1] - data[2] * 2 - data[3]) / 2 + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] + (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0], data[1] - data[2], data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1] - data[2], data[4] + data[5])
    dir += geo.Point3D(data[0] - 10,
                       data[1] - data[2] - 10, data[4] + data[5] - 10)
    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_top_part_4_2(build_ele, minus_1=0, minus_2=0, digit=-10):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1] - data[2] - minus_1, data[4] + data[5])
    p += geo.Point3D(data[0], data[1] + (data[6] - data[1]) /
                     2 - minus_2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] + (data[6] - data[1]) / 2 - minus_2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0], data[1] - data[2] - minus_1, data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1] - data[2] - minus_1, data[4] + data[5])
    dir += geo.Point3D(data[0], data[1] -
                       data[2] - minus_1 + digit, data[4] + data[5])

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_top_part_3_3(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[2], data[4] + data[5])
    p += geo.Point3D(data[0] + data[9], data[2] +
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] + data[5])
    p += geo.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                     (data[1] - data[2] * 2 - data[3]) / 2 - (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0] + (data[1] - data[2] * 2 - data[3]) /
                     2, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(data[0], data[2], data[4] + data[5])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[2], data[4] + data[5])
    dir += geo.Point3D(data[0] - 10, data[2] + 10, data[4] + data[5] - 10)

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_top_part_5(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(0, -(data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(0, data[6] - (data[6] - data[1]) /
                     2, data[4] + data[5] + data[7])
    p += geo.Point3D(0, data[6] - (data[6] - data[1]) /
                     2, data[4] + data[5] + data[7])
    p += geo.Point3D(0, data[6] - (data[6] - data[1]) /
                     2 - data[10], data[4] + data[5] + data[7])
    p += geo.Point3D(0, data[6] - (data[6] - data[1]) /
                     2 - data[10], data[4] + data[5] + data[7] + build_ele.hp.value)
    p += geo.Point3D(0, - (data[6] - data[1]) / 2 +
                     data[10], data[4] + data[5] + data[7] + build_ele.hp.value)
    p += geo.Point3D(0, - (data[6] - data[1]) /
                     2 + data[10], [4] + data[5] + data[7])
    p += geo.Point3D(0, - (data[6] - data[1]) / 2, data[4] + data[5] + data[7])
    p += geo.Point3D(0, -(data[6] - data[1]) / 2,  data[4] + data[5] + data[7])

    dir = geo.Polyline3D()
    dir += geo.Point3D(0, -(data[6] - data[1]) / 2,
                       data[4] + data[5] + data[7])
    dir += geo.Point3D(data[8], -(data[6] - data[1]) /
                       2, data[4] + data[5] + data[7])
    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_1(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1], data[4] - data[10])
    p += geo.Point3D(data[0], data[1] - data[2] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    p += geo.Point3D(data[0], data[1] - data[2] -
                     (data[1] - data[2] * 2 - data[3]) / 2 - data[3], data[4])
    p += geo.Point3D(data[0], 0, data[4] - data[10])
    p += geo.Point3D(data[0], data[1], data[4] - data[10])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1], data[4] - data[10])
    dir += geo.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1] - data[2], data[4])
    p += geo.Point3D(data[0] + data[9], data[1] -
                     data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    p += geo.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    p += geo.Point3D(data[0] + (data[1] - data[2]
                                * 2 - data[3]) / 2, data[1], data[4] - data[10])
    p += geo.Point3D(data[0], data[1] - data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1] - data[2], data[4])
    dir += geo.Point3D(data[0] - 10, data[1] - data[2] - 10, data[4] - 10)

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_bottom_part_3(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(0, data[1], data[4] - data[10])
    p += geo.Point3D(0, data[1] - data[2], data[4])
    p += geo.Point3D(0, data[2], data[4])
    p += geo.Point3D(0, 0, data[4] - data[10])
    p += geo.Point3D(0, data[1], data[4] - data[10])

    dir = geo.Polyline3D()
    dir += geo.Point3D(0, data[1], data[4] - data[10])
    dir += geo.Point3D(data[0], data[1], data[4] - data[10])

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_4(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[1] - data[2], data[4])
    p += geo.Point3D(data[0], data[1], data[4] - data[10])
    p += geo.Point3D(data[0] + (data[1] - data[2]
                                * 2 - data[3]) / 2, data[1], data[4] - data[10])
    p += geo.Point3D(data[0], data[1] - data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[1] - data[2], data[4])
    dir += geo.Point3D(data[0], data[1] - data[2] - 10, data[4])

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_bottom_part_2_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[2], data[4])
    p += geo.Point3D(data[0] + data[9], data[2] +
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    p += geo.Point3D(data[0] + data[9] + (data[1] - data[2] * 2 - data[3]) / 2,
                     (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    p += geo.Point3D(data[0] + (data[1] - data[2]
                                * 2 - data[3]) / 2, 0, data[4] - data[10])
    p += geo.Point3D(data[0], data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[2], data[4])
    dir += geo.Point3D(data[0] - 10, data[2] + 10, data[4] - 10)

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_3_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    p += geo.Point3D(data[8] - data[0], data[2], data[4])
    p += geo.Point3D(data[8] - data[0], 0, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[1], data[4] - data[10])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    dir += geo.Point3D(data[8], data[1], data[4] - data[10])

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_bottom_part_4_2(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[0], data[2], data[4])
    p += geo.Point3D(data[0], 0, data[4] - data[10])
    p += geo.Point3D(data[0] + (data[1] - data[2]
                                * 2 - data[3]) / 2, 0, data[4] - data[10])
    p += geo.Point3D(data[0], data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[0], data[2], data[4])
    dir += geo.Point3D(data[0], data[2] + 10, data[4])

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_bottom_part_2_3(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    p += geo.Point3D(data[8] - data[0] - data[9],
                     data[1] - data[2] - (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    p += geo.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2] * 2 - data[3]) / 2,
                     data[1] - (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[1], data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    dir += geo.Point3D(data[8] - data[0] +
                       10, data[1] - data[2] - 10, data[4] + 10)

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_3_3(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    p += geo.Point3D(data[8] - data[0], data[1], data[4] - data[10])
    p += geo.Point3D(data[8] - data[0] -
                     (data[1] - data[2] * 2 - data[3]) / 2, data[1], data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[1] - data[2], data[4])
    dir += geo.Point3D(data[8] - data[0], data[1] - data[2] - 10, data[4])

    e, f = geo.CreatePolyhedron(p, dir)
    return f


def addition_bottom_part_2_4(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[2], data[4])
    p += geo.Point3D(data[8] - data[0] - data[9],
                     data[2] + (data[1] - data[2] * 2 - data[3]) / 2, data[4])
    p += geo.Point3D(data[8] - data[0] - data[9] - (data[1] - data[2]
                                                    * 2 - data[3]) / 2, (data[1] - data[2] * 2 - data[3]) / 2, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0] -
                     (data[1] - data[2] * 2 - data[3]) / 2, 0, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[2], data[4])
    dir += geo.Point3D(data[8] - data[0] - 10, data[2] + 10, data[4] - 10)

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_3_4(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(data[8] - data[0], data[2], data[4])
    p += geo.Point3D(data[8] - data[0], 0, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0] -
                     (data[1] - data[2] * 2 - data[3]) / 2, 0, data[4] - data[10])
    p += geo.Point3D(data[8] - data[0], data[2], data[4])

    dir = geo.Polyline3D()
    dir += geo.Point3D(data[8] - data[0], data[2], data[4])
    dir += geo.Point3D(data[8] - build_ele.mew.value, data[2] + 10, data[4])

    e, f = geo.CreatePolyhedron(p, dir)

    return f


def addition_bottom_part_end(build_ele):
    data = EditBeam.get(build_ele)
    p = geo.Polygon3D()
    p += geo.Point3D(0, 20, 0)
    p += geo.Point3D(0, data[1] - 20, 0)
    p += geo.Point3D(0, data[1], 20)
    p += geo.Point3D(0, data[1], data[4] - data[10])
    p += geo.Point3D(0, 0, data[4] - data[10])
    p += geo.Point3D(0, 0, 20)
    p += geo.Point3D(0, 20, 0)

    dir = geo.Polyline3D()
    dir += geo.Point3D(0, 20, 0)
    dir += geo.Point3D(data[8], 20, 0)
    e, f = geo.CreatePolyhedron(p, dir)
    return f
