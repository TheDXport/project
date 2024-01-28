from manim import *


class Solution(Scene):
    def construct(self):
#         title = Text("AP Calculus BC FRQ 2014 #1").shift(UP)
#         self.play(Write(title))
#         underline = Underline(title, color=WHITE, buff=0.5).shift(UP * 0.35)
#         xin = Text("presented and coded by xinathan :D").scale(0.6)
#         seeattachedforsourcecode = Text("see attached for the source code!").scale(0.34).shift(DOWN * 0.55)
#         self.play(Create(underline), Write(xin, run_time=1.2))
        
#         self.wait(0.7)
        
#         self.play(Write(seeattachedforsourcecode, run_time=0.9))
        
#         self.wait(1.6)
        
#         self.play(FadeOut(title, xin, underline, seeattachedforsourcecode))
        
#         questionbackgroundp1 = Text("Grass clippings are placed in a bin, where they decompose. For 0 ≤ t ≤ 30, the amount of grass ").scale(0.5).shift(UP * 3)
#         questionbackgroundp2 = Text("clippings remaining in the bin is modeled by ").scale(0.5).shift(UP * 2.47 + LEFT * 3.28)
#         equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.67).shift(UP * 2.49 + RIGHT *1.26 )
#         questionbackgroundp3 = Text(", where A(t) is measured in ").scale(0.5).shift(UP * 2.47 + RIGHT * 4.5)
#         questionbackgroundp4 = Text("pounds and t is measured in days.").scale(0.5).shift(UP * 1.94 + LEFT * 4.05)
  
#         self.play(Write(questionbackgroundp1))
#         self.play(Write(questionbackgroundp2))
#         self.play(Write(equation))
#         self.play(Write(questionbackgroundp3))
#         self.play(Write(questionbackgroundp4)) 
        
#         self.wait(1.2)
        
#         partaquestion = Text("a) Find the average rate of change of A(t) over the interval 0 ≤ t ≤ 30. Indicate units of measure. ").scale(0.5).shift(UP * 1.25+ RIGHT * 0.1)
#         self.play(Write(partaquestion))
        
#         self.wait(1.5)
        
#         slope_formula = MathTex(r"\frac{y_2 - y_1}{x_2 - x_1}").shift(DOWN * 0.2)
#         self.play(Write(slope_formula))
#         self.play(slope_formula.animate.shift(LEFT * 1.7), run_time=3.5)
#         equal_sign = MathTex('=').shift(LEFT * 0.4 + DOWN * 0.14)
#         self.wait(0.8)
#         self.play(Write(equal_sign))
        
#         subbed_slope_formula = MathTex(r"\frac{A(30) - A(0)}{30 - 0}").shift(RIGHT * 1.3 + DOWN * 0.12).scale(0.9)
#         self.play(Write(subbed_slope_formula))

#         self.wait(0.9)
        
#         # Substitute
        
#         target_position = slope_formula.get_center()
#         self.play(FadeOut(slope_formula))
        
        
#         self.play(subbed_slope_formula.animate.move_to(target_position + LEFT * 3.3), equal_sign.animate.move_to(target_position + LEFT * 1.6))
        
#         fullySubbed_slope_formula = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(0.931)^0}{30 - 0}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9)
#         self.play(Write(fullySubbed_slope_formula))
        
#         self.wait(0.8)
        
#         target_position = subbed_slope_formula.get_center()
#         self.play(FadeOut(equal_sign, subbed_slope_formula), fullySubbed_slope_formula.animate.move_to(target_position + RIGHT * 1.7))
        
#         steps = MathTex(r"\frac{6.687(0.931)^{30} - 6.687(1)}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
#         self.play(Transform(fullySubbed_slope_formula, steps))
#         steps = MathTex(r"\frac{0.782928 - 6.687}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center() + LEFT * 0.6)
#         self.play(Transform(fullySubbed_slope_formula, steps))
#         steps = MathTex(r"\frac{-5.9040721306221}{30}").move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
#         self.play(Transform(fullySubbed_slope_formula, steps))
#         steps = MathTex('-0.196802').move_to(equal_sign.get_center() + RIGHT * 3.4).scale(0.9).move_to(fullySubbed_slope_formula.get_center())
#         self.play(Transform(fullySubbed_slope_formula, steps))
        
#         self.wait(2)
        
