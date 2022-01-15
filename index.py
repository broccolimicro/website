#!/usr/bin/python3

from pyhtml.html import *

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Img(Src="logo.svg", Height="50%", Id="logo"),
                H1("Broccoli, LLC")
            ]
		]
	])

