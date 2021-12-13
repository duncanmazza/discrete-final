#!/usr/bin/env python
import math
from manim import *


class Lengendre1(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: np.e ** x,
            color=BLUE
        )

        x_ln = axes.plot(
            lambda x: x * (math.log(x, np.e) - 1),
            color=RED,
            x_range=[0.001, 5]
        )

        x_2_label = axes.get_graph_label(x_2, "e^x")

        intro_words = Tex("""
            Consider the convex function $e^x$
        """)
        intro_words.to_corner(UL)

        self.play(Write(intro_words))

        self.play(
            Create(x_2),
            Create(x_ln),
            FadeIn(x_2_label),
        )

        self.wait(2)

        next_words = Tex("""
            At every point $x$ \\\\ we can draw a tangent line from $(x, f(x))$ \\\\ to the point where it intercepts the y axis
        """, font_size=30)
        next_words.to_corner(UL)

        self.play(
            FadeTransform(intro_words, next_words)
        )

        self.wait(2)

        alpha = ValueTracker(-5)

        # -axes.slope_of_tangent(x=alpha.get_value(), graph=x_2)
        # axes.i2gp(alpha.get_value(), x_2)[1]

        draw_tangent = (lambda:
                        Line(
                            start=axes.i2gp(alpha.get_value(), x_2),
                            end=axes.coords_to_point(0,
                                                     -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                     0),
                            color=WHITE))

        draw_intercept = (lambda:
                          Dot(
                              point=axes.coords_to_point(0,
                                                         -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                         0),
                              color=RED))

        draw_point = (lambda:
                      Dot(
                          point=[axes.i2gp(alpha.get_value(), x_2)[0],
                                 axes.i2gp(alpha.get_value(), x_2)[1],
                                 0],
                          color=RED))

        draw_result = (lambda:
                       Dot(
                           point=axes.coords_to_point(np.e ** alpha.get_value(),
                                                      -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                      0),
                           color=RED))

        tangent = always_redraw(draw_tangent)
        intercept = always_redraw(draw_intercept)
        point = always_redraw(draw_point)
        result = always_redraw(draw_result)

        trace = TracedPath(result.get_center)

        self.add(tangent)
        self.add(intercept)
        self.add(point)
        self.add(result)
        self.add(trace)

        self.play(alpha.animate.set_value(5), run_time=10, rate_func=rate_functions.linear)

        self.wait()


