#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate

if __name__ == "__main__":
	print(Document() << [
		Html() << [
			Head() << [
				Link(Rel="stylesheet", Type="text/css", Href="index.css"),
			],
			Body() << [
				Navigate(),
				Div(Class="main") << [
					Div(Class="banner dark-banner", Style="background-image: url(die.jpg)") << [
						Div(Class="left-banner-text") << [
							H1() << "Fundamental Shift in Microarchitecture",
							P() << "Offers order-of-magnitude improvements in capacity and faster processing, all using less power allowing you to put everything on a single chip."
						]
					],
					Div(Class="banner light-banner", Style="background-image: url(control.svg); background-size: 35%; background-position: 10% 50%; background-attachment: fixed") << [
						Div(Class="right-banner-text") << [
							H1() << "Configurable",
							P() << "Quickly and easily map your workload to the operators on chip without specialized hardware design expertise."
						] 
					],
					Div(Class="banner dark-banner", Style="background-image: url(fabric.svg)") << [
						Div(Class="left-banner-text") << [
							H1() << "Fast",
							P() << "On chip operators push the bounds for sequential performance and double throughput per transistor."
						]
					],
					Div(Class="banner light-banner", Style="background-image: url(control.svg); background-size: 35%; background-position: 10% 50%; background-attachment: fixed") << [
						Div(Class="right-banner-text") << [
							H1() << "Efficient",
							P() << "Intelligent control structures eliminate energy overheads not necessary for useful work."
						] 
					],
				]
			]
		]
	])


# A novel approach to compute
# ASIC speed without the ASIC
# Optimized for any workload
# ASIC performance, CPU programmability, GPU capacity, all in one


# Higher Capacity
# Easier to Program
# Intelligent control to cut the fat
# Configurable to any workload
