	def lower_bound(self, x):
		return self.__bound(x, True)

	def upper_bound(self, x):
		return self.__bound(x, False)

	def __bound(self, x, is_lower):
		if not self.root:
			return None
		node = self.root
		res = None
		while node:
			if (is_lower and node.key < x) or (not is_lower and node.key > x):
				res = (node.key, node.val)
				if is_lower:
					node = node.right
				else:
					node = node.left
			else:
				if is_lower:
					node = node.left
				else:
					node = node.right
		return res
