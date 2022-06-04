from manim import *
from manim import RegularPolygon, Arrow
import numpy as np

# Constants
F = 1 # calculated as F * U
D = 9 # calculated as D * U
lineLength = 10
U = lineLength / ((D + 1) * 2)

class ConvexLen(Scene):
    def construct(self):
        text = Tex("Convex lens")
        text.scale(2)

        # Introduction
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))

        text = MathTex("f = ", F)
        text.to_edge(UP + LEFT)
        self.play(Write(text))

        # Draw
        # Main axe
        l = NumberLine(
            x_range = [-D - 1, D + 1, 2],
            length = D + 1,
            color = BLUE,
            include_ticks = False,
            label_direction = DOWN,
            include_tip = True,
            tip_length = 0.2,
            font_size = 28,
            numbers_to_include = np.arange(F, -F - 0.001, -F * 2)
        )
        # F, F'
        f = Dot(point = np.array([-F * U, 0, 0]), color = YELLOW)
        f_ = Dot(point = np.array([F * U, 0, 0]), color = YELLOW)
        # Len
        ln = DoubleArrow(
            start = 3 * UP,
            end = 3 * DOWN,
            tip_length = 0.2,
            stroke_width = 2
        )
        
        self.play(Create(l))
        self.play(Create(f))
        self.play(Create(f_))
        self.play(Create(ln))

        # Animation
            # Object
        obj = Vector(UP)
        img_line = Arrow(
            tip_length = 0.2,
            color = TEAL_D
        )
        
        text_d = MathTex("d = ").next_to(text, DOWN)
        d = DecimalNumber(D).next_to(text_d, RIGHT)
        tracker = ValueTracker(D)
        obj.add_updater(
            lambda m: m.put_start_and_end_on(l.n2p(tracker.get_value()), l.n2p(tracker.get_value()) + UP)
        )
        d.add_updater(
            lambda m: m.set_value(tracker.get_value())
        )
        img_line.add_updater(
            lambda m: m.put_start_and_end_on(np.array([(1 / tracker.get_value() - 2) ** (-1), 0, 0]), np.array([(1 / tracker.get_value() - 2) ** (-1), 1 / tracker.get_value() * ((1 / tracker.get_value() - 2) ** (-1)), 0])
        ))

        self.play(Write(text_d))
        self.play(Write(d))
        self.play(Create(obj))
        self.play(Create(img_line))
        self.play(tracker.animate.set_value(-D), run_time = 15)
        self.wait()

class ConvergingLen(Scene):
    def construct(self):
        text = Tex("Converging lens")
        text.scale(2)

        # Introduction
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))

        text = MathTex("f = ", F)
        text.to_edge(UP + LEFT)
        self.play(Write(text))

        # Draw
        # Main axe
        l = NumberLine(
            x_range = [-D - 1, D + 1, 2],
            length = D + 1,
            color = BLUE,
            include_ticks = False,
            label_direction = DOWN,
            include_tip = True,
            tip_length = 0.2,
            font_size = 28,
            numbers_to_include = np.arange(F, -F - 0.001, -F * 2)
        )
        # F, F'
        f = Dot(point = np.array([F * U, 0, 0]), color = YELLOW)
        f_ = Dot(point = np.array([-F * U, 0, 0]), color = YELLOW)
        # Len
        ln = ImageMobject("assets/converging_len.png")

        self.play(Create(l))
        self.play(Create(f))
        self.play(Create(f_))
        self.add(ln)

        # Animation
            # Object
        obj = Vector(UP)
        img_line = Arrow(
            tip_length = 0.2,
            color = TEAL_D
        )
        
        text_d = MathTex("d = ").next_to(text, DOWN)
        d = DecimalNumber(D).next_to(text_d, RIGHT)
        tracker = ValueTracker(D)
        obj.add_updater(
            lambda m: m.put_start_and_end_on(l.n2p(tracker.get_value()), l.n2p(tracker.get_value()) + UP)
        )
        d.add_updater(
            lambda m: m.set_value(tracker.get_value())
        )
        img_line.add_updater(
            lambda m: m.put_start_and_end_on(np.array([(1 / tracker.get_value() + 2) ** (-1), 0, 0]), np.array([(1 / tracker.get_value() + 2) ** (-1), 1 / tracker.get_value() * ((1 / tracker.get_value() + 2) ** (-1)), 0])
        ))

        self.play(Write(text_d))
        self.play(Write(d))
        self.play(Create(obj))
        self.play(Create(img_line))
        self.play(tracker.animate.set_value(-D), run_time = 15)
        self.wait()
