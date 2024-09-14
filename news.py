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
				Script(Src="https://www.googletagmanager.com/gtag/js?id=G-FT6E284Y58", Async=True),
				Script() << [
"""window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-FT6E284Y58');""",
				],
				Title("News | Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
				Script(Src="js/imports.js"),
				Script(Src="js/pubcss.js"),
				Script(Src="js/code.js"),
				Script(Src="index.js"),
			],
			Body() << [
				Navigate("whitepaper" in cookies),
				Div(Class="main") << [
					Post("blog/2024-09-14-update.html"),
					Post("blog/2024-05-27-months-of-progress.html"),
					Post("blog/2023-08-31-intro-self-timed-circuits.html"),
					Post("blog/2022-06-21-dsp.html"),
					Post("blog/2022-04-10-technology-trends.html"),
				],
				Script() << """startWindow();
includeHTML(document)
.then(waitFor(loadCode))
.then(waitFor(formatAnchors))
.then(waitFor(formatLinks));"""
			]
		]
	])

