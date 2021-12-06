#!/usr/bin/env python
from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class DiscreteNewGraph(Scene):
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

        # x_4_label.shift(RIGHT*5 + UP*3)

        # x_4_label.shift(RIGHT)

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
            ShowCreation(x_2),
            FadeIn(x_2_label),
            FadeIn(dot_group, scale=0.5),
        )

        x_2_label.shift(RIGHT)

        # def move_dots(dots):
        #     for dot in dots:
        #         x = dot[0]
        #         dot[1].generate_target(use_deepcopy=True)
        #         dot[1].target = axes.c2p(x, (x-1)*(x-1)*(x+1)*(x+1))


        # move_dots(dots)

        dots2 = []
        dot_group2 = VGroup()

        for i in range(-5,5):
            new_dot = Dot(color=RED)
            new_dot.move_to(axes.c2p(i, (i-1)*(i-1)*(i+1)*(i+1)))
            dot_group2.add(new_dot)
            dots2.append((i, new_dot))

        
        self.play(
            # dot.animate.move_to(axes.c2p(0,1)),
            ReplacementTransform(x_2, x_4),
            FadeOut(x_2_label),
            FadeIn(x_4_label),
            ReplacementTransform(dot_group, dot_group2),)
            # MoveToTarget(dot_group))
        
        
        # self.wait(2)


        

        # x_4_label.shift(RIGHT)

                    #FadeTransform(x_2_label, x_4_label, shift = DOWN),


        # # Axes.get_graph will return the graph of a function
        # sin_graph = axes.get_graph(
        #     lambda x: 2 * math.sin(x),
        #     color=BLUE,
        # )
        # # By default, it draws it so as to somewhat smoothly interpolate
        # # between sampled points (x, f(x)).  If the graph is meant to have
        # # a corner, though, you can set use_smoothing to False
        # relu_graph = axes.get_graph(
        #     lambda x: max(x, 0),
        #     use_smoothing=False,
        #     color=YELLOW,
        # )
        # # For discontinuous functions, you can specify the point of
        # # discontinuity so that it does not try to draw over the gap.
        # step_graph = axes.get_graph(
        #     lambda x: 2.0 if x > 3 else 1.0,
        #     discontinuities=[3],
        #     color=GREEN,
        # )

        # # Axes.get_graph_label takes in either a string or a mobject.
        # # If it's a string, it treats it as a LaTeX expression.  By default
        # # it places the label next to the graph near the right side, and
        # # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        # relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        # step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        # self.play(
        #     ShowCreation(sin_graph),
        #     FadeIn(sin_label, RIGHT),
        # )
        # self.wait(2)
        # self.play(
        #     ReplacementTransform(sin_graph, relu_graph),
        #     FadeTransform(sin_label, relu_label),
        # )
        # self.wait()
        # self.play(
        #     ReplacementTransform(relu_graph, step_graph),
        #     FadeTransform(relu_label, step_label),
        # )
        # self.wait()

        # parabola = axes.get_graph(lambda x: 0.25 * x**2)
        # parabola.set_stroke(BLUE)
        # self.play(
        #     FadeOut(step_graph),
        #     FadeOut(step_label),
        #     ShowCreation(parabola)
        # )
        # self.wait()

        # # You can use axes.input_to_graph_point, abbreviated
        # # to axes.i2gp, to find a particular point on a graph
        # dot = Dot(color=RED)
        # dot.move_to(axes.i2gp(2, parabola))
        # self.play(FadeIn(dot, scale=0.5))

        # # A value tracker lets us animate a parameter, usually
        # # with the intent of having other mobjects update based
        # # on the parameter
        # x_tracker = ValueTracker(2)
        # f_always(
        #     dot.move_to,
        #     lambda: axes.i2gp(x_tracker.get_value(), parabola)
        # )

        # self.play(x_tracker.animate.set_value(4), run_time=3)
        # self.play(x_tracker.animate.set_value(-2), run_time=3)
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
            ShowCreation(x_2),
            FadeIn(x_2_label),
        )

        # x_2_label.shift(RIGHT)

        self.wait(2)
        self.play(
            ReplacementTransform(x_2, x_4),
            FadeOut(x_2_label),
            FadeIn(x_4_label),
        )
        # x_4_label.shift(RIGHT)

                    #FadeTransform(x_2_label, x_4_label, shift = DOWN),


        # # Axes.get_graph will return the graph of a function
        # sin_graph = axes.get_graph(
        #     lambda x: 2 * math.sin(x),
        #     color=BLUE,
        # )
        # # By default, it draws it so as to somewhat smoothly interpolate
        # # between sampled points (x, f(x)).  If the graph is meant to have
        # # a corner, though, you can set use_smoothing to False
        # relu_graph = axes.get_graph(
        #     lambda x: max(x, 0),
        #     use_smoothing=False,
        #     color=YELLOW,
        # )
        # # For discontinuous functions, you can specify the point of
        # # discontinuity so that it does not try to draw over the gap.
        # step_graph = axes.get_graph(
        #     lambda x: 2.0 if x > 3 else 1.0,
        #     discontinuities=[3],
        #     color=GREEN,
        # )

        # # Axes.get_graph_label takes in either a string or a mobject.
        # # If it's a string, it treats it as a LaTeX expression.  By default
        # # it places the label next to the graph near the right side, and
        # # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        # relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        # step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        # self.play(
        #     ShowCreation(sin_graph),
        #     FadeIn(sin_label, RIGHT),
        # )
        # self.wait(2)
        # self.play(
        #     ReplacementTransform(sin_graph, relu_graph),
        #     FadeTransform(sin_label, relu_label),
        # )
        # self.wait()
        # self.play(
        #     ReplacementTransform(relu_graph, step_graph),
        #     FadeTransform(relu_label, step_label),
        # )
        # self.wait()

        # parabola = axes.get_graph(lambda x: 0.25 * x**2)
        # parabola.set_stroke(BLUE)
        # self.play(
        #     FadeOut(step_graph),
        #     FadeOut(step_label),
        #     ShowCreation(parabola)
        # )
        # self.wait()

        # # You can use axes.input_to_graph_point, abbreviated
        # # to axes.i2gp, to find a particular point on a graph
        # dot = Dot(color=RED)
        # dot.move_to(axes.i2gp(2, parabola))
        # self.play(FadeIn(dot, scale=0.5))

        # # A value tracker lets us animate a parameter, usually
        # # with the intent of having other mobjects update based
        # # on the parameter
        # x_tracker = ValueTracker(2)
        # f_always(
        #     dot.move_to,
        #     lambda: axes.i2gp(x_tracker.get_value(), parabola)
        # )

        # self.play(x_tracker.animate.set_value(4), run_time=3)
        # self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


