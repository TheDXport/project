from manim import *


class Solution(Scene):
    def construct(self):
        title = Text("AP Calculus BC FRQ 2014 #1").shift(UP)
        self.play(Write(title))
        underline = Underline(title, color=WHITE, buff=0.5).shift(UP * 0.35)
        xin = Text("presented and coded by xinathan :D").scale(0.6)
        seeattachedforsourcecode = Text("see attached for the source code!").scale(0.34).shift(DOWN * 0.55)
        self.play(Create(underline), Write(xin, run_time=1.2))
        
        self.wait(0.7)
        
        self.play(Write(seeattachedforsourcecode, run_time=0.9))
        
        self.wait(1.6)
        
        self.play(FadeOut(title, xin, underline, seeattachedforsourcecode))
        
        questionbackgroundp1 = Text("Grass clippings are placed in a bin, where they decompose. For 0 ≤ t ≤ 30, the amount of grass ").scale(0.5).shift(UP * 3)
        questionbackgroundp2 = Text("clippings remaining in the bin is modeled by ").scale(0.5).shift(UP * 2.47 + LEFT * 3.28)
        equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.67).shift(UP * 2.49 + RIGHT *1.26 )
        questionbackgroundp3 = Text(", where A(t) is measured in ").scale(0.5).shift(UP * 2.47 + RIGHT * 4.5)
        questionbackgroundp4 = Text("pounds and t is measured in days.").scale(0.5).shift(UP * 1.94 + LEFT * 4.05)
  
        self.play(Write(questionbackgroundp1))
        self.play(Write(questionbackgroundp2))
        self.play(Write(equation))
        self.play(Write(questionbackgroundp3))
        self.play(Write(questionbackgroundp4)) 
        
        self.wait(1.2)
        
        partaquestion = Text("a) Find the average rate of change of A(t) over the interval 0 ≤ t ≤ 30. Indicate units of measure. ").scale(0.5).shift(UP * 1.25+ RIGHT * 0.1)
        self.play(Write(partaquestion))
        
        self.wait(1.5)
        
        slope_formula = MathTex(r"\frac{y_2 - y_1}{x_2 - x_1}").shift(DOWN * 0.2)
        self.play(Write(slope_formula))
        self.play(slope_formula.animate.shift(LEFT * 1.7), run_time=3.5)
        equal_sign = MathTex('=').shift(LEFT * 0.4 + DOWN * 0.14)
        self.wait(0.8)
        self.play(Write(equal_sign))
        
        subbed_slope_formula = MathTex(r"\frac{A(30) - A(0)}{30 - 0}").shift(RIGHT * 1.3 + DOWN * 0.12).scale(0.9)
        self.play(Write(subbed_slope_formula))

        self.wait(0.9)
        
        # Substitute
        
        target_position = slope_formula.get_center()
        self.play(FadeOut(slope_formula))
        
        
        self.play(subbed_slope_formula.animate.move_to(target_position + LEFT * 3.3), equal_sign.animate.move_to(target_position + LEFT * 1.6))
        
        fullySubbed_slope_formula = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(0.931)^0}{30 - 0}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9)
        self.play(Write(fullySubbed_slope_formula))
        
        self.wait(0.8)
        
        target_position = subbed_slope_formula.get_center()
        self.play(FadeOut(equal_sign, subbed_slope_formula), fullySubbed_slope_formula.animate.move_to(target_position + RIGHT * 1.7))
        
        steps = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(1)}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
        self.play(Transform(fullySubbed_slope_formula, steps))
        steps = MathTex(r"\frac{0.782928 - 6.687}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
        self.play(Transform(fullySubbed_slope_formula, steps))
        steps = MathTex(r"\frac{-5.9040721306221}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
        self.play(Transform(fullySubbed_slope_formula, steps))
        steps = MathTex('-0.196802').move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
        self.play(Transform(fullySubbed_slope_formula, steps))
        
        self.wait(2)
        
        units = MathTex(r"\frac{pounds}{day}").move_to(fullySubbed_slope_formula.get_center() + RIGHT * 2.03).scale(0.9)
        self.play(Write(units))
        answer_combined = VGroup(fullySubbed_slope_formula, units)
        answer_circle = Ellipse(color=YELLOW).surround(answer_combined)
        self.play(Create(answer_circle))
        
        self.wait(1) 
        
        self.play(FadeOut(questionbackgroundp1, questionbackgroundp2, questionbackgroundp3, questionbackgroundp4, partaquestion, answer_circle, answer_combined, equation))
        
        self.wait(2)
        # Visualize the rate of change as compared to the graph
        partbquestionp1 = Text("b) Find the value of A'(15). Using correct units, interpret the meaning of the value in the context").shift(UP * 3 + LEFT * 0.2).scale(0.5)
        partbquestionp2 = Text("of the problem.").shift(UP * 2.47 + LEFT * 5.27).scale(0.5)
        
        self.play(Write(partbquestionp1))
        self.play(Write(partbquestionp2))

        axes = Axes(
                x_range=[-2, 50, 1],
                y_range=[0, 9, 0.3],
                axis_config={"color": BLUE},
                x_axis_config={"include_tip": True}, 
                y_axis_config={"include_tip": True},
                 
            ).scale(0.7)

        self.wait(2)
        graph = axes.plot(lambda t: 6.687 * (0.931)**t, color=GREEN_B)
        
        graph_label = MathTex('f(t) = 6.687 \cdot (0.931)^t', color=GREEN_B).scale(0.7)

        # Determine a point on the graph to position the label above
        label_coord = axes.i2gp(5, graph)  # Get the graph point at x = 5
        graph_label.next_to(label_coord, RIGHT * 3)
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Write(graph_label, run_time=0.9))

        self.wait(2)
        
        derivative = lambda t: np.log(0.931) * 6.687 * (0.931)**t
        
        # Get the slope of the tangent line at x = 15
        slope = derivative(15)

        # Get the point on the graph at x = 15
        point_on_curve = axes.i2gp(15, graph)

        # Get a small line element at x = 15 that represents the tangent
        tangent_line = Line(
            start=point_on_curve + LEFT, 
            end=point_on_curve + RIGHT,
            color=RED
        ).scale(0.2)  # Adjust the length of the tangent line as needed

        # Rotate the tangent line according to the slope
        tangent_line.rotate(np.arctan(slope))

        # Display the tangent line
        self.play(Create(tangent_line))

        self.wait(2)
        
        self.play(FadeOut(axes, tangent_line, graph_label, graph))
        derivative_function = MathTex('6.687(0.931)^t')
        deriv = MathTex(r'\frac{d}{dt}').move_to(derivative_function.get_center() + LEFT * 1.8)
        combined = VGroup(deriv, derivative_function)
        self.play(Write(combined))
        step = MathTex(r"6.687(e^{ln(0.931)})^t")
        self.play(Transform(combined, step))
        step = MathTex(r"6.687(e^{ln(0.931)t})^1")
        self.play(Transform(combined, step))
        step = MathTex(r"6.687(e^{ln(0.931)t}) \cdot ln(0.931)")
        self.play(Transform(combined, step))
        function = MathTex(r"A'(t) =").move_to(combined.get_center() + LEFT * 4)

        self.play(combined.animate.shift(RIGHT * 1.3), Write(function))
        self.play(Write(function))



            