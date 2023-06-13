from pyhtml.html import *

def Post(path):
	try:
		fptr = open(path, 'r')
		return Div(Class="box post") << fptr.read()
	except:
		return ""

def Navigate():
	return Header(Id="navigate") << [
		A(Id="title", Href="/") << [
			Div(Id="logo") << Img(Id="logo_img", Src="logo.svg"),
			Div(Id="name", Class="nav_button") << "Broccoli"
		],
		Nav(Id="menu") << [
			#A(Class="nav_button", Href="/products") << "Products",
			A(Class="nav_button", Href="/")    << "News",
			A(Class="nav_button", Href="/BroccoliCapabilities.pdf") << "Government",
			A(Class="nav_button", Href="/courses.py")  << "Courses",
			A(Class="nav_button", Href="/contact.py")  << "Contact",
		]
	]

