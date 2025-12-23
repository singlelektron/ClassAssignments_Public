from manim import *

class VietaGeneralFormulaProof(Scene):
    def construct(self):
        # 1. Setup and Definition
        title = Title("Proof of Vieta's General Formulas")
        self.play(Write(title))
        self.wait(10)

        # Standard polynomial form (I) - Reduced scale for space
        Pz_standard = MathTex(
            "P(z) = a_{n}z^{n}", 
            "+", 
            "a_{n-1}z^{n-1}", 
            "+", 
            "a_{n-2}z^{n-2}", # New term for k=2
            "+", 
            "\\cdots", 
            "+", 
            "a_{0}"
        ).to_edge(UP).shift(DOWN).scale(0.8)
        
        # Factored form (II) - Reduced scale for space
        Pz_factored = MathTex(
            "P(z) = a_n (z - z_1)(z - z_2)\\cdots(z - z_n)"
        ).next_to(Pz_standard, DOWN, aligned_edge=LEFT).scale(0.8)
        
        self.play(
            Write(Pz_standard)
        )
        self.wait(10)
        self.play(
            Write(Pz_factored)
        )
        self.wait(10)
        
        comparison_header = Text("Comparing Coefficients from (I) and (II)").next_to(Pz_factored, DOWN).scale(0.8)
        self.play(Write(comparison_header))
        self.wait(10)

        # --- k = 1: Sum of Roots ---
        
        k1_title = MathTex(r"\text{k=1: Sum of Roots (Coefficient of }z^{n-1}\text{)}").next_to(comparison_header, DOWN, aligned_edge=LEFT).scale(0.6).set_color(BLUE)
        self.play(Write(k1_title))
        
        # Highlight a_{n-1}
        self.play(Indicate(Pz_standard[2], scale_factor=1.2, color=YELLOW))

        # Coefficient from factored form: $a_n \cdot (-z_1 - z_2 - \cdots - z_n)$
        k1_coeff_factored = MathTex("a_{n-1}", "=", "-a_n \\sum_{i=1}^{n} z_i").next_to(k1_title, DOWN)
        self.play(Write(k1_coeff_factored))
        self.wait(10)
        
        k1_formula = MathTex("\\sum_{i=1}^{n} z_i", "=", "-\\frac{a_{n-1}}{a_n}").next_to(k1_coeff_factored, DOWN).set_color(GREEN)
        self.play(ReplacementTransform(k1_coeff_factored, k1_formula))
        self.wait(10)
        
        # --- k = 2: Sum of Pairwise Products ---

        self.play(
            FadeOut(k1_formula),
            FadeOut(k1_title)
        )
        
        k2_title = MathTex(r"\text{k=2: Sum of Pairwise Products (Coefficient of }z^{n-2}\text{)}").next_to(comparison_header, DOWN).scale(0.6).set_color(ORANGE)
        self.play(Write(k2_title))
        
        # Highlight a_{n-2}
        self.play(Indicate(Pz_standard[4], scale_factor=1.2, color=YELLOW))
        
        # Explanation of $z^{n-2}$ term: selecting -z_i and -z_j
        # Coefficient from factored form: $a_n \cdot \sum_{i<j} (-z_i)(-z_j) = a_n \sum_{i<j} z_i z_j$
        k2_coeff_factored = MathTex("a_{n-2}", "=", "a_n \\sum_{1 \\le i < j \\le n} z_i z_j").next_to(k2_title, DOWN)
        self.play(Write(k2_coeff_factored))
        self.wait(10)
        
        k2_formula = MathTex("\\sum_{1 \\le i < j \\le n} z_i z_j", "=", "\\frac{a_{n-2}}{a_n}").next_to(k2_coeff_factored, DOWN).set_color(GREEN)
        self.play(ReplacementTransform(k2_coeff_factored, k2_formula))
        self.wait(10)

        # --- Generalization (k=m) ---
        
        self.play(
            FadeOut(k2_formula),
            FadeOut(k2_title)
        )
        
        general_title = MathTex(r"\text{Generalization: Coefficient of }z^{n-k}").next_to(comparison_header, DOWN).scale(0.6).set_color(PURPLE)
        self.play(Write(general_title))
        
        # 3.1. Explaining the general coefficient (a_{n-k})
        # The z^{n-k} term is formed by choosing $k$ factors of $-z_i$ and $n-k$ factors of $z$.
        general_coeff_text = MathTex(
            "\\text{The coefficient } a_{n-k} \\text{ involves choosing } k \\text{ roots } (-z_{i_1})\\cdots(-z_{i_k})",
        ).next_to(general_title, DOWN).scale(0.7)
        
        self.play(Write(general_coeff_text))
        
        # Sign check: $(-1)^k$
        sign_check = MathTex("\\text{Sign: } (-1)^k").next_to(general_coeff_text, DOWN).scale(0.7).set_color(RED)
        self.play(Write(sign_check))
        self.wait(10)

        # 3.2. Vieta's General Formula
        
        # Fade out previous details for the final grand reveal
        self.play(
            FadeOut(comparison_header),
            FadeOut(general_title),
            FadeOut(general_coeff_text),
            FadeOut(sign_check),
            FadeOut(Pz_standard),
            FadeOut(Pz_factored),
        )

        final_title = Text("Vieta's General Formulas").center().to_edge(UP).set_color(YELLOW)
        
        # General Formula (k-th elementary symmetric polynomial)
        final_formula = MathTex(
            r"\sum_{1 \le i_1 < \cdots < i_k \le n} z_{i_1} z_{i_2} \cdots z_{i_k}", 
            "=", 
            r"(-1)^k \frac{a_{n-k}}{a_n}", 
            r"\quad \text{for } k=1, 2, \cdots, n"
        ).next_to(final_title, DOWN, buff=1.0).scale(1).set_color(GREEN)
        
        # Re-introduce title and final formula
        self.play(
            Transform(title, final_title)
        )
        self.wait(10)
        
        self.play(Write(final_formula), run_time=3)
        self.wait(10)
        