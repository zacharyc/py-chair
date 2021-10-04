import sys

def main():
	while 1:
		print("Enter a command, q to quit")
		foo = str(input())

		if (foo == "q"):
			break;
		else:
			print(foo)


if __name__ == '__main__':
	main()