#         units = MathTex(r"\frac{pounds}{day}").move_to(fullySubbed_slope_formula.get_center() + RIGHT * 2.03).scale(0.9)
#         self.play(Write(units))
#         answer_combined = VGroup(fullySubbed_slope_formula, units)
#         answer_circle = Ellipse(color=YELLOW).surround(answer_combined)
#         self.play(Create(answer_circle))
        
#         self.wait(1) 
        
#         self.play(FadeOut(questionbackgroundp1, questionbackgroundp2, questionbackgroundp3, questionbackgroundp4, partaquestion, answer_circle, answer_combined, equation))
        
#         self.wait(2)
#         # Visualize the rate of change as compared to the graph
#         partbquestionp1 = Text("b) Find the value of A'(15). Using correct units, interpret the meaning of the value in the context").shift(UP * 3 + LEFT * 0.2).scale(0.5)
#         partbquestionp2 = Text("of the problem.").shift(UP * 2.47 + LEFT * 5.27).scale(0.5)
        
#         self.play(Write(partbquestionp1))
#         self.play(Write(partbquestionp2))

#         axes = Axes(
#                 x_range=[0, 50, 1],
#                 y_range=[0, 9, 1],
#                 axis_config={"color": BLUE},
#                 x_axis_config={
#                 "include_tip": True,  # Show the arrow tip
#                 "numbers_to_include": np.arange(0, 50, 5),  # Numbers to include
#                 "font_size": 30,  # Font size for the numbers
#             },
#             y_axis_config={
#                 "include_tip": True,  # Show the arrow tip
#                 "numbers_to_include": np.arange(0, 9, 2),  # Numbers to include
#                 "font_size": 30,  # Font size for the numbers
#             }, 
#             tips=True

                 
#             ).scale(0.7)

#         self.wait(2)
#         graph = axes.plot(lambda t: 6.687 * (0.931)**t, color=GREEN_B)
        
#         graph_label = MathTex('f(t) = 6.687 \cdot (0.931)^t', color=GREEN_B).scale(0.7)

#         # Determine a point on the graph to position the label above
#         label_coord = axes.i2gp(5, graph)  # Get the graph point at x = 5
#         graph_label.next_to(label_coord, RIGHT * 3)
#         self.play(Create(axes))
#         self.play(Create(graph))
#         self.play(Write(graph_label, run_time=0.9))

#         self.wait(2)
        
        

#          # Calculate the derivative at t = 15
#         t_value = 15
#         slope = 6.687 * np.log(0.931) * (0.931)**t_value
#         f_t = 6.687 * (0.931)**t_value

#         tangent_start = t_value - 1  # Adjust if you want a longer line
#         tangent_end = t_value + 1    # Adjust if you want a longer line


#         start_point = axes.c2p(tangent_start, slope * (tangent_start - t_value) + f_t)
#         end_point = axes.c2p(tangent_end, slope * (tangent_end - t_value) + f_t)

        
#         tangent_line = Line(start_point, end_point, color=RED).scale(10)
#         point_on_graph = axes.c2p(t_value, f_t)
#         dot = Dot(point_on_graph, color=WHITE, radius=0.06)  # Adjust the radius as needed

#         start_point = axes.c2p(t_value, 0)  # Start from the x-axis
#         end_point = point_on_graph          # End at the point of tangency on the graph
#         dotted_line = DashedLine(start_point, end_point, dashed_ratio=0.6, color=WHITE)

#         # Animate the dotted line approaching the point of tangency
#         self.play(Create(dotted_line))
       
#         self.play(FadeIn(dot))
#         self.play(Create(tangent_line))

#         self.wait(2)
        
#         self.play(FadeOut(tangent_line, dot, dotted_line))
#         self.play(FadeOut(axes, graph_label, graph))
#         derivative_function = MathTex('6.687(0.931)^t')
#         deriv = MathTex(r'\frac{d}{dt}').move_to(derivative_function.get_center() + LEFT * 1.8)
#         combined = VGroup(deriv, derivative_function)
#         self.play(Write(combined))
#         step = MathTex(r"6.687(e^{ln(0.931)})^t")
#         self.play(Transform(combined, step))
#         step = MathTex(r"6.687(e^{ln(0.931)t})^1")
#         self.play(Transform(combined, step))
#         step = MathTex(r"6.687(e^{ln(0.931)t}) \cdot ln(0.931)")
#         self.play(Transform(combined, step))

