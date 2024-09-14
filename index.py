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
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
				Script(Src="index.js"),
			],
			Body() << [
				Navigate("whitepaper" in cookies),
				Div(Id="main") << [
					A(Id="loom"),
					Div(Class="loom-box box") << [
						Div(Class="banner", Style="max-width: 42rem;") << [
							Div(Class="banner-bh") << [
								H1() << "Loom",
								H3() << "pre-alpha release",
								P(Style="margin: 0 0 1rem 0; text-align: center;") << "A programming language for quasi-delay insensitive asynchronous circuits.",
								Ul(Style="margin: 0 0 1rem 0;") << [
									Li() << (A(href="#synthesis") << "Logic synthesis from functional specifications"),
									Li() << (A(href="#layout") << "Automated custom cell layout, placement, and routing"),
									Li() << (A(href="#simulation") << "Behavioral and digital simulation"),
								],
								A(Class="button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", href="#download") << "Get Started",

								A(Class="button", href="#sponsor") << "Sponsor",
								A(Class="button", href="https://github.com/broccolimicro/loom") << "View Source",
							],
						],

						Div(Class="banner") << [
							A(Id="sponsors"),
							Div(Class="banner-bh") << [
								A(Href="#sponsor") << "Help shape this community with your logo here.",
							],
						],
					],


			
					Div(Class="loom-box box", Style="background-color: rgb(244, 244, 245);") << [
						A(Id="problem"),
						Div(Class="banner") << [
							Div(Class="banner-li", Style="height: 20rem; background-image: url('photo/memory.png');") << [
							], Div(Class="banner-rt") << [
								H2() << [
									"Chip design is challenging",
								],
								P(Style="margin: 0 0 0.5rem 0;") << "\"Chips like GPUs require nearly 1,000 people to build, and each must understand how pieces of the design work together as they work to continuously improve them\"",
								P(Style="margin: 0 0 1.5rem 0; text-align: right;") << (A(href="https://www.wsj.com/articles/designing-chips-is-getting-harder-these-engineers-say-chatbots-and-ai-can-help-092b4c49") << "Bryan Catanzaro, VP of Applied Deep Learning Research, NVidia"),
								P(Style="margin: 0 0 1rem 0;") << "Chip design is challenging, and the vast majority of that comes from functional and timing verification. Manufacturing a chip is slow and expensive, mistakes in the design are doubly so.",
							],
						],

	
						A(Id="synthesis"),
						Div(Class="banner") << [
							Div(Class="banner-ri") << [
								Div(Class="terminal") << [
									Pre(Id="synthesis-example", Class="terminal-window", inline=True),
								],
							], Div(Class="banner-lt") << [
								H2() << [
									"Correct by construction", Br(), "Insensitive to delay",
								],
								P(Style="margin: 0 0 1rem 0;") << "Synthesize your design directly from your functional specification. Synthesis is correct by construction and generates circuits that function correctly regardless of timing. This dramatically reduces the need for both functional and timing verification allowing you to focus on your product.",

								A(Id="synthesis-button", Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Onclick="synthesize()") << "Synthesize your design",
							],
						],


						A(Id="layout"),
						Div(Class="banner") << [
							Div(Class="banner-li") << [
								Div(Id="layout-example", Class="terminal") << [
									Pre(Class="terminal-window", inline=True) << [
Span(Style="font-weight: 700;", inline=True) << "$ lm wchb1b.hse sky130.py",
"""
$ klayout wchb1b.gds
""",
									],
								],
								Img(Id="layout-example-imgs", Src="photo/cell_01.png", Style="max-width: 100%; height: 30rem; border-radius: 0.75rem; display: none;"),
							], Div(Class="banner-rt") << [
								H2() << "Automated physical design",
								P(Style="margin: 0 0 1rem 0;") << "Devices are sized and cell layouts are generated automatically. Design rules are specified through a simple python interface. This reduces the timeline for physical design from 6 months to the click of a button.",
								P(Style="margin: 0 0 1rem 0;") << [
									"See the spec for ",
									A(href="https://github.com/broccolimicro/floret/blob/main/tech/sky130.py") << "Skywater 130nm",
									".",
								],
								A(Id="layout-button", Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Onclick="layout()", Dataview=True) << "Generate your layout",
							],
						],


						A(Id="simulation"),
						Div(Class="banner") << [
							Div(Class="banner-ri") << [
								Div(Id="simulate-example-main") << [
									Div(Class="terminal") << [
										Pre(Id="simulate-example", Class="terminal-window", inline=True),
									],
								],
								Img(Id="simulate-example-imgs", Src="photo/hsesim.png", Style="max-width: 100%; height: 30rem; border-radius: 0.75rem;"),
							], Div(Class="banner-lt") << [
								H2() << "Flexible to your needs",
								P(Style="margin: 0 0 1rem 0;") << "Want to make low level changes in the compiled circuits? Simulate your behavioral and digital specifications with random timing for verification. View the results in gtkwave or work directly on the command line.",
								A(Id="gtkwave-button", Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Onclick="simulate(true)", Dataview=True) << "View in gtkwave",
								A(Id="simulate-button", Class="small-button", Onclick="simulate(false)") << "Simulate your devices",
							],
						],
					],



					A(Id="download"),
					Div(Id="download-box", Class="box") << [
						Div(Class="banner") << [
							Div(Class="banner-bh") << [
								H1() << "Get started with Loom",
								P(Style="text-align: center;") << "A pre-alpha release is currently only available for Linux.",#, Windows, and macOS.",
							], Div(Class="banner-lt", Style="padding-top: 6.5rem;") << [
								H4() << "Linux",
								P() << "Download the latest version for Ubuntu 24.04 or later.",
								P() << [
									A(Class="small-green-button", Href="https://github.com/broccolimicro/loom/releases") << "Download",
									A(Class="small-button", Href="https://github.com/broccolimicro/loom") << "Docs",
									#A(Class="small-button", Href="forum.py") << "Forum",
								],
								#H4(Style="margin-top: 2rem;") << "Windows",
								#P() << "Download the latest version for Windows 10 or later.",
								#P() << [
								#	A(Class="small-green-button", Href="https://github.com/broccolimicro/loom/releases") << "Download",
								#	A(Class="small-button", Href="https://github.com/broccolimicro/loom") << "Docs",
								#	A(Class="small-button", Href="forum.py") << "Forum",
								#],
								#H4(Style="margin-top: 2rem;") << "macOS",
								#P() << "Download the latest version for macOS 10.15 or later.",
								#P() << [
								#	A(Class="small-green-button", Href="https://github.com/broccolimicro/loom/releases") << "Download",
								#	A(Class="small-button", Href="https://github.com/broccolimicro/loom") << "Docs",
								#	A(Class="small-button", Href="forum.py") << "Forum",
								#],
							], Div(Class="banner-ri", Style="height: 45rem; background-image: url('photo/control.svg');") << [
							],
						],
					],



					A(Id="sponsor"),
					Div(Id="sponsor-box", Class="box", Style="background-color: rgb(244, 244, 245);") << [
						Div(Class="banner") << [
							Div(Class="banner-bh") << [
								H1() << [
									"Support the Development of Loom",
								],
								P(Style="text-align: center;") << "Become a sponsor and help us improve and maintain Loom. Your support is greatly appreciated.",

								Div(Style="background-color: rgb(255,255,255); border-radius: 0.75rem; width: 20rem; text-align: center; padding: 2rem 1rem 2rem 1rem; margin: 2rem 1rem 2rem 1rem; border: 1px solid rgb(128,128,128); display: inline-block;") << [
									H3(Style="text-align: center; margin: 0 0 1rem 0;") << "Individual",
									H4(Style="text-align: center; margin: 0 0 2rem 0;") << "$10 / month",
									P(Style="text-align: center; margin: 0 0 2rem 0;") << "Support the development of Loom and receive exclusive updates.",
									A(Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Href="https://github.com/sponsors/broccolimicro/sponsorships?tier_id=428571&preview=false") << "Become a Sponsor",
								],

								Div(Style="background-color: rgb(255,255,255); border-radius: 0.75rem; width: 20rem; text-align: center; padding: 2rem 1rem 2rem 1rem; margin: 2rem 1rem 2rem 1rem; border: 1px solid rgb(128,128,128); display: inline-block;") << [
									H3(Style="text-align: center; margin: 0 0 1rem 0;") << "Organization",
									H4(Style="text-align: center; margin: 0 0 2rem 0;") << "$2,000 / month",
									P(Style="text-align: center; margin: 0 0 2rem 0;") << "Support the development of Loom. Your bug tickets are prioritized, you have direct access to the team, and you may display your logo prominantly on this site.",
									A(Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Href="https://github.com/sponsors/broccolimicro/sponsorships?tier_id=428573&preview=false") << "Become a Sponsor",
								],

								Div(Style="background-color: rgb(255,255,255); border-radius: 0.75rem; width: 20rem; text-align: center; padding: 2rem 1rem 2rem 1rem; margin: 2rem 1rem 2rem 1rem; border: 1px solid rgb(128,128,128); display: inline-block;") << [
									H3(Style="text-align: center; margin: 0 0 1rem 0;") << "Enterprise",
									H4(Style="text-align: center; margin: 0 0 2rem 0;") << "$10,000 / month",
									P(Style="text-align: center; margin: 0 0 2rem 0;") << "Support the development of Loom. Your bug tickets are prioritized, you have direct access to the team, and you may display your logo prominantly on this site. Your feature requests are prioritized, and you are given an advisory position in which you may guide development with bi-weekly 1:1s. You are allocated half an engineer for every multiple of this sponsorship.",
									A(Class="small-button", Style="background-color: rgb(10, 133, 55); border: 0px; color: rgb(255, 255, 255);", Href="https://github.com/sponsors/broccolimicro/sponsorships?tier_id=428574&preview=false") << "Become a Sponsor",
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

