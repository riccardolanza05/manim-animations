from manim import *
from random import *
from itertools import accumulate
import random as rm
from math import *

def simula_lanci(n):
    risultati = [rm.choice([0,1]) for i in range(n)]
    somme_cumulate = list(accumulate(risultati))
    medie = [somme_cumulate[i]/(i+1) for i in range(n)]
    return [(n_lanci,media) for n_lanci,media in zip(range(1,n+1),medie)]

class LeggeForteGrandiNumeri(Scene):
    def construct(self):
        self.next_section("Titolo")
        titolo = MathTex(r"\mathbb{S}\text{trong } \mathbb{L}\text{aw of}", font_size = 100).move_to(ORIGIN).shift(UP*0.5)
        sottotitolo = MathTex(r"\mathbb{L}\text{arge }",r"\mathbb{N}\text{umbers}", font_size = 100).move_to(ORIGIN).shift(DOWN*0.5)
        sottotitolo.set_color(RED_D)
        self.play(Write(titolo), Write(sottotitolo), run_time = 2)
        self.wait()
        self.play(FadeOut(titolo), FadeOut(sottotitolo))

        self.next_section("Monetina")
        esito = rm.choice([0,1])
        testa = MathTex("0")
        croce = MathTex("1")
        dubbio = MathTex("?")
        moneta_dubbio = VGroup(dubbio,Circle()).move_to(ORIGIN)
        moneta_1 = VGroup(croce,Circle()).move_to(ORIGIN)
        moneta_0 = VGroup(testa, Circle()).move_to(ORIGIN)
        self.play(FadeIn(moneta_dubbio), run_time=2)
        self.play(moneta_dubbio.animate.stretch(0, dim=0), run_time=2)
        if esito == 1:
            moneta_dubbio.become(moneta_1)
        else:
            moneta_dubbio.become(moneta_0)
        self.play(moneta_dubbio.animate.stretch(1, dim=0), run_time=2)
        self.wait()
        self.play(FadeOut(moneta_dubbio))

        self.next_section("Costruzione assi e retta tratteggiata")
        n_sim = 500
        ax = Axes(
            x_range = [0, n_sim, n_sim/10],
            y_range = [0,1, 0.5],
            tips = False,
            x_axis_config = {"include_numbers" : True,
                           "decimal_number_config" : {"num_decimal_places":0}},
            y_axis_config={"include_numbers": True,
                           "decimal_number_config": {"num_decimal_places": 1}},
        )

        linea_media = DashedLine(ax.c2p(0,0.5), ax.c2p(n_sim,0.5),
                                 dash_length=0.1, dashed_ratio=0.65, color = RED_E)
        self.play(Create(ax),run_time = 2)
        self.play( Create(linea_media))

        self.next_section("Simulazione dei dati")
        for color in [BLUE_D, YELLOW_D, GREEN_D, PURPLE_D]:
            x_val , y_val = zip(*simula_lanci(n_sim))
            line_graph = ax.plot_line_graph(x_val,y_val,line_color = color, add_vertex_dots = False)
            self.play(Create(line_graph), run_time = 3)




