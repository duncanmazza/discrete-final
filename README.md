# Discrete Convex Analysis
*A class project by [Duncan Mazza](https://github.com/duncanmazza) and [Colin Snow](https://github.com/colinmsnow) for [MTH2110 Discrete Math](https://olin.smartcatalogiq.com/en/2018-19/Catalog/Courses-Credits-Hours/MTH-Mathematics/2000/MTH2110) at [Olin College](https://olin.edu)*

## Background

Our class project culminated in a presentation to the class on discrete convex analysis, the topic of our exploration. The presentation had an accompanying slide deck which contained various animations that were used to explain the technical definition of L-natural convexity of functions on the 2-dimensional integers and the Legendre-Fenchel transform. These animations were created using the [Manim Community](https://github.com/ManimCommunity/manim) library.

Our primary technical reference:

> K.  Murota,  “Main  features  of  discrete  convex  analysis,”  Jun  2018.[Online].   Available: [https://www.comp.tmu.ac.jp/kzmurota/paper/rimsCOSS2018/COSS2018chap1.pdf](https://www.comp.tmu.ac.jp/kzmurota/paper/rimsCOSS2018/COSS2018chap1.pdf)

## Directory

- [convexity_1d.py](discrete/convexity_1d.py): Animation showing the convexity definition for a discrete function on the 1-dimensional integers.
- [convexity_2d.py](discrete/convexity_2d.py): Animation showing L-natural convexity for a discrete function on the 2-dimensional integers.
- [fruits_example.py](discrete/fruits_example.py): Brute-force search of optimal solution for the fruit-buying example described in the presentation. This example was designed to reflect the Gross Substitutes Property in Economics.
- [legendre.py](discrete/legendre.py): Animations explaining the Legendre-Fenchel transform.

## Usage

Documentation on installing the requisite libraries and generating the animations can be found at [Manim Community documentation](https://www.manim.community/) page.
