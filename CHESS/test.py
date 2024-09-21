# tester = "A1"
# tester = tester.lower()
# print(tester)
class Pet():
	def bark():
		print("i dont know what to say")

class Dog(Pet):
	def bark():
		print("GAU GAU")

Long = Dog()
Long.bark
