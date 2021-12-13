#!/usr/bin/env python
from manim import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

# class TangentLineExample(Scene):
#     def construct(self):
#         circle = Circle(radius=2)
#         line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
#         line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
#         self.add(circle, line_1, line_2)





class TangentLineGraph(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-1, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.get_graph(
            lambda x: x*x,
            color = BLUE
        )

        x_4 = axes.get_graph(
            lambda x: (x-1)*(x-1)*(x+1)*(x+1),
            color = BLUE
        )
        x_2_label = axes.get_graph_label(x_2, "x^2")

        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))


        self.play(
            Create(x_4),
            # FadeIn(x_2_label),
        )

        alpha = ValueTracker(.45)

        draw_tangent = (lambda: 
            TangentLine(x_4, alpha.get_value(), 5, color=WHITE))

        tangent = always_redraw(draw_tangent)  

        self.play(Create(tangent))

        self.play(alpha.animate.set_value(.55), run_time = 10, rate_func=rate_functions.linear)

        self.wait()


class DiscreteNewGraph(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-1, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.get_graph(
            lambda x: x*x,
            color = BLUE
        )

        x_4 = axes.get_graph(
            lambda x: (x-1)*(x-1)*(x+1)*(x+1),
            color = BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "x^2")
        x_4_label = axes.get_graph_label(x_4, "(x-1)^2 (x+1)^2")


        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))

        dots = []
        dot_group = VGroup()

        for i in range(-5,5):
            new_dot = Dot(color=RED)
            new_dot.move_to(axes.c2p(i, i*i))
            dot_group.add(new_dot)
            dots.append((i, new_dot))



        self.play(
            Create(x_2),
            FadeIn(x_2_label),
            FadeIn(dot_group, scale=0.5),
        )

        x_2_label.shift(RIGHT)


        dots2 = []
        dot_group2 = VGroup()

        for i in range(-5,5):
            new_dot = Dot(color=RED)
            new_dot.move_to(axes.c2p(i, (i-1)*(i-1)*(i+1)*(i+1)))
            dot_group2.add(new_dot)
            dots2.append((i, new_dot))

        
        self.play(
            ReplacementTransform(x_2, x_4),
            FadeOut(x_2_label),
            FadeIn(x_4_label),
            ReplacementTransform(dot_group, dot_group2))
        self.wait()


class NewGraph(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-1, 5))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.get_graph(
            lambda x: x*x,
            color = BLUE
        )

        x_4 = axes.get_graph(
            lambda x: (x-1)*(x-1)*(x+1)*(x+1),
            color = BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "x^2")
        x_4_label = axes.get_graph_label(x_4, "(x-1)^2 (x+1)^2")

        x_4_label.shift(RIGHT*5 + UP*3)

        # x_4_label.shift(RIGHT)


        self.play(
            Create(x_2),
            FadeIn(x_2_label),
        )

        # x_2_label.shift(RIGHT)

        self.wait(2)
        self.play(
            ReplacementTransform(x_2, x_4),
            FadeOut(x_2_label),
            FadeIn(x_4_label),
        )
        self.wait()


