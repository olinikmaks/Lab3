import NemAll_Python_Geometry as geo
import NemAll_Python_BaseElements as base
import NemAll_Python_BasisElements as basis
from maxlab3addition import *


class EditBeam:

    def __init__(self, doc):
        self.model_ele_list = []
        self.handle_list = []
        self.document = doc

    # union of all parts
    def create(self, build_ele):
        self.beam_upper_part(build_ele)
        self.beam_lower_part(build_ele)
        return (self.model_ele_list, self.handle_list)

    def beam_upper_part(self, build_ele):
        s = base.CommonProperties()
        s.GetGlobalProperties()
        s.Pen = 1
        s.Color = 3
        s.Stroke = 1
        lower = self.beam_lower_part(build_ele)
        middle = self.beam_middle_part(build_ele)
        upper = self.top_part(build_ele)
        e, f = geo.MakeUnion(lower, middle)
        e, f = geo.MakeUnion(f, upper)
        self.model_ele_list.append(
            basis.ModelElement3D(s, f))

    def beam_lower_part(self, build_ele):
        f = addition_bottom_part_1(build_ele)
        e, f = geo.MakeUnion(f, addition_bottom_part_2(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_3(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_4(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_2_2(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_3_2(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_4_2(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_2_3(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_3_3(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_2_4(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_3_4(build_ele))
        e, f = geo.MakeUnion(f, addition_bottom_part_end(build_ele))
        return f

    def top_part(self, build_ele):
        sign = (build_ele.len.value - build_ele.cenw.value)
        f = addition_top_part_1(build_ele)
        e, f = geo.MakeUnion(f, addition_top_part_3(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_2(build_ele))
        e, f = geo.MakeUnion(
            f, addition_top_part_3(build_ele, sign=sign))
        e, f = geo.MakeUnion(f, addition_top_part_4(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_2_2(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_4(
            build_ele, build_ele.widb.value - build_ele.sectionbb.value * 2, build_ele.wit.value, 10))
        e, f = geo.MakeUnion(f, addition_top_part_2_3(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_4_2(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_4_2(
            build_ele, build_ele.widb.value - build_ele.sectionbb.value * 2, build_ele.wit.value, 10))
        e, f = geo.MakeUnion(f, addition_top_part_3_3(build_ele))
        e, f = geo.MakeUnion(f, addition_top_part_5(build_ele))
        return f

    def beam_middle_part(self, build_ele):
        data = self.get_interface_data(build_ele)
        polil = geo.Polygon3D()
        polil += geo.Point3D(0, data[0], data[1])
        polil += geo.Point3D(0, data[2] - data[0], data[1])
        polil += geo.Point3D(data[3], data[2] - data[0], data[1])
        polil += geo.Point3D(data[3] + data[4], data[2] -
                             data[0] - (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        polil += geo.Point3D(data[6] - (data[3] + data[4]),
                             data[2] - data[0] - (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        polil += geo.Point3D(data[6] - data[3], data[2] - data[0], data[1])
        polil += geo.Point3D(data[6], data[2] - data[0], data[1])
        polil += geo.Point3D(data[6], data[0], data[1])
        polil += geo.Point3D(data[6] - data[3], data[0], data[1])
        polil += geo.Point3D(data[6] - data[3] - data[4],
                             data[0] + (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        polil += geo.Point3D(data[3] + data[4],
                             data[0] + (data[2] - data[0] * 2 - data[5]) / 2, data[1])
        polil += geo.Point3D(data[3], data[0], data[1])
        polil += geo.Point3D(0, data[0], data[1])

        direction = geo.Polyline3D()
        direction += geo.Point3D(0, data[0], data[1])
        direction += geo.Point3D(0, data[0], data[1] + build_ele.cenhe.value)

        e, f = geo.CreatePolyhedron(polil, direction)
        return f

    def get_interface_data(self, build_ele):
        cenw = build_ele.cenw.value
        widb = build_ele.widb.value
        sectionbb = build_ele.sectionbb.value
        cenwi = build_ele.cenwi.value
        heb = build_ele.heb.value
        cenhe = build_ele.cenhe.value
        wit = build_ele.wit.value
        ths = build_ele.ths.value
        len = build_ele.len.value
        tent = build_ele.tent.value
        inte = build_ele.inte.value
        return [cenw, widb, sectionbb, cenwi, heb, cenhe, wit, ths, len, tent, inte]


def check_allplan_version(build_ele, version):
    del build_ele
    del version
    return True


def create_element(build_ele, doc):
    el = EditBeam(doc)
    return el.create(build_ele)
