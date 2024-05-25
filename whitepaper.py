#!/usr/bin/python3

from pyhtml.html import *
from common import Navigate, getPOST
import os

if __name__ == "__main__":
	post = getPOST()

	print(Document() << [])