class Lengendre2(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: np.e ** x,
            color=BLUE
        )

        # x_ln = axes.plot(
        #     lambda x: x*(math.log(x, np.e)-1),
        #     color = RED,
        #     x_range=[0.001, 5]
        # )

        x_2_label = axes.get_graph_label(x_2, "e^x")

        intro_words = Tex("""
            Consider the convex function $e^x$
        """)
        intro_words.to_corner(UL)

        self.play(Write(intro_words))

        self.play(
            Create(x_2),
            # Create(x_ln),
            FadeIn(x_2_label),
        )

        self.wait(2)

        words2 = Tex("""
            At every point $x$ \\\\ we can draw a tangent line from $(x, f(x))$ \\\\ to the point where it intercepts the y axis
        """, font_size=30)
        words2.to_corner(UL)

        self.play(
            FadeTransform(intro_words, words2)
        )

        self.wait(2)

        alpha = ValueTracker(-5)

        # -axes.slope_of_tangent(x=alpha.get_value(), graph=x_2)
        # axes.i2gp(alpha.get_value(), x_2)[1]

        draw_tangent = (lambda:
                        Line(
                            start=axes.i2gp(alpha.get_value(), x_2),
                            end=axes.coords_to_point(0,
                                                     -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                     0),
                            color=WHITE))

        draw_intercept = (lambda:
                          Dot(
                              point=axes.coords_to_point(0,
                                                         -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                         0),
                              color=RED))

        draw_point = (lambda:
                      Dot(
                          point=[axes.i2gp(alpha.get_value(), x_2)[0],
                                 axes.i2gp(alpha.get_value(), x_2)[1],
                                 0],
                          color=RED))

        draw_result = (lambda:
                       Dot(
                           point=axes.coords_to_point(np.e ** alpha.get_value(),
                                                      -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value(),
                                                      0),
                           color=RED))

        tangent = always_redraw(draw_tangent)
        intercept = always_redraw(draw_intercept)
        point = always_redraw(draw_point)
        result = always_redraw(draw_result)

        trace = TracedPath(result.get_center)

        self.add(tangent)
        self.add(intercept)
        self.add(point)

        self.play(alpha.animate.set_value(2), run_time=8, rate_func=rate_functions.linear)

        self.wait(3)

        # words3 = Tex("""
        #     Now consider the tangent line at x=1.25
        # """, font_size=30)
        # words3.to_corner(UL)

        # self.play(
        #     FadeTransform(words2, words3)
        # )

        words4 = Tex("""
            Now consider the tangent line at x=1.25 \\\\ The tangent has a slope of 3.49 \\\\ and a y intercept of -.87
        """, font_size=30)
        words4.to_corner(UL)

        # Tex("(0, ").scale(0.75).next_to(grid.c2p(1, 1, 0))

        self.play(
            FadeTransform(words2, words4),
            alpha.animate.set_value(1.25), run_time=1, rate_func=rate_functions.linear
        )

        # alpha.set_value(1.25)

        # line = Line(intercept.get_center(), point.get_center())

        # brace = Brace(line)
        # bracetext = brace.get_text("Horizontal distance")

        def dot_position(mobject):
            mobject[1].set_value(-np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value())
            mobject.next_to(intercept, LEFT + DOWN)

        def slope_position(mobject):
            mobject[1].set_value(np.e ** alpha.get_value())
            mobject.next_to(tangent, RIGHT / 2 + UP)

        # dot = Dot(RIGHT*3)
        label = VGroup(Text("intercept = ", font_size=35), DecimalNumber())
        label.arrange(RIGHT)
        label.add_updater(dot_position)
        label2 = VGroup(Text("slope = ", font_size=35), DecimalNumber())
        label2.arrange(RIGHT)
        label2.add_updater(slope_position)
        self.add(label, label2)

        # yinterceptlabel = MathTex("2+i").next_to(intercept, UR, 0.1)
        # self.add(yinterceptlabel)

        # self.play(FadeIn(yinterceptlabel))

        self.wait(7)

        words5 = Tex("""
            We can plot the point (3.49, -.52) which represents \\\\the y intercept of a tangent line\\\\ as a function of slope
        """, font_size=30)
        words5.to_corner(UL)

        # Tex("(0, ").scale(0.75).next_to(grid.c2p(1, 1, 0))

        self.play(
            FadeTransform(words4, words5),
            # alpha.animate.set_value(1.25), run_time = 1, rate_func=rate_functions.linear
        )

        def transformed_position(mobject):
            # mobject.set_value(np.e ** alpha.get_value())
            mobject.move_to(axes.c2p(np.e ** alpha.get_value(),
                                     -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value()))

        def transformed_position2(mobject):
            # mobject.set_value(np.e ** alpha.get_value())
            mobject = axes.get_lines_to_point(axes.c2p(np.e ** alpha.get_value(),
                                                       -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value()))

        dot_axes = Dot(axes.c2p(np.e ** alpha.get_value(),
                                -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value()),
                       color=GREEN)

        lines = always_redraw(lambda: axes.get_lines_to_point(axes.c2p(np.e ** alpha.get_value(),
                                                                       -np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value())))

        # lines =

        def label3_position(mobject):
            mobject[1].set_value(np.e ** alpha.get_value())
            mobject[3].set_value(-np.e ** alpha.get_value() * alpha.get_value() + np.e ** alpha.get_value())
            mobject.next_to(dot_axes, DOWN)

        label3 = VGroup(Text("(", font_size=35, should_center=False), DecimalNumber(),
                        Text(", ", font_size=35, should_center=False), DecimalNumber(),
                        Text("  )", font_size=35, should_center=False))
        label3.arrange(RIGHT)
        label3.add_updater(label3_position)
        self.add(label3)

        self.add(dot_axes, lines)

        self.wait(5)

        words6 = Tex("""
            If we now sweep the tangent line we can trace\\\\ how this point moves 
        """, font_size=30)
        words6.to_corner(UL)

        # Tex("(0, ").scale(0.75).next_to(grid.c2p(1, 1, 0))

        self.play(
            FadeTransform(words5, words6),
            # alpha.animate.set_value(1.25), run_time = 1, rate_func=rate_functions.linear
        )

        dot_axes.add_updater(transformed_position)
        # lines.add_updater(transformed_position2)

        alpha.set_value(-5)

        trace = TracedPath(dot_axes.get_center, stroke_color=GREEN)

        self.add(trace)

        self.play(alpha.animate.set_value(1.5), run_time=10, rate_func=rate_functions.linear)

        self.wait(4)

        words7 = Tex("""
            If we look at this trace we can see\\\\ that it actually traces out the function \\\\ -x (ln(x)-1)
        """, font_size=30)
        words7.to_corner(UL)

        self.play(
            FadeTransform(words6, words7),
            FadeOut(label),
            FadeOut(label2),
            FadeOut(label3),
            FadeOut(intercept),
            FadeOut(tangent),
            FadeOut(point),
        )

        x_ln = axes.plot(
            lambda x: -x * (math.log(x, np.e) - 1),
            color=RED,
            x_range=[0.001, 5]
        )

        x_ln_label = axes.get_graph_label(x_ln, "-x (ln(x)-1)", direction=LEFT)

        self.play(
            Create(x_ln),
            # Create(x_ln),
            FadeIn(x_ln_label),
        )

        self.wait(4)

        x_ln2 = axes.plot(
            lambda x: x * (math.log(x, np.e) - 1),
            color=RED,
            x_range=[0.001, 5]
        )

        x_ln2_label = axes.get_graph_label(x_ln2, "x (ln(x)-1)", direction=LEFT)

        words8 = Tex("""
            Taking the negative of this yields -x (ln(x)-1)\\\\  This is the dual of $e^x$\\\\ 
        """, font_size=30)
        words8.to_corner(UL)

        self.play(
            # FadeOut(x_ln),
            FadeOut(x_ln_label),
            FadeOut(dot_axes),
            FadeOut(trace),
            FadeOut(lines),
            ReplacementTransform(x_ln, x_ln2),
            FadeIn(x_ln2_label),
            FadeTransform(words7, words8)
        )

        self.wait()


