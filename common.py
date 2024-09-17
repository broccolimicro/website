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
					Div(Id="logo"),
					A(Id="name", Href="/#loom") << "Broccoli",
				], 
				Div(Id="nav-mid") << [
					A(Class="nav-button", Id="loom-button", Href="/#problem") << "Loom",
					A(Class="nav-button", Id="download-button", Href="/#download")  << "Download",
					A(Class="nav-button", Id="sponsor-button", Href="/#sponsor")  << "Sponsor",
					A(Class="nav-button", Id="about-button", Href="/#about")  << "About",
					A(Class="nav-button", Id="docs-button", Href="https://github.com/broccolimicro/loom")  << "Docs",
					#A(Class="nav-button", Id="courses-button", Href="/courses.py")  << "Courses",
					A(Class="nav-button", Id="forum-button", Href="https://github.com/broccolimicro/loom/discussions")  << "Forum",
				], Div(Id="nav-right") << [
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf") << "Government",
				], Div(Id="nav-small") << [
					A(Class="nav-button", Id="toggle", Href="javascript:toggleMenu()") << Img(Id="toggle_img", Src="logos/menu.svg"),
				],
			],
			Div(Id="menu-top") << [
				Div(Id="menu") << [
					A(Class="nav-button", Href="/#problem", Onclick="toggleMenu()") << "Loom",
					A(Class="nav-button", Href="/#download", Onclick="toggleMenu()")  << "Download",
					A(Class="nav-button", Href="/#sponsor", Onclick="toggleMenu()")  << "Sponsor",
					A(Class="nav-button", Href="/#about", Onclick="toggleMenu()")  << "About",
					A(Class="nav-button", Href="https://github.com/broccolimicro/loom", Onclick="toggleMenu()")  << "Docs",
					#A(Class="nav-button", Href="/courses.py", Onclick="toggleMenu()")  << "Courses",
					A(Class="nav-button", Href="https://github.com/broccolimicro/loom/discussions", Onclick="toggleMenu()")  << "Forum",
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf", Onclick="toggleMenu()") << "Government",
				],
			],
		],
	]

