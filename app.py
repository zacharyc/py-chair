import sys

menu="""
Welcome to Py Chair -> A wheelchair simulation.
Menu:
1) Echo Print
q) quit
"""

# Writing a class

class WheelChair:
	length = 0
	width = 0

	def __init__(self, length, width):
		self.length = length
		self.width = width

def main():
	while 1:
		print(menu)
		foo = str(input())

		if (foo == "q"):
			break;
		elif (foo == "1"):
			print("Enter a length in inches:")
			l = str(input())
			print("Enter a width in inches:")
			w = str(input())
			wc = WheelChair(l, w)

			print(wc)
		else:
			print(foo)


if __name__ == '__main__':
	main()