class Lengendre3(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: -np.e ** x,
            color=BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "-e^x", direction=LEFT)

        x_ln2 = axes.plot(
            lambda x: x * (math.log(x, np.e) - 1),
            color=RED,
            x_range=[0.001, 5]
        )

        x_ln2_label = axes.get_graph_label(x_ln2, "x (ln(x)-1)", direction=LEFT)

        words = Tex("""
            Now let's look at what happens when we \\\\  apply the same process to this new function\\\\ 
        """, font_size=30)
        words.to_corner(UL)

        self.play(
            # Create(x_2),
            Create(x_ln2),
            # FadeIn(x_2_label),
            FadeIn(x_ln2_label),
            FadeIn(words),
        )

        def slope(x):
            return math.log(x, np.e)

        def func(x):
            return x * (math.log(x, np.e) - 1)

        alpha = ValueTracker(.001)

        def transformed_position(mobject):
            mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                     -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position2(mobject):
            mobject.move_to(axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position3(mobject):
            mobject.move_to(axes.c2p(alpha.get_value(), func(alpha.get_value())))

        dot_axes = Dot(
            axes.c2p(slope(alpha.get_value()), -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
            color=GREEN)
        dot_axes.add_updater(transformed_position)

        lines = always_redraw(lambda: axes.get_lines_to_point(axes.c2p(slope(alpha.get_value()), -slope(
            alpha.get_value()) * alpha.get_value() + func(alpha.get_value()))))

        dot_intercept = Dot(axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
                            color=RED)
        dot_intercept.add_updater(transformed_position2)

        dot_func = Dot(axes.c2p(alpha.get_value(), func(alpha.get_value())), color=RED)
        dot_func.add_updater(transformed_position3)

        draw_tangent = (lambda:
                        Line(
                            start=axes.c2p(alpha.get_value(), func(alpha.get_value())),
                            end=axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
                            color=WHITE))

        tangent = always_redraw(draw_tangent)

        trace = TracedPath(dot_axes.get_center, stroke_color=GREEN)

        self.add(dot_axes, lines, dot_intercept, dot_func, tangent, trace)
        self.play(alpha.animate.set_value(5), run_time=10, rate_func=rate_functions.linear)

        words2 = Tex("""
            The new path traces out the function $-e^x$\\\\ 
        """, font_size=30)
        words2.to_corner(UL)
        self.play(
            FadeTransform(words, words2),
            FadeOut(tangent),
            FadeOut(dot_func),
            FadeOut(dot_intercept),
            FadeOut(dot_axes),

            # Create(x_2),
            FadeOut(trace),
            FadeOut(lines),
            Create(x_2),
            FadeIn(x_2_label),

        )

        self.wait(4)

        x_2_new = axes.plot(
            lambda x: np.e ** x,
            color=BLUE
        )

        x_2_new_label = axes.get_graph_label(x_2_new, "e^x", direction=LEFT)

        words3 = Tex("""
            Taking the negative of this yields $e^x$\\\\ This is the same as our original function
        """, font_size=30)
        words3.to_corner(UL)

        self.play(
            ReplacementTransform(x_2, x_2_new),
            FadeOut(x_2_label),
            FadeIn(x_2_new_label),
            FadeTransform(words2, words3),
        )

        self.wait()


class Lengendre4(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: (x - 1) ** 2 * (x + 1) ** 2,
            color=BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "(x-1)^2 (x+1)^2", direction=RIGHT)

        words = Tex("""
            Consider the non-convex \\\\function$(x-1)^2 (x+1)^2$\\\\ 
        """, font_size=30)
        words.to_corner(UL)

        self.play(
            Create(x_2),

            FadeIn(x_2_label),

            FadeIn(words),
        )

        self.wait(3)

        def slope(x):
            return 4 * x * (x ** 2 - 1)

        def func(x):
            return (x - 1) ** 2 * (x + 1) ** 2

        alpha = ValueTracker(-1.5)

        def transformed_position(mobject):
            mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                     -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position2(mobject):
            mobject.move_to(axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position3(mobject):
            mobject.move_to(axes.c2p(alpha.get_value(), func(alpha.get_value())))

        def transformed_position4(mobject):
            mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                     slope(alpha.get_value()) * alpha.get_value() - func(alpha.get_value())))

        dot_axes = Dot(
            axes.c2p(slope(alpha.get_value()), -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
            color=GREEN)
        dot_axes.add_updater(transformed_position)

        lines = always_redraw(lambda: axes.get_lines_to_point(axes.c2p(slope(alpha.get_value()), -slope(
            alpha.get_value()) * alpha.get_value() + func(alpha.get_value()))))

        dot_intercept = Dot(axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
                            color=RED)
        dot_intercept.add_updater(transformed_position2)

        dot_func = Dot(axes.c2p(alpha.get_value(), func(alpha.get_value())), color=RED)
        dot_func.add_updater(transformed_position3)

        draw_tangent = (lambda:
                        Line(
                            start=axes.c2p(alpha.get_value(), func(alpha.get_value())),
                            end=axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())),
                            color=WHITE))

        tangent = always_redraw(draw_tangent)

        trace = TracedPath(dot_axes.get_center, stroke_color=GREEN)

        words1 = Tex("""
            We can apply the same process \\\\ to this as the previous function
        """, font_size=30)
        words1.to_corner(UL)

        self.play(
            FadeTransform(words, words1),
        )

        self.add(dot_axes, lines, dot_intercept, dot_func, tangent, trace)
        # self.add(dot_axes)
        self.play(
            alpha.animate.set_value(1.5), run_time=5, rate_func=rate_functions.linear)

        words2 = Tex("""
            A non-convex function has \\\\ multiple points with the same slope\\\\ so the trace of the point is \\\\ not a function
        """, font_size=30)
        words2.to_corner(UL)

        self.play(
            FadeOut(tangent),
            FadeOut(dot_func),
            FadeOut(dot_axes),
            FadeOut(dot_intercept),
            FadeOut(lines),
            FadeTransform(words1, words2),

        )

        self.wait(5)

        words3 = Tex("""
            However, if we only look at the lower \\\\ bound of the function \\\\ we can see that it is concave
        """, font_size=30)
        words3.to_corner(UL)

        def transformed_position5(mobject):
            if -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value()) < 0:
                mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                         -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))
            else:
                mobject.move_to(axes.c2p(0, 0))

        dot_axes_new = Dot(axes.c2p(0, 0), color=RED)
        dot_axes_new.add_updater(transformed_position5)

        trace_new = TracedPath(dot_axes_new.get_center, stroke_color=RED)

        self.add(dot_axes_new, trace_new)
        alpha.set_value(-1.5)
        self.play(
            FadeOut(trace),
            alpha.animate.set_value(1.5), run_time=5, rate_func=rate_functions.linear)

        self.play(
            FadeTransform(words2, words3),
        )

        words4 = Tex("""
            The negative of this function is the \\\\lengendre-fenchel transform \\\\ and it is convex even though \\\\ the input function is not convex
        """, font_size=30)
        words4.to_corner(UL)

        self.wait(5)

        self.play(
            FadeTransform(words3, words4),

        )

        self.wait()