#         self.play(combined.animate.shift(RIGHT * 1.3))
#         function = MathTex(r"A'(t) =").move_to(combined.get_center() + LEFT * 3.9)
#         self.play(Write(function, run_time=0.6))
#         self.play(Transform(function, MathTex(r"A'(15) =").move_to(combined.get_center() + LEFT * 4.06)))
#         step = MathTex(r"6.687(e^{ln(0.931)15}) \cdot ln(0.931)").move_to(function.get_center() + RIGHT * 4.2)
#         self.play(Transform(combined,step))
#         step = MathTex(r"6.687(e^{(-0.0714)15}) \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 4.36)
#         self.play(Transform(combined,step))
#         step = MathTex(r"6.687(0.931^{15}) \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 4.6)
#         self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.7))
#         step = MathTex(r"2.2881 \cdot (-0.0714)").move_to(function.get_center() + RIGHT * 3.5)
#         self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.5))
#         step = MathTex(r"-0.1635").move_to(function.get_center() + RIGHT * 2.6)
#         self.play(Transform(combined,step), function.animate.shift(RIGHT * 0.56))
#         combined = VGroup(function, combined)
#         self.play(combined.animate.shift(LEFT * 1.2))
#         units = MathTex(r"\frac{pounds}{day}").move_to(combined.get_center() + RIGHT * 3)
#         self.play(Write(units))
#         combined = VGroup(combined, units)
#         self.play(combined.animate.scale(0.8))
#         self.play(combined.animate.shift(LEFT * 3.7 + UP))
#         explanation = Text("This means that the total amount of grass clippings in the bin is decreasing at exactly\n-0.1635 pounds per day specifically on day 15 (t = 15).", pacing=1.1).scale(0.5).shift(LEFT * 0.11 + DOWN * 0.37)line_s
#         self.play(Write(explanation))
#         combined = VGroup(combined, explanation)
#         answer_circle = Rectangle(color=YELLOW).surround(combined)
#         answer_circle.stretch_to_fit_height(answer_circle.height * 0.5)
#         answer_circle.stretch_to_fit_width(answer_circle.width * 1.02)
#         self.play(ShowCreationThenFadeOut(answer_circle))
#         self.wait(2)
#         self.play(FadeOut(combined, partbquestionp1, partbquestionp2))
          partcquestion = Text("c) Find the time t for which the amount of grass clippings in the bin is equal to the\n    average amount of grass clippings in the bin over the interval 0 ≤ t ≤ 30.", line_spacing=1.1).shift(UP * 3 + LEFT * 0.2).scale(0.5)
          self.play(Write(partcquestion), run_time=2.5)
          recallText = Text("Recall that we are given:").shift(LEFT * 4 + UP * 1.5).scale(0.5)
          equation = MathTex('A(t) = 6.687(0.931)^t').scale(0.7).move_to(recallText.get_center() + RIGHT * 3.42)
          recallTextp2 = Text("as the total grass clippings").scale(0.5).move_to(equation.get_center() + RIGHT * 3.6)
          self.play(Write(recallText))
          self.play(Write(equation))
          self.play(Write(recallTextp2))
          text = Text("Average amount of grass clippings: ").scale(0.5).shift(LEFT * 3.25 + UP * 0.6)
          
          
          averageAmount = MathTex(r"\frac{1}{b - a} \int_b^a A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4)
          self.play(Write(text))
          self.play(Write(averageAmount))
          zero = MathTex("0").shift(LEFT)
          middleOfInterval = MathTex("\leq t \leq")
          thirty = MathTex("30").shift(RIGHT)
          interval = VGroup(zero, middleOfInterval, thirty).scale(0.7).shift(DOWN * 0.4)
          self.play(Write(interval))
          arrowa = Arrow(start=interval.get_center() + DOWN * 1.2 + LEFT * 0.7, end = interval.get_center() + DOWN * 0.1 + LEFT * 0.7)
          arrowb = Arrow(start=interval.get_center() + DOWN * 1.2 + RIGHT * 0.6, end = interval.get_center() + DOWN * 0.1 + RIGHT * 0.6)
          a = Text("a").scale(0.5).shift(arrowa.get_center() + DOWN * 0.5)
          b = Text("b").scale(0.5).shift(arrowb.get_center() + DOWN * 0.5)
          
          self.wait(1)
          
          self.play(Write(arrowa))  
          self.play(Write(arrowb)) 
          self.play(Write(a), Write(b))
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30 - 0}\int_0^{30}A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4.18)))
          
          self.wait(2) 
                    
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\int_0^{30}A(t)\,dt").scale(0.7).move_to(text.get_center() + RIGHT * 4)))

          # Script: Now the question is asking: when is the total number of grass clippings equal to average amount? 
          # So, we simply set them equal to each other! 
          
          self.wait(9)
          
          self.play(FadeOut(recallText, recallTextp2, text, arrowa, arrowb, a, b, interval))
          self.play(Transform(equation, MathTex("6.687(0.931)^t").scale(0.7).move_to(equation.get_center())))
          self.play(equation.animate.shift(LEFT * 3), averageAmount.animate.shift(UP * 0.9 + LEFT * 1.6))
          equalSign = MathTex("=").scale(0.7).move_to(equation.get_center() + RIGHT * 1.3)
          self.play(Write(equalSign))
          
          self.wait(3)
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,\int_0^{30}6.687(0.931)^t\,dt").move_to(averageAmount.get_center() + RIGHT * 0.67).scale(0.7)))
          
          self.wait()
          
          # Let's evaluate the right side first!
          self.wait(1)
          
          self.play(averageAmount.animate.shift(LEFT * 4), FadeOut(equalSign, equation))
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}(0.931)^t\,dt").scale(0.7).move_to(averageAmount.get_center())))
          recallText = Text("We know that ").scale(0.5)
          eln = MathTex("e^{ln(k)}").scale(0.7)
          recallTextp2 = Text("cancels out to").scale(0.5)
          k = MathTex("k").scale(0.7)
          combined = VGroup(recallText, eln, recallTextp2, k).arrange(RIGHT)
          self.play(Write(combined))
          
          self.wait(2)
          
          self.play(Transform(combined, Text("Hence, we can rewrite as follows!").scale(0.5)))
          
          self.wait()
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931^t)}\,dt").scale(0.7).move_to(averageAmount.get_center() + RIGHT * 0.32)))
          self.play(FadeOut(combined))
          
          self.wait()
          
          self.play(Transform(averageAmount, MathTex(r"\frac{1}{30}\,6.687\int_0^{30}e^{ln(0.931)t}\,dt").scale(0.7).move_to(averageAmount.get_center())))
          
          self.wait(2)
          
          equalSign = MathTex("=").scale(0.7).move_to(averageAmount.get_center() + RIGHT * 2.2)
          integral_expr = MathTex(r"\frac{1}{30}\,(\frac{6.687e^{ln(0.931)t}}{ln(0.931)})").scale(0.7).move_to(equalSign.get_center() + RIGHT * 1.8)
          bounds = MathTex("\\Bigg|", "_0", "^{30}").scale(0.7)
          bounds.next_to(integral_expr, RIGHT)
          self.play(Write(equalSign))
          self.play(Write(integral_expr))
          self.play(Write(bounds))
          definite_integral_eval = MathTex (r"\frac{1}{30}\,((\frac{6.687e^{ln(0.931)30}}{ln(0.931)})-(\frac{6.687e^{ln(0.931)0}}{ln(0.931)}))").scale(0.7).move_to(averageAmount.get_center() + DOWN * 1.5 + RIGHT * 1.3)
          self.play(Write(definite_integral_eval))
          
          self.wait(2)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687e^{0}}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
          
          self.wait(1.5)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687(1)}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
          
          self.wait(1.5)
          
          self.play(Transform(definite_integral_eval, MathTex(r"\frac{1}{30}\,((\frac{6.687e^{(ln(0.931))30}}{ln(0.931)})-(\frac{6.687}{ln(0.931)}))").scale(0.7).move_to(definite_integral_eval.get_center())))
        
          self.play(FadeOut(averageAmount, equalSign, integral_expr, bounds))
          self.wait()
          self.play(definite_integral_eval.animate.shift(UP * 1.2 + LEFT * 0.3))
          equalSign.next_to(definite_integral_eval, RIGHT)
          self.play(Write(equalSign))
          recallText = Text("Factor").next_to(equalSign, RIGHT).scale(0.5)
          recallTextp2 = MathTex(r"\frac{6.687}{ln(0.931)}").scale(0.7).next_to(recallText, RIGHT)
          self.play(Write(recallText), Write(recallTextp2))
          