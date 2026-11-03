#proviamo a visualizzare la dimostrazione del th. di Pitagora
from manim import *
from math import sqrt

class TeoremaPitagora(Scene):
    def construct(self):
        l = 2.5
        lato_a = Line([0,0,0], [l,0,0])
        lato_b = Line([0,0,0], [0,l,0])
        lato_c = Line([l,0,0], [0,l,0])
        trig_rett = VGroup(lato_a,lato_b,lato_c, color = BLUE)
        trig_rett.move_to(ORIGIN)
        self.play(Create(trig_rett), run_time = 1.5)


        self.next_section("Aggiungo le etichette in LaTeX")
        a = MathTex("a", color = RED)
        b = MathTex("b", color = BLUE)
        c = MathTex("c", color = GREEN)
        lettere = VGroup(a,b,c)
        a.next_to(lato_a, DOWN)
        b.next_to(lato_b, LEFT)
        c.move_to(lato_c.get_center())
        c.shift(UP * 0.3 + RIGHT * 0.2)
        self.play(Write(a), Write(b), Write(c), run_time = 2)

        self.next_section("Aggiungo i quadrati", skip_animations = False)
        q_a = Square(side_length = lato_a.get_length())
        q_b = Square(side_length = lato_b.get_length())
        q_c = Square(side_length = lato_c.get_length())
        q_a.set_fill(RED, opacity = 0.2)
        q_b.set_fill(BLUE, opacity=0.2)
        q_c.set_fill(GREEN, opacity=0.2)
        q_c.rotate(lato_c.get_angle())
        q_a.next_to(lato_a, DOWN, buff = 0.01)
        q_b.next_to(lato_b, LEFT, buff = 0.01)
        q_c.move_to(lato_c.get_center())
        q_c.shift((UP+RIGHT) * lato_c.get_length() * 0.36)
        self.play(Create(q_a), Create(q_b), run_time = 2)

        formula = MathTex("a^{2}", "+", "b^{2}", "=", "c^{2}")
        formula[0].color = RED
        formula[2].color = BLUE
        formula[4].color = GREEN
        formula_originale = formula.copy()

        formula[0].move_to(q_a)
        formula[2].move_to(q_b)
        self.play(Transform(a,formula[0]), Transform(b,formula[2]))

        q_cateti = VGroup(q_a,q_b)
        self.play(TransformFromCopy(q_cateti,q_c), run_time = 2)

        formula[4].move_to(q_c)
        self.play(Transform(c, formula[4]))

        formula_originale.to_edge(UP)
        formula_originale.shift(LEFT*3 + DOWN)
        cornice = SurroundingRectangle(formula_originale, buff = 0.2, color = WHITE, corner_radius = 0.05)

        self.play(TransformFromCopy(a,formula_originale[0]),
                  TransformFromCopy(b,formula_originale[2]),
                  TransformFromCopy(c,formula_originale[4]),
                  Write(formula_originale[1]), Write(formula_originale[3]), run_time = 2)
        #titolo = MathTex(r"\mathbb{T} \text{eorema di }\mathbb{P}\text{itagora}")
        #titolo.to_edge(DOWN + RIGHT)
        #self.play(Create(cornice), Write(titolo), run_time = 1.5)
        self.wait(3)

