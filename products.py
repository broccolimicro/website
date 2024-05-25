#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Title("Products | Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					Div(Class="left-banner") << [
						Img(Src="photo/cgra.svg", Width="512px", Style="float: left; margin: 4rem 4rem 4rem 4rem;"),
						H1(Style="margin: 5rem 0px 0px 0px;") << ["Dataflow acceleration", Br(), "that gets out of your way."],
						P(Style="margin: 2rem 0px 0rem 0px;") << [B() << "Larger programs. ", "More execution nodes on chip for your program."],
						P(Style="margin: 2rem 0px 0rem 0px;") << [B() << "Less Power. ", "Cut out the cruft. Energy is carefully managed to ensure it contributes exclusively to solving your problem."],
						P(Style="margin: 2rem 0px 3rem 0px;") << [B() << "Just Works. ", "No need for timing closure, no need for retiming, and no need for synthesis. Map any program for ASIC level performance and power."],
						Form(Id="whitepaper-form") << [
							Input(Type="text", Placeholder="First Name"), Input(Type="text", Placeholder="Last Name"), Br(),
							Input(Type="email", Placeholder="Email"), Input(Type="submit", Value="Read the Whitepaper"),
						],
					],
				]
			]
		]
	])

