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
	formItems.append(Input(Type="submit", Value="Read our Whitepaper"))

	form = None
	if "whitepaper" in cookies:
		form = Form(Id="whitepaper-form", Method="post", action="/BroccoliWhitepaper.pdf") << formItems
	else:
		form = Form(Id="whitepaper-form", Method="post", onsubmit="submitWhitepaper(event)") << formItems

	print(Document() << [
		Html() << [
			Head() << [
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
				Script(Src="js/imports.js"),
				Script(Src="js/pubcss.js"),
				Script(Src="js/code.js"),
				Script(Src="index.js"),
			],
			Body() << [
				P() << str(cookies),
				Navigate("whitepaper" in cookies),
				Div(Class="main") << [
					A(Id="products") << [
						Div(Id="products-box", Class="box") << [
							Div(Class="left-banner") << [
								Img(Src="photo/cgra.svg", Width="512px", Style="float: left; margin: 4rem 4rem 4rem 4rem;"),
								H1(Style="margin: 3rem 0px 0px 0px;") << ["Dataflow acceleration", Br(), "that gets out of your way."],
								P(Style="margin: 2rem 0px 0rem 0px;") << [B() << "Larger programs. ", "Reduced network overhead allow more execution nodes on chip for your program."],
								P(Style="margin: 2rem 0px 0rem 0px;") << [B() << "Less Power. ", "Energy is carefully managed to ensure it contributes exclusively to solving your problem."],
								P(Style="margin: 2rem 0px 3rem 0px;") << [B() << "Just Works. ", "No need for timing closure, no need for retiming, and no need for synthesis. Map any program for ASIC level performance and power."],
								form,
							],
						],
					],
					A(Id="tools") << [
						Div(Id="tools-box", Class="box") << [
							Div(Class="left-banner") << [
								Img(Src="photo/bcli.png", Width="768px", Style="float: left; margin: 4rem 4rem 4rem 4rem;"),
								H1(Style="margin: 5rem 0px 0px 0px;") << ["Broccoli CLI ", A(Href="https://github.com/broccolimicro/bcli") << Img(Src="logos/github.jpg", Width="40px"), " ", A(Href="https://github.com/broccolimicro/bcli/releases") << Img(Src="logos/tag.svg", Width="40px")],
								P(Style="margin: 0px 0px 7rem 0px;") << "BCLI is a containerized development environment for self-timed circuits. It includes ACT, OpenROAD, Magic, KLayout, Floret, Haystack, and Xyce. Your home directory is mounted as a volume, the user information is replicated, and X11 forwarding is enabled to provide a seamless development experience."
							],
							Div(Class="left-banner") << [
								Img(Src="photo/control.svg", Width="768px", Height="280px", Style="float: right; margin: 4rem 4rem 4rem 4rem; object-fit: cover; object-position: 0 35%;"),
								H1(Style="margin: 5rem 0px 0px 0px;") << ["Haystack ", A(Href="https://github.com/broccolimicro/haystack") << Img(Src="logos/github.jpg", Width="40px"), " ", A(Href="https://github.com/broccolimicro/haystack/releases") << Img(Src="logos/tag.svg", Width="40px")],
								P(Style="margin: 0px 0px 7rem 0px;") << "Haystack is a high level synthesis engine for compiling Communicating Hardware Processes (CHP) to Production Rules (PRS). This is still under development, but can currently handle disambiguated Handshaking Expansions (HSE)."
							],
							Div(Class="left-banner") << [
								Img(Src="photo/floret.png", Width="768px", Style="float: left; margin: 4rem 4rem 4rem 4rem;"),
								H1(Style="margin: 5rem 0px 0px 0px;") << ["Floret ", A(Href="https://github.com/broccolimicro/floret") << Img(Src="logos/github.jpg", Width="40px"), " ", A(Href="https://github.com/broccolimicro/floret/releases") << Img(Src="logos/tag.svg", Width="40px")],
								P(Style="margin: 0px 0px 7rem 0px;") << "Floret is an automated cell layout engine. While it is still under development, it produces layouts that are often good enough with minor modifications. While Floret is currently being tested against Skywater 130nm, new technologies can be defined with design rules specified in Python."
							],
						],
					],
					A(Id="courses") << [
						Div(Id="courses-box", Class="box") << [
							Post("courses/2024_self_timed_circuits.html"),
							Post("courses/2023_self_timed_circuits.html"),
						],
					],
					A(Id="about") << [
						Div(Id="about-box", Class="box") << [
							Div(Class="left-banner") << [
								Img(Src="logo.svg", Width="256px", Style="float: left; margin: 4rem 4rem 4rem 4rem;"),
								P(Style="margin: 7rem 0px 7rem 0px;") << "Broccoli was founded in 2021 to bring about a categorical improvement in compute performance. Autonomous systems require reconfigurable Digital Signal Processors (DSP) with order of magnitude improvements in throughput, power, latency, and capacity. Field Programmable Gate Arrays push timing and pipeline management challenges to the user, making them very difficult to use. With the added challenge of managing multiple clock domains, designs often have a low operating frequency and therefore throughput unless significant time and effort are taken to tune the design and its mapping. Broccoli is solving these challenges in hardware to dramatically simplify the compilation and mapping process, and allow designers to iterate on designs quickly while meeting their power and performance constraints."
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
				],
				Script() << """startWindow();
includeHTML(document)
.then(waitFor(loadCode))
.then(waitFor(formatAnchors))
.then(waitFor(formatLinks));"""
			]
		]
	])

