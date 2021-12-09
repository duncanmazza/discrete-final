import manim
import numpy as np
from manim import Scene, Axes, Write, Create, FadeIn, BLUE, RED, VGroup, Dot, ReplacementTransform, FadeOut
from manim.utils.file_ops import open_file as open_media_file

from functions import *


class Convexity1D(Scene):

    def construct(self):
        axes_white = Axes((-5, 5), (-3, 5), axis_config={"color": manim.WHITE})
        self.play(Write(axes_white, lag_ratio=0.01, run_time=1))

        x_2 = axes_white.plot(
            parabola_default,
            color=BLUE
        )
        self.play(
            Create(x_2, run_time=3)
        )

        dot_group = VGroup()
        dot = Dot(color=RED)
        dot.move_to(axes_white.c2p(0, 0))
        dots_x = np.arange(-5, 5, 1)
        dots_midpoint = len(dots_x) // 2
        dots_y = parabola_default(dots_x)
        for i in range(len(dots_y)):
            new_dot = Dot(color=RED)
            new_dot.move_to(axes_white.c2p(dots_x[i], dots_y[i]))
            dot_group.add(new_dot)
        tex = manim.Tex(r"$f : \mathbb{Z} \to \mathbb{R}$", color=manim.RED)
        tex.move_to(manim.RIGHT * (-4) + manim.DOWN * 2.5)
        self.play(
            FadeIn(dot_group, scale=0.5),
            FadeIn(tex)
        )
        self.play(
            manim.Wait()
        )

        axes_gray = Axes((-5, 5), (-3, 5), axis_config={"color": manim.GRAY})
        self.play(
            FadeOut(x_2),
            ReplacementTransform(axes_white, axes_gray),
        )

        int_line_prev = None
        int_line_intersections_prev = None
        for midpoint_offsets in [(-1, 3), (-4, 4), (-4, 2)]:
            int_line_x_left = dots_midpoint + midpoint_offsets[0]
            int_line_x_right = dots_midpoint + midpoint_offsets[1]

            int_line_start = dot_group[int_line_x_left].get_center()
            int_line_end = dot_group[int_line_x_right].get_center()
            int_line = manim.Line(int_line_start, int_line_end, color=manim.GREEN)
            int_line_slope = (int_line_end[1] - int_line_start[1]) / (int_line_end[0] - int_line_start[0])
            int_line_intercept = int_line_end[1] - int_line_slope * int_line_end[0]
            int_lines_x_inbetween = np.arange(int_line_x_left + 1, int_line_x_right, 1)
            int_line_intersections = []
            for i in int_lines_x_inbetween:
                dot_center = dot_group[i].get_center()
                dashed_line_end = (dot_center[0], dot_center[0] * int_line_slope + int_line_intercept, 0)
                int_line_intersections.append(manim.DashedLine(dot_center, dashed_line_end, color=manim.GREEN))

            if int_line_prev is None and int_line_intersections_prev is None:
                self.play(
                    Create(int_line),
                    *[Create(l) for l in int_line_intersections]
                )
            else:
                self.play(
                    *[manim.Uncreate(l) for l in int_line_intersections_prev]
                )
                self.play(
                    ReplacementTransform(int_line_prev, int_line),
                    *[Create(l) for l in int_line_intersections],
                )
            self.play(
                manim.Wait()
            )
            int_line_prev = int_line
            int_line_intersections_prev = list(int_line_intersections)


if __name__ == "__main__":
    scene = Convexity1D()
    scene.render()
    open_media_file(scene.renderer.file_writer.movie_file_path)
