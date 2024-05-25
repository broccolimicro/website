#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, getPOST
import os

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					P() << str(getPOST())
				],
			]
		]
	])

