class MinHeap:

	def __init__(self, inital_data = None):
		if inital_data is None:
			self.data = []
		else:
			self.data = list(inital_data)
			for i in range((len(self.data) // 2) - 1, -1, -1):
				self._bubble_down(i)

	def is_empty(self):
		return len(self.data) == 0

	def size(self):
		return len(self.data)

	def push(self, data):
		self.data.append(data)
		self._bubble_up(len(self.data) - 1)

	def pop(self):
		result = self.data[0]
		last = self.data.pop()
		if len(self.data) > 0:
			self.data[0] = last
			self._bubble_down(0)
		return result

	def min(self):
		return self.data[0]

	def _bubble_up(self, i):
		while i > 0:
			parent = (i - 1) // 2
			if self.data[i] < self.data[parent]:
				self.data[i], self.data[parent] = self.data[parent], self.data[i]
				i = parent
			else:
				break

	def _bubble_down(self, i):
		n = len(self.data)
		while True:
			left = 2 * i + 1
			right = 2 * i + 2
			smallest = i

			if left < n and self.data[left] < self.data[smallest]:
				smallest = left
			if right < n and self.data[right] < self.data[smallest]:
				smallest = right

			if smallest != i:
				self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
				i = smallest
			else:
				break