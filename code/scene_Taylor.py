#sviluppo in serie di Taylor di una funzione
from manim import *
from math import *

def sin_McLaurin(n):
    coeff = [0 if k % 2 == 0 else ((-1)**((k-1)//2)) / factorial(k) for k in range(n+1)]
    return coeff

def genera_polinomio(coeff):
    return lambda x: sum(c * x**i for i, c in enumerate(coeff))

class SviluppoTaylor(Scene):
    def construct(self):

        self.next_section("Titolo")
        titolo = MathTex(r"\mathbb{T}\text{aylor }\mathbb{E}\text{xpansion of}", color = WHITE, font_size = 120).move_to(ORIGIN).shift(UP*0.5)
        sottotitolo = MathTex(r"sin(x)", font_size = 120, color=DARK_BLUE).move_to(ORIGIN).shift(DOWN)
        self.play(Write(titolo), run_time = 2)
        self.play( Write(sottotitolo), run_tim = 1)
        self.wait(2)
        self.play(FadeOut(titolo), FadeOut(sottotitolo))

        self.next_section("Plot del grafico")
        x_min = -2 * PI
        x_max = 2 * PI
        y_min = -1
        y_max = 1
        asse_x  = MathTex("-2\pi","-\pi","0","\pi","2\pi" )
        ax = Axes(
            x_range = [x_min-0.5, x_max+0.5, PI],
            y_range = [y_min-0.2,y_max + 0.2, 1],
            tips = True,
            axis_config = {"tip_width" : 0.2,
                             "tip_height" : 0.2,
                           "include_numbers" : False,
            }
        )
        x_labels = {-2 * PI: MathTex("-2 \pi"),
                    - PI: MathTex("-\pi"),
                    0: MathTex("0"),
                    PI: MathTex("\pi"),
                    2 * PI: MathTex("2 \pi")
        }
        y_labels = {-1: MathTex("-1"),
                    1: MathTex("1")}
        #ax.get_axis_labels(y_label = MathTex("sin(x)"))
        ax.get_x_axis().add_labels(x_labels)
        ax.get_y_axis().add_labels(y_labels)
        graph = ax.plot(lambda x: sin(x), x_range = [x_min, x_max], color = DARK_BLUE)
        grafico_assi = VGroup(graph,ax)
        grafico_assi.shift(UP * 0.5)
        self.play(Create(ax), run_time = 2)
        self.bring_to_front(ax.get_x_axis())
        self.play(Create(graph), run_time = 2)


        self.next_section("Scrivo i polinomi della serie")
        n = 15
        termini_str = [r"x"]
        negative = True
        for i in range(3,n+1,2):
            if negative:
                sign = "-"
                negative = False
            else:
                sign = "+"
                negative = True
            termini_str.append(rf"{sign}\frac{{x^{{{i}}}}}{{{i}!}}")

        prec_formula = MathTex(termini_str[0]).set_x(0).shift(DOWN*3.25)
        prec_poly = ax.plot(lambda x: x, x_range = [x_min, x_max], color = RED_E)
        self.play(Write(prec_formula), Create(prec_poly),run_time = 2.5)

        for i in range(1,len(termini_str)+1):
            curr_poly = ax.plot(genera_polinomio(sin_McLaurin(2*i+1)), x_range = [x_min, x_max], color = RED_E)
            if i == len(termini_str):
                curr_formula = MathTex(*termini_str[0:i+1], r"\text{ }\cdots").set_x(0).shift(DOWN * 3.25)
            else:
                curr_formula = MathTex(*termini_str[0:i+1]).set_x(0).shift(DOWN*3.25)
            self.play(TransformMatchingTex(prec_formula, curr_formula),
                      ReplacementTransform(prec_poly,curr_poly),
                      run_time = 2.5)
            prec_formula = curr_formula
            prec_poly = curr_poly
        self.wait(3)