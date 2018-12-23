


def main():
	with open('./input/input.txt') as f:
		data = f.read()
		print(data)
		with open('./output/output.txt', 'w') as f2:
			f2.write(data)


main()