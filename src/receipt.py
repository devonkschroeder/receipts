class Receipt:

	def __init__(self, account, date, items, total, number_of_goods):
		self._account = account
		self._date = date
		self._items = items # (item, category, price)
		self._total = total
		self._number_of_goods = number_of_goods
