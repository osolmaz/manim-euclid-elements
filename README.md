# Euclid's Elements with Manim

This repo contains code that can auto-generate a video rendering of [Euclid's Elements](https://en.wikipedia.org/wiki/Euclid%27s_Elements):

> The Elements (Ancient Greek: Στοιχεῖα Stoikheîa) is a mathematical treatise consisting of 13 books attributed to the ancient Greek mathematician Euclid in Alexandria, Ptolemaic Egypt c. 300 BC. It is a collection of definitions, postulates, propositions (theorems and constructions), and mathematical proofs of the propositions. The books cover plane and solid Euclidean geometry, elementary number theory, and incommensurable lines. Elements is the oldest extant large-scale deductive treatment of mathematics. It has proven instrumental in the development of logic and modern science, and its logical rigor was not surpassed until the 19th century.

For example, the Pythagorean Theorem is rendered as:

https://user-images.githubusercontent.com/2453968/203163757-e6307b2d-5c82-4bf9-9fb3-51851c014b3c.mp4

## How?

This was possible thanks to the meticulous work performed by [Ibrahim Sagiroglu](https://twitter.com/ratherthanpaper) in [his own browser-based interactive rendering](https://elements.canberead.com/):

- [Sagiroglu's machine readable source](https://github.com/ibrahimsag/canberead) provides all the geometry and proposition information.
- Animations are auto-generated using the math animation library [Manim](https://manim.community).
- Voiceovers are also auto-generated using AI with the [Manim Voiceover](https://voiceover.manim.community) plugin (also authored by me).

Another example that is in 3d:

https://user-images.githubusercontent.com/2453968/203164845-34aff154-ded5-401f-a7b1-fd442703a771.mp4

## Details

This is an experiment to invent new and automatic ways of making knowledge more accessible. It will improve over time.

Current stats:

- Coverage: 228/465 propositions
- Total duration: ~12.5 hrs

I currently use YouTube to host the entire book:

- Part 1 (Books 1-11, ~9.5 hrs): https://youtu.be/c3Tg5GX9jOg
- Part 2 (Books 12-13, ~3 hrs): https://youtu.be/wxfc2CAdTlI

## License

MIT
