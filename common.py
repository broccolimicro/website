from pyhtml.html import *
import sys

def Post(path):
	try:
		fptr = open(path, 'r')
		return Div(Class="box post") << fptr.read()
	except:
		return ""

def getPOST():
	post = {}
	args = sys.stdin.read().split('&')

	for arg in args: 
		t = arg.split('=')
		if len(t)>1:
			k, v = arg.split('=')
			post[k] = v
	return post

def Navigate(whitepaper=False):
	nav = [
		A(Id="title", Href="/news.py") << [
			Div(Id="logo") << Img(Id="logo_img", Src="logo_simple.png"),
			Div(Id="name", Class="nav_button") << "Broccoli",
		],
		A(Class="nav_button", Id="products-button", Href="/index.py#products") << "Products",
		A(Class="nav_button", Id="tools-button", Href="/index.py#tools") << "Tools",
		A(Class="nav_button", Id="courses-button", Href="/index.py#courses")  << "Courses",
		A(Class="nav_button", Id="about-button", Href="/index.py#about")  << "About",
		A(Class="nav_button", Href="/BroccoliCapabilities.pdf", Style="float: right;") << "Government",
	]
	if whitepaper:
		nav.append(A(Class="nav_button", Href="/BroccoliWhitepaper.pdf", Style="float: right;") << "Whitepaper")
	return Header(Id="navigate") << [
		Nav(Id="menu") << nav,
	]

