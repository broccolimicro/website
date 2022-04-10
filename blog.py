#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

def Post(path):
	with open(path, 'r') as fptr:
		return Div(Class="box post") << fptr.read()

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					Post("blog/2017-04-29-computing_trends.html")
				]
			]
		]
	])