class Lengendre5(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-1, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: (x - 1) ** 2 * (x + 1) ** 2,
            color=BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "(x-1)^2 (x+1)^2", direction=RIGHT)

        words = Tex("""
            Now let's look at the transform\\\\ and the double transform of \\\\$(x-1)^2 (x+1)^2$\\\\ 
        """, font_size=30)
        words.to_corner(UL)

        self.play(
            Create(x_2),

            FadeIn(x_2_label),

            FadeIn(words),
        )

        self.wait(3)

        def slope(x):
            return 4 * x * (x ** 2 - 1)

        def func(x):
            return (x - 1) ** 2 * (x + 1) ** 2

        alpha = ValueTracker(-1.5)

        def transformed_position(mobject):
            mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                     -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position2(mobject):
            mobject.move_to(axes.c2p(0, -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value())))

        def transformed_position3(mobject):
            mobject.move_to(axes.c2p(alpha.get_value(), func(alpha.get_value())))

        def transformed_position4(mobject):
            mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                     slope(alpha.get_value()) * alpha.get_value() - func(alpha.get_value())))

        def transformed_position5(mobject):
            if -slope(alpha.get_value()) * alpha.get_value() + func(alpha.get_value()) < 0:
                mobject.move_to(axes.c2p(slope(alpha.get_value()),
                                         slope(alpha.get_value()) * alpha.get_value() - func(alpha.get_value())))
            else:
                mobject.move_to(axes.c2p(0, 0))

        def transformed_position6(mobject):
            x = alpha.get_value()
            if x < -1 or x > 1:
                mobject.move_to(axes.c2p(x, func(x)))
            else:
                mobject.move_to(axes.c2p(x, 0))

        first_transform = Dot(axes.c2p(0, 0), color=RED)
        first_transform.add_updater(transformed_position5)

        first_trace = TracedPath(first_transform.get_center, stroke_color=RED)

        second_transform = Dot(axes.c2p(0, 0), color=GREEN)
        second_transform.add_updater(transformed_position6)

        second_trace = TracedPath(second_transform.get_center, stroke_color=GREEN)

        self.add(first_transform, first_trace, second_transform, second_trace)
        alpha.set_value(-2)

        label1 = axes.get_graph_label(x_2, "f^{\cdot}(x)", direction=RIGHT + DOWN * 2, color=RED)
        label2 = axes.get_graph_label(x_2, "f^{\cdot \cdot}(x)", direction=RIGHT + DOWN * 5, color=GREEN)

        self.add(label1, label2)
        self.play(
            # FadeOut(trace),
            alpha.animate.set_value(2), run_time=5, rate_func=rate_functions.linear)

        words2 = Tex("""
            The first lengendre transform is a convex\\\\ function with a discontinuous derivative \\\\ The second lengendre transform is \\\\ the largest convex function that \\\\ is smaller than f(x)
        """, font_size=30)
        words2.to_corner(UL)

        self.play(
            FadeTransform(words, words2),

        )

        self.wait()


