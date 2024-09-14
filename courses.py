#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, Post
from http.cookies import SimpleCookie
import os

if __name__ == "__main__":
	cookies = SimpleCookie(os.environ.get('HTTP_COOKIE', ''))

	print(Document() << [
		Doctype(Html=True),
		Html() << [
			Head() << [
				# Google Analytics
				Script(Src="https://www.googletagmanager.com/gtag/js?id=G-FT6E284Y58", Async=True),
				Script() << [
"""window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-FT6E284Y58');""",
				],
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
				Script(Src="index.js"),
			],
			Body() << [
				Navigate("whitepaper" in cookies),
				Div(Id="main") << [
					A(Id="learn"),
					Div(Id="learn-box", Class="box") << [
						Div(Class="banner") << [
							Div(Class="banner-ri") << [
								Iframe(Style="width: 100%; aspect-ratio: 16 / 9;", Src="https://www.youtube-nocookie.com/embed/videoseries?si=ZFy0bMNimvsltEu2&amp;list=PLUCgknFT8LMilpLkfwXddes_TS0W9XvO-", Title="YouTube video player", Frameborder="0", Allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share", Referrerpolicy="strict-origin-when-cross-origin", Allowfullscreen=True),
							], Div(Class="banner-lt") << [
								H2() << ["Introduction to Self Timed Circuits"],
								P(Style="margin: 0 0 0 0;") << [
									"This course covers the fundamentals of self-timed circuits including timing assumptions and guarantees, failure modes, pipeline structures, data encodings, conditional logic, internal memory, and non-deterministic behavior, hardware description languages for different layers of abstraction, and two design methodologies. It is designed with a bottom up approach, starting with circuitry and working its way up through more abstract representations. Background experience with programming is required, and circuit design is helpful but optional. The course is offered for free with the goal of building local expertise and community in VLSI, Computer Architecture, and Self-Timed Circuits.",
									Div(Id="course-links") << [
										(A(Class="course-link", Href="https://github.com/broccolimicro/course-self-timed-circuits/tree/summer-2023") << "Summer 2023"),
									],
								],
							],
						],

						Div(Class="banner") << [
							Div(Class="banner-li") << [
								Img(Class="feature-img", Src="photo/bcli.png"),
							], Div(Class="banner-rt") << [
								H2() << [
									"Broccoli-CLI ",
								],
								P(Style="margin: 0 0 1rem 0;") << "bcli is a docker container with a full development environment for self-timed circuits. It includes ACT, OpenROAD, Magic, KLayout, Floret, Loom, Xyce, Gaw, and more.",
								H1(Style="margin: 0 0 7rem 0;") << [
									A(Href="https://github.com/broccolimicro/bcli") << Img(Class="img-link", Src="logos/github.png"), " ",
									A(Href="https://hub.docker.com/r/broccolimicro/broccoli-cli") << Img(Class="img-link", Src="logos/docker.svg"),
								],
							],
						],
					],
					



					A(Id="about"),
					Div(Id="about-box", Class="box") << [	
						Div(Class="banner") << [
							Div(Class="banner-bh") << [
								Img(Id="logo-img", Src="logo.svg"),
								P(Style="margin: 5rem 0 5rem 0;") << "<b>Broccoli</b> was founded in December of 2021 to bring about a categorical improvement in compute performance, and we believe that asynchronous design is the next step. With asynchronous design, it is possible to implement complex control that takes advantage of pareto rules in the workload to dramatically improve performance and power. However, asynchronous design has proven to be far too difficult for commercial viability. Our first step toward achieving our mission is to remove that blocker with Loom.",
								Div(Class="contact-card") << [
									Div(Class="contact-photo") << (Div(Class="contact-img-frame") << Img(Class="contact-img", Src="photo/ned.jpg")),
									Div(Class="contact-info") << (P() << [A(Href="https://nedbingham.com") << "Ned Bingham, Founder", Address() << "edward.bingham@broccolimicro.io"]),
								],
							],
						],
					],
	
				],
				Script() << "startWindow();"
			]
		]
	])

