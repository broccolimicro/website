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
					Div(Id="logo", Href="/news.py"),
					A(Id="name", Href="/news.py") << "Broccoli",
				], 
				Div(Id="nav-mid") << [
					A(Class="nav-button", Id="loom-button", Href="/#loom") << "Loom",
					A(Class="nav-button", Id="download-button", Href="/#download")  << "Download",
					A(Class="nav-button", Id="sponsor-button", Href="/#sponsor")  << "Sponsor",
					A(Class="nav-button", Id="about-button", Href="/#about")  << "About",
					A(Class="nav-button", Id="docs-button", Href="/docs.py")  << "Docs",
					A(Class="nav-button", Id="forum-button", Href="/forum.py")  << "Forum",
				], Div(Id="nav-right") << [
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf") << "Government",
				], Div(Id="nav-small") << [
					A(Class="nav-button", Id="toggle", Href="javascript:toggleMenu()") << Img(Id="toggle_img", Src="logos/menu.svg"),
				],
			],
			Div(Id="menu-top") << [
				Div(Id="menu") << [
					A(Class="nav-button", Href="/#loom", Onclick="toggleMenu()") << "Loom",
					A(Class="nav-button", Href="/#download", Onclick="toggleMenu()")  << "Download",
					A(Class="nav-button", Href="/#sponsor", Onclick="toggleMenu()")  << "Sponsor",
					A(Class="nav-button", Href="/#about", Onclick="toggleMenu()")  << "About",
					A(Class="nav-button", Href="/docs.py", Onclick="toggleMenu()")  << "Docs",
					A(Class="nav-button", Href="/forum.py", Onclick="toggleMenu()")  << "Forum",
					A(Class="nav-button", Href="/BroccoliCapabilities.pdf", Onclick="toggleMenu()") << "Government",
				],
			],
		],
	]

