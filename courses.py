#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, Post

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
					Post("courses/self_timed_circuits.html")
				],
				Script() << """includeHTML(document)
.then(waitFor(loadCode))
.then(waitFor(formatAnchors))
.then(waitFor(formatLinks));"""
			]
		]
	])

