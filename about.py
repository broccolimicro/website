#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Title("About | Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
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
				]
			]
		]
	])

