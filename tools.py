#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Title("Tools | Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
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
				]
			]
		]
	])

