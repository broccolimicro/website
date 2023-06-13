#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					Div(Class="banner light-banner") << [
						Div(Class="center-banner-text") << [
							H1() << "Contact",
							P() << ["Ned Bingham", Address() << "edward.bingham@broccolimicro.io"],
							P() << ["Jimmy Torre", Address() << "jtorre@broccolimicro.io"],
						]
					]
				]
			]
		]
	])

