from manim import *
from manim_revealjs import PresentationScene

config.background_color = ORANGE
MYGREEN = "#06943C"

class Thumbnail(PresentationScene):
    def construct(self):
        title = Text("Introducción a las funciones", font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=BLACK).to_edge(UP)
        rec = SurroundingRectangle(title, color=MYGREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=1.0, buff=0.3)
        eq = MathTex("f(x)={ {x^2-9}\\over{x+3} }", color=BLACK, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).scale(3)
        text = Text("Explicación completa", color=BLUE_E, font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).to_edge(DOWN)
        self.add(title, rec, eq, text)
        self.bring_to_back(rec)
        self.end_fragment()

Y_AXIS_LENGTH = config.frame_height-3.1
X_AXIS_LENGTH = Y_AXIS_LENGTH*(config.frame_width-2)/(config.frame_height-2)
AXES_CONFIG = {
    "x_range":[0, 24, 2],
    "y_range":[0, 40, 5], 
    "x_axis_config":{
        "color":BLACK,
        "decimal_number_config":{
            "color":BLACK,
            "num_decimal_places":0
        }
    },
    "y_axis_config":{
        "color":BLACK,
        "decimal_number_config":{
            "color":BLACK,
            "num_decimal_places":0
        }
    },
    "x_length":X_AXIS_LENGTH,
    "y_length":Y_AXIS_LENGTH
}

class Approach(PresentationScene):
    def construct(self):
        case = Text("Caso: temperatura del día", font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=BLACK).to_edge(UP)
        rec = SurroundingRectangle(case, color=MYGREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=1.0, buff=0.3)
        self.bring_to_back(rec)
        self.play(DrawBorderThenFill(rec))
        self.play(Write(case))
        self.end_fragment()
        ax = Axes(**AXES_CONFIG).add_coordinates().to_edge(DOWN)
        labels = ax.get_axis_labels(Tex("$t$ (h)", color=BLACK), Tex("$T$ (\\textdegree C)", color=BLACK))
        self.play(Write(ax))
        self.play(Write(labels))
        self.end_fragment()
        def func(x):
            if 0<=x<7:
                return -1/7*x+2.5
            if 7<=x<11:
                return 8.5/4*(x-7)+1.5
            if 11<=x<16:
                return 4*(x-11)+10
            if 16<=x<21:
                return -3*(x-16)+30
            if 21<=x<=24:
                return -11.5/3*(x-21)+15
        graph = ax.get_graph(function=func, x_range=[0,24], color=BLUE_E, use_smoothing=True)
        self.play(Create(graph))
        self.end_fragment()
        xvaltracker = ValueTracker(12)
        graph_label = ax.get_graph_label(graph=graph, x_val=xvaltracker.get_value(), label=MathTex("(t, T(t))"), direction=UP, dot=True, dot_config={"color":BLACK})
        graph_label.add_updater(lambda m: m.become(ax.get_graph_label(graph=graph, x_val=xvaltracker.get_value(), label=MathTex("(t, T(t))"), direction=UP, dot=True, dot_config={"color":BLACK})))
        self.play(Write(graph_label))
        self.end_fragment()
        self.play(xvaltracker.animate(run_time=2).set_value(23))
        self.end_fragment()
        xline = ax.get_vertical_line(ax.c2p(xvaltracker.get_value(), func(xvaltracker.get_value())), color=MYGREEN)
        yline = ax.get_horizontal_line(ax.c2p(xvaltracker.get_value(), func(xvaltracker.get_value())), color=MYGREEN)
        self.play(Create(xline), Create(yline))
        self.end_fragment()

