from pyhtml.html import *

def Post(path):
	try:
		fptr = open(path, 'r')
		return Div(Class="box post") << fptr.read()
	except:
		return ""

def Navigate():
	return Header(Id="navigate") << [
		Nav(Id="menu") << [
			A(Id="title", Href="/news.py") << [
				Div(Id="logo") << Img(Id="logo_img", Src="logo_simple.png"),
				Div(Id="name", Class="nav_button") << "Broccoli",
			],
			A(Class="nav_button", Href="/index.py#products", Style="border-bottom: 3px solid black;") << "Products",
			A(Class="nav_button", Href="/index.py#tools") << "Tools",
			A(Class="nav_button", Href="/index.py#courses")  << "Courses",
			A(Class="nav_button", Href="/index.py#about")  << "About",
			A(Class="nav_button", Href="/BroccoliCapabilities.pdf", Style="float: right;") << "Government",
			A(Class="nav_button", Href="/BroccoliWhitepaper.pdf", Style="float: right;") << "Whitepaper",
		],
	]