class Lengendre6(Scene):
    def construct(self):
        lines = VGroup(
            Tex("""
                The technical definition of the lengendre-fenchel transform is \\\\
            """, font_size=30),
            Tex("""
                $f^\cdot(p) = sup\{px - f(x) | x \in \mathbb{R}\} (p \in \mathbb{R})$ \\\\
            """, font_size=30),
            Tex("""
                or for discrete functions \\\\
            """, font_size=30),
            Tex("""
                $f^\cdot(p) = sup\{px - f(x) | x \in \mathbb{Z}\} (p \in \mathbb{Z})$ \\\\
            """, font_size=30),

            Tex("""
                This transform has several unique properties which make it useful in functional analysis\\\\ 
            """, font_size=30)
        )

        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(
            FadeIn(lines),
        )


class Lengendre7(Scene):
    def construct(self):
        lines = VGroup(
            Tex("""
                1. The lengendre-fenchel transform of a function is convex\\\\
            """, font_size=30),
            Tex("""
                2. If a function is convex it is equal to its double lengendre-fenchel transform\\\\
            """, font_size=30),
            Tex("""
                3. If a function is not convex its double lengendre-fenchel transform is \\\\
                the largest function which is pointwise-dominated by the function
            """, font_size=30),
            # Tex("""
            #     $f^\cdot(p) = sup\{px - f(x) | x \in \mathbb{Z}\} (p \in \mathbb{R})$ \\\\
            # """, font_size=30),

            # Tex("""
            #     This transform has several unique properties which make it useful in functional analysis\\\\ 
            # """, font_size=30)
        )

        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(
            FadeIn(lines[0]),
        )
        self.wait(3)

        self.play(
            FadeIn(lines[1]),
        )
        self.wait(3)

        self.play(
            FadeIn(lines[2]),
        )
        self.wait(3)


