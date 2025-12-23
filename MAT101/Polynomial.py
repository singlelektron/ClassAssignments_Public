from manim import *

class PolynomialRootProof(Scene):
    def construct(self):
        # 1. Title and Introduction
        title = Text("Inductive Proof: n-degree Polynomial has n Roots", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # General form of the polynomial - FIX APPLIED HERE
        poly_form_tex = r"P(z) = a_{n}z^{n}+a_{n-1}z^{n-1}+\cdots +a_{1}z+a_{0} \quad \left(a_n \neq 0\right)"
        poly_form = MathTex(poly_form_tex).next_to(title, DOWN, buff=0.5)
        self.play(Write(poly_form))
        self.wait(1)

        # --- Transition ---
        self.play(poly_form.animate.to_edge(UP).shift(DOWN*0.5), title.animate.set_opacity(0))
        self.wait(10)

        # 2. Base Case (n=1)
        base_case_title = Text("Ⅰ. Base Case (n=1)", font_size=32).to_edge(LEFT).shift(UP*1.5)
        self.play(Write(base_case_title))
        
        # n=1 equation
        n1_eq = MathTex(r"P_1(z) = a_1 z + a_0").next_to(base_case_title, DOWN, aligned_edge=LEFT)
        self.play(Write(n1_eq))
        self.wait(5)
        
        # Solution
        solution = MathTex(r"z = -\frac{a_0}{a_1} \quad \Rightarrow \quad 1 \text{ Root}").next_to(n1_eq, DOWN, aligned_edge=LEFT)
        self.play(Write(solution))
        self.wait(10)
        
        # Base case summary
        base_summary = Text("Conclusion: True for n=1.", font_size=30, color=GREEN).next_to(solution, DOWN, aligned_edge=LEFT).shift(DOWN*0.5)
        self.play(Write(base_summary))
        self.wait(10)

        # 3. Inductive Hypothesis (n=k)
        self.play(FadeOut(base_case_title, n1_eq, solution, base_summary))
        
        hypo_title = Text("Ⅱ. Inductive Hypothesis (Assume True for n=k)", font_size=32).to_edge(LEFT).shift(UP*1.5)
        self.play(Write(hypo_title))
        
        hypo_text = VGroup(
            MathTex(r"\text{Assume k-degree polynomial }P_k(z)\text{ has k complex roots.}", font_size=30),
            MathTex(r"P_k(z) = a_k(z-r_1)(z-r_2)\cdots(z-r_k)").scale(0.9)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(hypo_title, DOWN, aligned_edge=LEFT)
        
        self.play(Write(hypo_text))
        self.wait(10)

        # 4. Inductive Step (n=k+1)
        self.play(FadeOut(hypo_title, hypo_text))
        
        step_title = Text("Ⅲ. Inductive Step (Prove True for n=k+1)", font_size=32).to_edge(LEFT).shift(UP*1.5)
        self.play(Write(step_title))
        
        step_part1 = MathTex(r"\text{Consider the (k+1)-degree polynomial }P_{k+1}(z)", font_size=30).next_to(step_title, DOWN, aligned_edge=LEFT)
        self.play(Write(step_part1))
        self.wait(10)
        
        # Using the Fundamental Theorem of Algebra to guarantee one root r_{k+1}
        theorem_call = Text("By the Fundamental Theorem of Algebra:", font_size=28, color=YELLOW).next_to(step_part1, DOWN, aligned_edge=LEFT)
        root_exists = MathTex(r"\text{There exists at least one root }r_{k+1}\text{.}", font_size=30).next_to(theorem_call, DOWN, aligned_edge=LEFT)
        self.play(Write(theorem_call))
        self.play(Write(root_exists))
        self.wait(10)

        self.play(FadeOut(step_part1, theorem_call))
        self.play(root_exists.animate.next_to(step_title, DOWN, aligned_edge=LEFT))

        # Factor Theorem
        factor_theorem_title = Text("By the Factor Theorem:", font_size=28, color=YELLOW).next_to(root_exists, DOWN, aligned_edge=LEFT)
        
        division_eq_1 = MathTex(r"P_{k+1}(z) = (z-r_{k+1}) \cdot Q(z)").next_to(factor_theorem_title, DOWN, aligned_edge=LEFT).scale(0.95)
        division_eq_2 = MathTex(r"\quad \text{where } Q(z) \text{ is a } k \text{-degree polynomial}").next_to(division_eq_1, DOWN, aligned_edge=LEFT).scale(0.95)


        self.play(Write(factor_theorem_title))
        self.play(Write(division_eq_1))
        self.play(Write(division_eq_2))
        self.wait(10)

        self.play(FadeOut(root_exists, factor_theorem_title, division_eq_2))
        self.play(division_eq_1.animate.next_to(step_title, DOWN, aligned_edge=LEFT))


        # Applying Inductive Hypothesis
        apply_hypo_title = Text("Apply Inductive Hypothesis:", font_size=30, color=BLUE).next_to(division_eq_1, DOWN, aligned_edge=LEFT)
        apply_hypo_text = MathTex(r"Q(z)\text{ has k roots }r_1, r_2, \ldots, r_k\text{.}", font_size=30).next_to(apply_hypo_title, DOWN, aligned_edge=LEFT)
        
        self.play(Write(apply_hypo_title))
        self.play(Write(apply_hypo_text))
        self.wait(10)
        
        # Final factored form
        final_form_title = MathTex(r"\text{Thus, }P_{k+1}(z)\text{ is completely factored:}", font_size=30).next_to(apply_hypo_text, DOWN, aligned_edge=LEFT)
        final_form = MathTex(
            r"P_{k+1}(z) = a_{k+1}(z-r_1)(z-r_2)\cdots(z-r_k)(z-r_{k+1})"
        ).scale(0.9).next_to(final_form_title, DOWN, aligned_edge=LEFT)
        
        self.play(Write(final_form_title))
        self.play(Write(final_form))
        
        # Final count summary
        final_count = Text("Total of k+1 roots.", font_size=35, color=GREEN).next_to(final_form, DOWN, buff=0.7)
        self.play(Write(final_count))
        self.wait(10)

        # 5. Conclusion
        conclusion = Text("Conclusion: For any n, an n-degree polynomial has n roots.", font_size=40, color=RED).move_to(ORIGIN)
        self.play(FadeOut(Group(*self.mobjects), run_time=1))
        self.play(Write(conclusion))
        self.wait(10)