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
				Script(Src="js/imports.js"),
				Script(Src="js/pubcss.js"),
				Script(Src="js/code.js"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					#Post("blog/2022-06-21-cgra.html"),
					Post("blog/2022-06-21-dsp.html"),
					Post("blog/2022-04-10-technology-trends.html")
				],
				Script() << """includeHTML(document)
.then(waitFor(loadCode))
.then(waitFor(formatAnchors))
.then(waitFor(formatLinks));"""
			]
		]
	])