class Lengendre8(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-1, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: (x / 2 - 1) ** 2 * (x / 2 + 1) ** 2,
            color=BLUE
        )

        x_2_label = axes.get_graph_label(x_2, "(x/2-1)^2 (x/2+1)^2 ", direction=RIGHT)

        x_2l = axes.plot(
            lambda x: (x / 2 - 1) ** 2 * (x / 2 + 1) ** 2 if x > 2 or x < -2 else 0,
            color=RED
        )

        x_2l_label = axes.get_graph_label(x_2, "f ^{\cdot \cdot}(x)", direction=RIGHT + 5 * DOWN, color=RED)

        words = Tex("""
            What does it mean to be pointwise dominated?\\\\ 
        """, font_size=30)
        words.to_corner(UL)

        self.play(
            Create(x_2),

            FadeIn(x_2_label),

            FadeIn(words),
        )

        self.wait(1)

        words2 = Tex("""
            At every point the function is as large as it\\\\ can be while still being less than or equal \\\\ to f(x) and convex
        """, font_size=30)
        words2.to_corner(UL)

        self.play(
            Create(x_2l),

            FadeIn(x_2l_label),
            FadeTransform(words, words2),
        )

        x_points_list = [Dot(point=axes.c2p(x, (x / 2 - 1) ** 2 * (x / 2 + 1) ** 2), color=BLUE) for x in range(-5, 5)]
        x_points = VGroup(*x_points_list)

        def f_2(x):
            return (x / 2 - 1) ** 2 * (x / 2 + 1) ** 2

        x_lines_list = [Line(start=axes.c2p(x, f_2(x)), end=axes.c2p(x + 1, f_2(x + 1)), color=BLUE) for x in
                        range(-6, 5)]
        x_lines = VGroup(*x_lines_list)

        def f(x):
            return (x / 2 - 1) ** 2 * (x / 2 + 1) ** 2 if x > 2 or x < -2 else 0

        xl_points_list = [Dot(point=axes.c2p(x, f(x)), color=RED, radius=.15) for x in range(-5, 5)]
        xl_points = VGroup(*xl_points_list)

        self.wait(5)

        words3 = Tex("""
            The same is true in a discrete context \\\\ Every point will be as close to f(x) \\\\ as possible while remaining convex
        """, font_size=30)
        words3.to_corner(UL)

        self.play(
            FadeOut(x_2),
            FadeOut(x_2l),
            FadeIn(xl_points),
            FadeIn(x_points),
            FadeIn(x_lines),
            FadeTransform(words2, words3),
        )

        self.wait()
