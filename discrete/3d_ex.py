"""
Miscellaneous code for learning how to use Manim.
"""

from manim import *


class ThreeDEx(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        axes = ThreeDAxes((-4, 4), (-4, 4))
        self.add(axes)

        d0 = Dot3D(axes.coords_to_point(*[0, 0, 0]), color=RED)
        d1 = Dot3D(axes.coords_to_point(*[2, 2, 2]), color=RED)

        self.add(d0, d1)

        l_conv_p0_tex = Tex(r"$\mathbf{p}_0$").next_to(d0, LEFT)
        l_conv_p1_tex = Tex(r"$\mathbf{p}_1$").next_to(d1, RIGHT)

        self.add_fixed_orientation_mobjects(l_conv_p0_tex, l_conv_p1_tex)

        self.play(
            Write(l_conv_p1_tex)
        )

        self.move_camera(0, 0)


if __name__ == "__main__":
    scene = ThreeDEx()
    scene.render(preview=True)
