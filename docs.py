#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, Post
from http.cookies import SimpleCookie
import os

if __name__ == "__main__":
	cookies = SimpleCookie(os.environ.get('HTTP_COOKIE', ''))

	currentRelease = "0.8.2"

	print(Document() << [
		Doctype(Html=True),
		Html() << [
			Head() << [
				# Google Analytics
				Script(Src="https://www.googletagmanager.com/gtag/js?id=G-FT6E284Y58", Async=True),
				Script() << [
"""window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-FT6E284Y58');""",
				],
				Title("Broccoli"),
				Link(Rel="stylesheet", Type="text/css", Href="/index.css"),
				Script(Src="/index.js"),
			],
			Body(Style="overflow: hidden;") << [
				A(Id="skip-link", Href="#main-content") << "Skip to main content",
				Navigate("whitepaper" in cookies),
				A(Id="main-content"),
				Div(Id="main") << [
					Iframe(Src="https://broccolimicro.github.io/loom/", Width="100%", Frameborder="0", Style="height: 100%;"),
				],
				Script() << "startWindow();"
			]
		]
	])

