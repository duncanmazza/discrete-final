import math
from manim import *
from functions import parabola_3d


class Conv3D(ThreeDScene):
    parabola_range = 3
    axes_range = 6
    resolution_fa = 42

    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        axes = ThreeDAxes(
            x_range=(-Conv3D.axes_range, Conv3D.axes_range),
            y_range=(-Conv3D.axes_range, Conv3D.axes_range),
            color=GRAY
        )
        self.add(axes)

        parabola_surf_blue = Surface(
            parabola_3d,
            resolution=(Conv3D.resolution_fa, Conv3D.resolution_fa),
            v_range=[-Conv3D.parabola_range, +Conv3D.parabola_range],
            u_range=[-Conv3D.parabola_range, +Conv3D.parabola_range]
        )
        parabola_surf_blue.set_style(fill_opacity=1, stroke_color=BLUE)
        parabola_surf_blue.set_fill_by_checkerboard(BLUE_D, BLUE_E, opacity=0.5)
        self.play(
            Create(parabola_surf_blue)
        )

        self.wait(2)

        dots_dict = {}
        dots = VGroup()
        for u in range(-Conv3D.parabola_range, Conv3D.parabola_range + 1):
            for v in range(-Conv3D.parabola_range, Conv3D.parabola_range + 1):
                dot_coords = axes.coords_to_point(*parabola_3d(u, v))
                new_dot = Dot3D(dot_coords, color=RED)
                dots.add(new_dot)
                dots_dict[(u, v)] = new_dot

        map_comain_codomain_tex = Tex(r"$f : \mathbb{Z}^2 \to \mathbb{R}$", color=RED)
        map_comain_codomain_tex.to_corner(DL)
        self.add_fixed_in_frame_mobjects(map_comain_codomain_tex)

        parabola_surf_red = Surface(
            parabola_3d,
            resolution=(14, 14),
            v_range=[-Conv3D.parabola_range, +Conv3D.parabola_range],
            u_range=[-Conv3D.parabola_range, +Conv3D.parabola_range]
        )
        parabola_surf_red.set_style(fill_opacity=0.1, stroke_color=RED, stroke_opacity=0.3)
        parabola_surf_red.set_fill_by_checkerboard(RED, RED, opacity=0.1)

        self.play(
            FadeIn(dots),
            Write(map_comain_codomain_tex),
            ReplacementTransform(parabola_surf_blue, parabola_surf_red)
        )

        self.wait(3)

        # -------------------

        self.move_camera(phi=0, theta=0, run_time=3)

        l_conv_uvs = [(-1, -1), (1, 2)]
        l_conv_midpoint = (
                (l_conv_uvs[0][0] + l_conv_uvs[1][0]) / 2,
                (l_conv_uvs[0][1] + l_conv_uvs[1][1]) / 2,
        )
        l_conv_midpoint_int_c = (
            math.ceil(l_conv_midpoint[0]),
            math.ceil(l_conv_midpoint[1])
        )
        l_conv_midpoint_int_f = (
            math.floor(l_conv_midpoint[0]),
            math.floor(l_conv_midpoint[1])
        )

        dots_chosen = VGroup()
        for l_conv_uv in l_conv_uvs:
            dots_chosen.add(Dot3D(axes.coords_to_point(*parabola_3d(*l_conv_uv)), color=GREEN))

        dots_not_chosen_set = set(dots_dict.keys())
        dots_not_chosen_set -= set(l_conv_uvs)
        dots_not_chosen = VGroup()
        for dot_not_chosen_coord in dots_not_chosen_set:
            dots_not_chosen.add(dots_dict[dot_not_chosen_coord])

        self.play(
            FadeIn(dots_chosen),
            FadeOut(dots_not_chosen)
        )

        line_between = Line3D(start=dots_chosen[0], end=dots_chosen[1], color=GREEN)
        self.play(
            Create(line_between)
        )

        dot_midpoint = Dot3D(axes.coords_to_point(*parabola_3d(*l_conv_midpoint)), color=YELLOW)
        dot_midpoint_int_c_pre = Dot3D(dot_midpoint.get_center(), color=YELLOW)
        dot_midpoint_int_f_pre = Dot3D(dot_midpoint.get_center(), color=YELLOW)

        p01_floor_tex = "$\\lfloor (\\mathbf{p}_1 + \\mathbf{p}_2)/2 \\rfloor$"
        p01_ceil_tex = "$\\lceil (\\mathbf{p}_1 + \\mathbf{p}_2)/2 \\rceil$"
        p0_tex = "$\\mathbf{p}_0$"
        p1_tex = "$\\mathbf{p}_1$"

        l_conv_p0_tex = Tex(p0_tex, color=GREEN).next_to(dots_chosen[0], LEFT)
        l_conv_p1_tex = Tex(p1_tex, color=GREEN).next_to(dots_chosen[1], RIGHT)
        self.add_fixed_orientation_mobjects(l_conv_p0_tex, l_conv_p1_tex)

        self.play(
            FadeIn(
                dot_midpoint,
                dot_midpoint_int_c_pre,
                dot_midpoint_int_f_pre
            ),
            Write(l_conv_p0_tex),
            Write(l_conv_p1_tex)
        )

        self.wait(3)

        dot_midpoint_int_c = Dot3D(axes.coords_to_point(*parabola_3d(*l_conv_midpoint_int_c)), color=YELLOW)
        dot_midpoint_int_f = Dot3D(axes.coords_to_point(*parabola_3d(*l_conv_midpoint_int_f)), color=YELLOW)
        l_conv_midpoint_int_f_tex = Tex(p01_floor_tex, color=YELLOW)
        l_conv_midpoint_int_c_tex = Tex(p01_ceil_tex, color=YELLOW)
        self.add_fixed_orientation_mobjects(l_conv_midpoint_int_c_tex, l_conv_midpoint_int_f_tex)
        l_conv_midpoint_int_c_tex.next_to(dot_midpoint_int_c, UP * 7)
        l_conv_midpoint_int_f_tex.next_to(dot_midpoint_int_f, DOWN * 7)

        self.play(
            Transform(dot_midpoint_int_c_pre, dot_midpoint_int_c),
            Transform(dot_midpoint_int_f_pre, dot_midpoint_int_f),
            Write(l_conv_midpoint_int_c_tex),
            Write(l_conv_midpoint_int_f_tex),
            FadeOut(dot_midpoint),
            FadeOut(map_comain_codomain_tex),
        )

        self.wait(7)

        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES)

        self.wait(3)

        l_conv_definition_tex = Tex(
            "$f($", p0_tex, "$) + f($", p1_tex, "$) \\geq f( $", p01_floor_tex, "$) + f($", p01_ceil_tex, "$)$",
        ).to_corner(DL)
        l_conv_definition_tex.set_color_by_tex(p0_tex, GREEN)
        l_conv_definition_tex.set_color_by_tex(p1_tex, GREEN)
        l_conv_definition_tex.set_color_by_tex(p01_ceil_tex, YELLOW)
        l_conv_definition_tex.set_color_by_tex(p01_floor_tex, YELLOW)
        self.add_fixed_in_frame_mobjects(l_conv_definition_tex)

        self.play(
            Write(l_conv_definition_tex)
        )



if __name__ == "__main__":
    scene = Conv3D()
    scene.render(preview=True)






















