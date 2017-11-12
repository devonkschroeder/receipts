from receiptparser import ReceiptParser

class MenyReceiptParser(ReceiptParser):

	def __init__(self, receipt_lines, cards):
		super(MenyReceiptParser, self).__init__(receipt_lines, cards)
