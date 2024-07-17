#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, Post
from http.cookies import SimpleCookie
import os

if __name__ == "__main__":
	cookies = SimpleCookie(os.environ.get('HTTP_COOKIE', ''))

	formItems = []
	if "whitepaper" not in cookies:
		formItems += [
			Input(Type="text", Placeholder="First Name", Name="first", Required=True),
			Input(Type="text", Placeholder="Last Name", Name="last", Required=True), Br(),
			Input(Type="email", Placeholder="Email", name="email", Required=True)
		]
	formItems.append(Input(Id="submit-whitepaper", Type="submit", Value="Read our Whitepaper"))

	form = None
	if "whitepaper" in cookies:
		form = Form(Id="whitepaper-form", Method="post", action="/BroccoliWhitepaper.pdf") << formItems
	else:
		form = Form(Id="whitepaper-form", Method="post", onsubmit="submitWhitepaper(event)") << formItems

	print(Document() << [
		Doctype(Html=True),
		Html() << [
			Head() << [
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
				Script(Src="index.js"),
			],
			Body() << [
				Navigate("whitepaper" in cookies),
				Div(Id="main") << [
					A(Id="products"),
					Div(Id="products-box", Class="box") << [
						Div(Class="left-banner") << [
							Img(Id="cgra-img", Src="photo/cgra.svg"),
							H1(Style="margin: 3rem 0px 0px 0px;") << ["Programmable dataflow acceleration", Br(), "without the hassle."],
							P(Style="margin: 2rem 0px 0rem 0px;") << [B(Style="font-size: 1.6rem;") << "Unconstrained", Br(), "Reduced network overhead allows more execution nodes on chip, and energy is carefully managed to ensure it contributes exclusively to solving your problem."],
							P(Style="margin: 2rem 0px 0rem 0px;") << [B(Style="font-size: 1.6rem;") << "Open Source", Br(), "Our tools are developed in the open so you can trust in their quality and longevity."],
							P(Style="margin: 2rem 0px 2rem 0px;") << [B(Style="font-size: 1.6rem;") << "Just Works", Br(), "No need for timing closure, no need for retiming, and no need for synthesis. Map any dataflow program for ASIC-like performance and power."],
							form,
						],
					],
					A(Id="tools"),
					Div(Id="tools-box", Class="box") << [
						Div(Class="left-banner") << [
							Img(Class="right-img", Src="photo/control.svg", Height="280px", Style="object-fit: cover; object-position: 0 35%;"),
							H1(Style="margin: 5rem 0px 0px 0px;") << [
								"Haystack ",
							],
							P(Style="margin: 0 0 1rem 0;") << "Haystack is a high level circuit synthesis engine. It compiles Communicating Hardware Processes (CHP), a message passing control flow language similar to Golang, into Production Rules (PRS), which specify the digital logic that implements those Quasi-Delay Insensitive (QDI) processes. This is still under development, but can currently simulate and compile Handshaking Expansions (HSE) that have a complete state encoding.",
							H1(Style="margin: 0 0 7rem 0;") << [
								A(Href="https://github.com/broccolimicro/haystack") << Img(Class="img-link", Src="logos/github.png"), " ",
								A(Href="https://github.com/broccolimicro/haystack/releases") << Img(Class="img-link", Src="logos/tag.svg"), " ",
								A(Href="https://www.paypal.com/donate/?hosted_button_id=6633ZXZTED63A") << Img(Class="img-link", Src="logos/donate.svg"),
							],
						],
						Div(Class="left-banner") << [
							Img(Class="left-img", Src="photo/floret.png"),
							H1(Style="margin: 5rem 0px 0px 0px;") << [
								"Floret ",
							],
							P(Style="margin: 0 0 1rem 0;") << "Floret is an automated cell layout engine. This is still under development, but it currently produces layouts that are often good enough with minor modifications. While Floret is currently being tested against Skywater 130nm, new technologies can be defined with design rules specified in Python.",
							H1(Style="margin: 0 0 7rem 0;") << [
								A(Href="https://github.com/broccolimicro/floret") << Img(Class="img-link", Src="logos/github.png"), " ",
								A(Href="https://github.com/broccolimicro/floret/releases") << Img(Class="img-link", Src="logos/tag.svg"), " ",
								A(Href="https://www.paypal.com/donate/?hosted_button_id=6633ZXZTED63A") << Img(Class="img-link", Src="logos/donate.svg"),
							],
						],
						Div(Class="left-banner") << [
							Img(Class="right-img", Src="photo/bcli.png"),
							H1(Style="margin: 5rem 0px 0px 0px;") << [
								"Broccoli-CLI ",
							],
							P(Style="margin: 0 0 1rem 0;") << "bcli is a docker container with a full development environment for self-timed circuits. It includes ACT, OpenROAD, Magic, KLayout, Floret, Haystack, Xyce, Gaw, and more.",
							H1(Style="margin: 0 0 7rem 0;") << [
								A(Href="https://github.com/broccolimicro/bcli") << Img(Class="img-link", Src="logos/github.png"), " ",
								A(Href="https://hub.docker.com/r/broccolimicro/broccoli-cli") << Img(Class="img-link", Src="logos/docker.svg"),
							],
						],
					],
					A(Id="courses"),
					Div(Id="courses-box", Class="box") << [
						Div(Class="left-banner") << [
							Iframe(Class="right-img", Style="aspect-ratio: 16 / 9;", Src="https://www.youtube-nocookie.com/embed/videoseries?si=ZFy0bMNimvsltEu2&amp;list=PLUCgknFT8LMilpLkfwXddes_TS0W9XvO-", Title="YouTube video player", Frameborder="0", Allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share", Referrerpolicy="strict-origin-when-cross-origin", Allowfullscreen=True),
							H1(Style="margin: 0 0 0 0;") << ["Introduction to Self Timed Circuits"],
							P(Style="margin: 0 0 0 0;") << [
								"This course covers the fundamentals of self-timed circuits including timing assumptions and guarantees, failure modes, pipeline structures, data encodings, conditional logic, internal memory, and non-deterministic behavior, hardware description languages for different layers of abstraction, and two design methodologies. It is designed with a bottom up approach, starting with circuitry and working its way up through more abstract representations. Background experience with programming is required, and circuit design is helpful but optional. The course is offered for free with the goal of building local expertise and community in VLSI, Computer Architecture, and Self-Timed Circuits.",
								Div(Id="course-links") << [
									(A(Class="course-link", Href="https://github.com/broccolimicro/course-self-timed-circuits/tree/summer-2023") << "Summer 2023"),
									(A(Class="course-link", Href="https://github.com/broccolimicro/course-self-timed-circuits") << ["Summer 2024"]),
								],
							],
						],
					],
					A(Id="about"),
					Div(Id="about-box", Class="box") << [
						Div(Class="left-banner") << [
							Img(Id="logo-img", Src="logo.svg"),
							P(Style="margin: 5rem 0px 7rem 0px;") << "Broccoli was founded in 2021 to bring about a categorical improvement in compute performance. Autonomous systems require reconfigurable Digital Signal Processors (DSP) with order of magnitude improvements in throughput, power, latency, and capacity. Field Programmable Gate Arrays push timing and pipeline management challenges to the user, making them very difficult to use. With the added challenge of managing multiple clock domains, designs often have a low operating frequency and therefore throughput unless significant time and effort are taken to tune the design and its mapping. Broccoli is solving these challenges in hardware to dramatically simplify the compilation and mapping process, and allow designers to iterate on designs quickly while meeting their power and performance constraints."
						],
						Div(Class="banner") << [
							H1() << "Team",
							Div(Class="contact-card") << [
								Div(Class="contact-photo") << (Div(Class="contact-img-frame") << Img(Class="contact-img", Src="photo/ned.jpg")),
								Div(Class="contact-info") << (P() << [A(Href="https://nedbingham.com") << "Ned Bingham, Founder", Address() << "edward.bingham@broccolimicro.io"]),
							],
						]
					],
				],
				Script() << "startWindow();"
			]
		]
	])

