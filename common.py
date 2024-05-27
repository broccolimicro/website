from pyhtml.html import *
import sys
from urllib.parse import unquote

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
			post[unquote(k)] = unquote(v)
	return post

def Navigate(whitepaper=False):
	return Header(Id="header") << [
		Nav(Id="nav") << [
			Div(Id="nav-top") << [
				Div(Id="nav-left") << [
					A(Id="title", Href="/news.py") << [
						Div(Id="logo"),
						Div(Id="name") << "Broccoli",
					],
				], Div(Id="nav-mid") << [
					A(Class="nav-button", Id="products-button", Href="/#products") << "Products",
					A(Class="nav-button", Id="tools-button", Href="/#tools") << "Tools",
					A(Class="nav-button", Id="courses-button", Href="/#courses")  << "Courses",
					A(Class="nav-button", Id="about-button", Href="/#about")  << "About",
				], Div(Id="nav-right") << ([
					A(Class="nav-button", Href="/BroccoliWhitepaper.pdf") << "Whitepaper",
				] if whitepaper else []) + [
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf") << "Government",
				], Div(Id="nav-small") << [
					A(Class="nav-button", Id="toggle", Href="javascript:toggleMenu()") << Img(Id="toggle_img", Src="logos/menu.svg"),
				],
			],
			Div(Id="menu-top") << [
				Div(Id="menu") << [
					A(Class="nav-button", Href="/#products", Onclick="toggleMenu()") << "Products",
					A(Class="nav-button", Href="/#tools", Onclick="toggleMenu()") << "Tools",
					A(Class="nav-button", Href="/#courses", Onclick="toggleMenu()")  << "Courses",
					A(Class="nav-button", Href="/#about", Onclick="toggleMenu()")  << "About",
				] + ([
					A(Class="nav-button", Href="/BroccoliWhitepaper.pdf", Onclick="toggleMenu()") << "Whitepaper",
				] if whitepaper else []) + [
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf", Onclick="toggleMenu()") << "Government",
				],
			],
		],
	]