class Approach2(PresentationScene):
    def construct(self):
        case = Text("Caso: costo del viaje en taxi", font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=BLACK).to_edge(UP)
        rec = SurroundingRectangle(case, color=MYGREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=1.0, buff=0.3)
        self.bring_to_back(rec)
        self.play(DrawBorderThenFill(rec))
        self.play(Write(case))
        self.end_fragment()
        text = Text("Tarifa inicial: $280.", color=BLACK, font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).scale(0.5)
        text2 = Text("Si el taxi está recorriendo, el costo total del viaje aumenta.\nPor cada tramo recorrido de 200 m el viaje cuesta $60 más\nque al inicio de éste.", color=BLACK, font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).scale(0.5)
        group = VGroup(text, text2).arrange(DOWN).next_to(rec, DOWN)
        self.play(Write(text))
        self.end_fragment()
        self.play(Write(text2))
        self.end_fragment()
        f_function = MathTex("C(s)=60s+280", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE).scale(2)
        self.play(Write(f_function))
        self.end_fragment()
        f_exp1 = MathTex("C(5)=60(5)+280", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp2 = MathTex("C(5)=580", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exps = VGroup(f_exp1, f_exp2).arrange(DOWN).to_edge(DOWN)
        self.play(Write(f_exp1))
        self.end_fragment()
        self.play(TransformMatchingTex(f_exp1.copy(), f_exp2))
        self.play(Circumscribe(f_exp2))
        self.end_fragment()
        self.play(FadeOut(f_exp1), FadeOut(f_exp2))
        self.end_fragment()
        f_exp3 = MathTex("1000=60s+280", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp4 = MathTex("1000-280=60s+280-280", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp5 = MathTex("720=60s", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp6 = MathTex("\\frac{720}{60}=\\frac{60s}{60}", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp7 = MathTex("12=s", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exp8 = MathTex("s=12", color=BLUE_E, stroke_width=1.0, stroke_opacity=1.0, stroke_color=WHITE)
        f_exps2 = VGroup(f_exp3, f_exp6).arrange(DOWN).to_edge(DOWN)
        f_exp4.next_to(f_exp3, DOWN)
        f_exp5.next_to(f_exp3, DOWN)
        f_exp7.next_to(f_exp3, DOWN)
        f_exp8.next_to(f_exp3, DOWN)
        self.play(Write(f_exp3))
        self.end_fragment()
        self.play(TransformMatchingTex(f_exp3.copy(), f_exp4), run_time=0.5)
        self.play(TransformMatchingTex(f_exp4, f_exp5), run_time=0.5)
        self.play(TransformMatchingTex(f_exp5, f_exp6), run_time=0.5)
        self.play(TransformMatchingTex(f_exp6, f_exp7), run_time=0.5)
        self.play(TransformMatchingTex(f_exp7, f_exp8), run_time=0.5)
        self.play(Circumscribe(f_exp8))
        self.end_fragment()

class Definition(PresentationScene):
    def construct(self):
        definition = Text("Definición de función", font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=BLACK).to_edge(UP)
        rec = SurroundingRectangle(definition, color=MYGREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=1.0, buff=0.3)
        self.bring_to_back(rec)
        self.play(DrawBorderThenFill(rec))
        self.play(Write(definition))
        self.end_fragment()
        thed = Tex("Una función real $f:A\\rightarrow B$ es una regla que asigna a cada elemento $x\\in A$\\\\un único elemento $y\\in B$. Al ser $y$ un valor que corresponde a un $x$ determinado por la función $f$,se le denota por $f(x)$, es decir, $y=f(x)$.\\\\Debe cumplirse $A\\subseteq\\mathbb{R}$ y $B\\subseteq\\mathbb{R}$.", color=BLUE_E, stroke_width=0.5, stroke_opacity=1.0, stroke_color=WHITE).scale(0.7)
        self.play(Write(thed))
        self.end_fragment()
        imp = MathTex("\\mathrm{dom}(f)=A", color=BLUE_E, stroke_width=0.5, stroke_opacity=1.0, stroke_color=WHITE).scale(0.7)
        imp2 = MathTex("\\mathrm{cod}(f)=B", color=BLUE_E, stroke_width=0.5, stroke_opacity=1.0, stroke_color=WHITE).scale(0.7)
        imp3 = MathTex("\\mathrm{rec}(f)=\\{f(x):x\\in A\\}", color=BLUE_E, stroke_width=0.5, stroke_opacity=1.0, stroke_color=WHITE).scale(0.7)
        imp4 = MathTex("G(f)=\\{(x,f(x)):x\\in A\\}", color=BLUE_E, stroke_width=0.5, stroke_opacity=1.0, stroke_color=WHITE).scale(0.7)
        group = VGroup(imp, imp2, imp3, imp4).arrange(DOWN).to_edge(DOWN)
        self.play(Write(imp))
        self.end_fragment()
        self.play(Write(imp2))
        self.end_fragment()
        self.play(Write(imp3))
        self.end_fragment()
        self.play(Write(imp4))
        self.end_fragment()

class YTThumbnail(Scene):
    def construct(self):
        title = Text("Introducción a las funciones", font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=BLACK).to_edge(UP)
        rec = SurroundingRectangle(title, color=MYGREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_opacity=1.0, buff=0.3)
        eq = MathTex("f(x)={ {x^2-9}\\over{x+3} }", color=BLACK, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).scale(3)
        text = Text("Explicación completa", color=BLUE_E, font="Orbitron", weight=BOLD, stroke_width=2.0, stroke_opacity=1.0, stroke_color=WHITE).to_edge(DOWN)
        self.add(title, rec, eq, text)
        self.bring_to_back(rec)
