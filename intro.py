from ctypes import alignment
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

LEFT_EDGE = -5.5
LINE_SPACING = 0.75

class Introduction(VoiceoverScene):
    def construct(self):

        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            ),
            create_subcaption=False,
        )

        # self.add_sound("audio/1-second-of-silence.mp3")
        text1 = Tex("Euclid's Elements", font_size=72)
        text2 = Tex("A Video Rendering", font_size=48)
        text3 = Tex("version 0.0.2", font_size=24).align_on_border(DR)
        VGroup(text1, text2).arrange(DOWN, buff=1)
        with self.voiceover(text="Euclid's Elements") as tracker:
            self.play(Write(text1), run_time=2)
        self.wait()

        with self.voiceover(text="A video rendering") as tracker:
            self.play(Write(text2), Write(text3), run_time=tracker.duration)
        self.wait()
        self.play(Unwrite(text1), Unwrite(text2), Unwrite(text3))
        self.wait()

        text1 = Tex(
            r"\textsf{Around 310 BC in Ancient Greece, Euclid of Megara compiled\\a book of geometry called Stoikheîa, translated into English as Elements.}",
            # line_spacing=LINE_SPACING,
            font_size=36,
        )
        text2 = Tex(
            r"\textsf{Over the next 2300 years became the foundation of mathematical education.\\Its number of editions surpass 1000, being second only to the Bible.}",
            # line_spacing=LINE_SPACING,
            font_size=36,
        )
        text3 = Tex(
            r"\textsf{In 2007, Richard Fitzpatrick published an English translation of Elements on his website, which itself is based on Johan Ludvig Heiberg's 1883 edition.}",
            # line_spacing=LINE_SPACING,
            font_size=36,
        )

        VGroup(text1, text2, text3).arrange(DOWN, buff=1)
        self.play(FadeIn(text1), run_time=2)
        self.wait(5)
        self.play(FadeIn(text2), run_time=2)
        self.wait(5)
        self.play(FadeIn(text3), run_time=2)
        self.wait(5)
        self.play(FadeOut(text1, text2, text3))

        text1 = Tex(
            r"\textsf{In 2022, Ibrahim Sagiroglu converted Fitzpatrick's edition into an interactive website after 2 years of work. You can find it under \texttt{canberead.com/elements}.}",
            font_size=36,
        )
        text2 = Tex(
            r"\textsf{We used the open source Python math animation library \textbf{Manim} to auto-convert Elements into video, using Sagiroglu's machine-readable source.}",
            font_size=36,
        )
        text3 = Tex(
            r"\textsf{This project evolves continuously, and we hope that it will set an example in making the world's knowledge more accessible. You can find the source under \texttt{github.com/osolmaz/manim-euclid-elements}}",
            font_size=36,
        )

        VGroup(text1, text2, text3).arrange(DOWN, buff=1)
        self.play(FadeIn(text1), run_time=2)
        self.wait(5)
        self.play(FadeIn(text2), run_time=2)
        self.wait(5)
        self.play(FadeIn(text3), run_time=2)
        self.wait(5)
        self.play(FadeOut(text1, text2, text3))

        self.wait()


Introduction.__name__ = "00-01"
