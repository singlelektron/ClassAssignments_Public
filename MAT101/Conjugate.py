from manim import *

class ConjugateRootProof(Scene):
    def construct(self):
        # 1. Introduce the polynomial P(z)
        title = Title("Proof of the Conjugate Root Theorem", color=YELLOW)
        self.play(Write(title))
        self.wait(0.5)

        # The MathTex object is created and parts are isolated
        poly_def = MathTex(
            r"P(z) = a_{n}z^{n}+a_{n-1}z^{n-1}+\cdots +a_{1}z+a_{0}",
            substrings_to_isolate=["a_{n}", "a_{n-1}", "a_{1}", "a_{0}"]
        ).scale(0.9).to_edge(UP, buff=1.5)

        # ----------------------------------------------------
        # FIX IS HERE: Use .submobjects instead of .subobjects[0].subobjects
        # ----------------------------------------------------
        for part in poly_def.submobjects:
            # Check if the isolated part starts with 'a_' to identify coefficients
            if part.get_tex_string().startswith('a_'):
                 part.set_color(BLUE) # Highlight coefficients in blue
        # ----------------------------------------------------

        constraint = MathTex(
            r"\text{Where } a_k \in \mathbb{R} \text{ (Real coefficients)}",
            color=BLUE
        ).next_to(poly_def, DOWN, buff=0.3, aligned_edge=LEFT).scale(0.8)

        self.play(Write(poly_def))
        self.play(FadeIn(constraint, shift=UP))
        self.wait(10)
        
        # 2. Set the condition P(alpha) = 0
        alpha = MathTex(r"\text{Let } \alpha = a+bi \text{ be a root of } P(z)=0").next_to(poly_def, DOWN, buff=0.5, aligned_edge=LEFT)
        
        condition = MathTex(
            r"P(\alpha) = a_{n}\alpha^{n}+\cdots +a_{0} = 0"
        ).scale(0.9).next_to(alpha, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(
            FadeOut(constraint)
        )
        self.play(
            Write(alpha)
        )
        self.wait(10)
        self.play(
            Write(condition)
        )
        self.wait(10)

        # 3. Take the conjugate of both sides
        self.play(FadeOut(alpha))

        self.play(condition.animate.next_to(poly_def, DOWN))

        condition_copy = MathTex(
            r"P(\alpha) = a_{n}\alpha^{n}+\cdots +a_{0} = 0"
        ).scale(0.9).next_to(condition, DOWN, aligned_edge=LEFT)
        
        conjugate_step = MathTex(
            r"\overline{P(\alpha)} = \overline{a_{n}\alpha^{n}+\cdots +a_{0}} = \overline{0}"
        ).next_to(condition, DOWN, aligned_edge=LEFT).scale(0.9)

        self.play(
            ReplacementTransform(
                condition_copy, 
                conjugate_step
            )
        )
        self.wait(10)
        
        # 4. Apply the properties of the conjugate (Sum Rule)
        conjugate_step_2 = MathTex(
            r"\overline{a_{n}\alpha^{n}} + \overline{a_{n-1}\alpha^{n-1}} + \cdots + \overline{a_{0}} = 0"
        ).scale(0.9).move_to(conjugate_step)
        
        self.play(
            ReplacementTransform(
                conjugate_step,
                conjugate_step_2
            )
        )
        self.wait(10)

        # 5. Apply the properties of the conjugate (Product Rule)
        conjugate_step_3 = MathTex(
            r"\overline{a_{n}}\overline{\alpha}^{n} + \overline{a_{n-1}}\overline{\alpha}^{n-1} + \cdots + \overline{a_{0}} = 0"
        ).scale(0.9).move_to(conjugate_step_2)

        self.play(
            ReplacementTransform(conjugate_step_2, conjugate_step_3),
            # FadeOut(conjugate_step_2)
        )
        self.wait(10)
        
        # 6. Substitute the Real Coefficient property
        conjugate_step_4 = MathTex(
            r"a_{n}\overline{\alpha}^{n} + a_{n-1}\overline{\alpha}^{n-1} + \cdots + a_{0} = 0"
        ).scale(0.9).move_to(conjugate_step_3)
        
        self.play(
            ReplacementTransform(conjugate_step_3, conjugate_step_4)
        )
        self.wait(10)
        
        # 7. Final Conclusion
        final_form = MathTex(
            r"P(\overline{\alpha}) = 0"
        ).scale(1.5).next_to(poly_def, DOWN, buff=1.0)
        
        final_result = MathTex(
            r"\text{Therefore, } P(a-bi) = 0",
            color=GREEN_C
        ).scale(1.5).next_to(final_form, DOWN, buff=0.5)
        
        self.play(
            ReplacementTransform(conjugate_step_4, final_form),
            FadeOut(poly_def),
            FadeOut(condition)
        )
        self.wait(10)
        self.play(
            Write(final_result)
        )
        self.play(
            Circumscribe(final_result, color=GREEN, run_time=2),
            Flash(final_result, color=GREEN)
        )
        self.wait(2)
        self.play(FadeOut(*self.mobjects))