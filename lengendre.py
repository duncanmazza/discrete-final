#!/usr/bin/env python
from manim import *
import numpy as np
import math


class Lengendre1(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: np.e**x,
            color = BLUE
        )

        x_ln = axes.plot(
            lambda x: x*(math.log(x, np.e)-1),
            color = RED,
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
        #axes.i2gp(alpha.get_value(), x_2)[1]

        draw_tangent = (lambda: 
            Line(
                start=axes.i2gp(alpha.get_value(), x_2),
                end=axes.coords_to_point(0,
                    -np.e ** alpha.get_value() * alpha.get_value()  +  np.e ** alpha.get_value(),
                    0),
                color=WHITE))

        draw_intercept = (lambda: 
            Dot(
                point = axes.coords_to_point(0,
                        -np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value(),
                        0),
                color=RED))

        draw_point = (lambda: 
            Dot(
                point = [axes.i2gp(alpha.get_value(), x_2)[0],
                        axes.i2gp(alpha.get_value(), x_2)[1],
                        0],
                color=RED))

        draw_result = (lambda: 
            Dot(
                point = axes.coords_to_point(np.e ** alpha.get_value(),
                        -np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value(),
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

        self.play(alpha.animate.set_value(5), run_time = 10, rate_func=rate_functions.linear)

        self.wait()



class Lengendre2(Scene):
    def construct(self):
        axes = Axes((-5, 5), (-5, 5))
        # axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        x_2 = axes.plot(
            lambda x: np.e**x,
            color = BLUE
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
        #axes.i2gp(alpha.get_value(), x_2)[1]

        draw_tangent = (lambda: 
            Line(
                start=axes.i2gp(alpha.get_value(), x_2),
                end=axes.coords_to_point(0,
                    -np.e ** alpha.get_value() * alpha.get_value()  +  np.e ** alpha.get_value(),
                    0),
                color=WHITE))

        draw_intercept = (lambda: 
            Dot(
                point = axes.coords_to_point(0,
                        -np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value(),
                        0),
                color=RED))

        draw_point = (lambda: 
            Dot(
                point = [axes.i2gp(alpha.get_value(), x_2)[0],
                        axes.i2gp(alpha.get_value(), x_2)[1],
                        0],
                color=RED))

        draw_result = (lambda: 
            Dot(
                point = axes.coords_to_point(np.e ** alpha.get_value(),
                        -np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value(),
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

        self.play(alpha.animate.set_value(2), run_time = 8, rate_func=rate_functions.linear)

        self.wait(3)



        # words3 = Tex("""
        #     Now consider the tangent line at x=1.25
        # """, font_size=30)
        # words3.to_corner(UL)

        # self.play(
        #     FadeTransform(words2, words3)
        # )


        words4 = Tex("""
            Now consider the tangent line at x=1.25 \\\\ The tangent has a slope of 3.49 \\\\ and a y intercept of -.52
        """, font_size=30)
        words4.to_corner(UL)


        # Tex("(0, ").scale(0.75).next_to(grid.c2p(1, 1, 0))

        self.play(
            FadeTransform(words2, words4),
            alpha.animate.set_value(1.25), run_time = 1, rate_func=rate_functions.linear
        )



        # alpha.set_value(1.25)

        # line = Line(intercept.get_center(), point.get_center())

        # brace = Brace(line)
        # bracetext = brace.get_text("Horizontal distance")

        def dot_position(mobject):
            mobject[1].set_value(-np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value())
            mobject.next_to(intercept, LEFT + DOWN)

        def slope_position(mobject):
            mobject[1].set_value(np.e ** alpha.get_value())
            mobject.next_to(tangent, RIGHT/2 + UP)

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
            mobject.move_to(axes.c2p(np.e ** alpha.get_value(), -np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value()))

        def transformed_position2(mobject):
            # mobject.set_value(np.e ** alpha.get_value())
            mobject = axes.get_lines_to_point(axes.c2p(np.e ** alpha.get_value(),-np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value()))


        dot_axes = Dot(axes.c2p(np.e ** alpha.get_value(),-np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value()), color=GREEN)

        lines = always_redraw(lambda: axes.get_lines_to_point(axes.c2p(np.e ** alpha.get_value(),-np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value())))
        # lines = 

        def label3_position(mobject):
            mobject[1].set_value(np.e ** alpha.get_value())
            mobject[3].set_value(-np.e ** alpha.get_value() * alpha.get_value() +  np.e ** alpha.get_value())
            mobject.next_to(dot_axes, DOWN + RIGHT)

        label3 = VGroup(Text("(", font_size=35), DecimalNumber(), Text(", ", font_size=35), DecimalNumber(), Text(" )", font_size=35),)
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


        self.play(alpha.animate.set_value(1.5), run_time = 10, rate_func=rate_functions.linear)

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
            lambda x: -x*(math.log(x, np.e)-1),
            color = RED,
            x_range=[0.001, 5]
        )

        x_ln_label = axes.get_graph_label(x_ln, "-x (ln(x)-1)", direction = LEFT)


        self.play(
            Create(x_ln),
            # Create(x_ln),
            FadeIn(x_ln_label),
        )

        self.wait(4)

        x_ln2 = axes.plot(
            lambda x: x*(math.log(x, np.e)-1),
            color = RED,
            x_range=[0.001, 5]
        )

        x_ln2_label = axes.get_graph_label(x_ln2, "x (ln(x)-1)", direction = LEFT)

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

        







        # self.add(result)
        # self.add(trace)

        # self.play(alpha.animate.set_value(5), run_time = 10, rate_func=rate_functions.linear)

        self.wait()