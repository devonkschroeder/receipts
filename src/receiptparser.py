import logging
import re

class ReceiptParser:

	def __init__(self, receipt_lines, cards):
		self._receipt_lines = receipt_lines
		self._date = self._get_date()
		self._card_number = self._get_card_number(cards)

	def _validate_date(self, line_given):
		# regular expression for reading date
		match = re.search("^(\d\d).?(\d\d).?(\d\d\d\d)", line_given)
		date = None
		if match:
			date = (match.group(1), match.group(2), match.group(3))
		return date

	def _get_date(self):
		date = self._validate_date(self._receipt_lines[-6])
		logging.debug(self._receipt_lines[-6])
		while date == None:
			date = input("Could not find date. What is the date for this receipt? (dd.mm.yyyy) ")
			date = self._validate_date(date)
		return date

	def _validate_card_number(self, number, cards):
		return number in cards.keys()

	def _get_card_number(self, cards):
		match = re.search("(\d{4}).?(?:\d|\w)$", self._receipt_lines[-11])
		if not match:
			match = re.search("(\d{4}).?(?:\d|\w)$", self._receipt_lines[-10])
		card_number = None
		if match:
			card_number = match.group(1)
			if not self._validate_card_number(card_number, cards):
				card_number = None
		while card_number == None:
			card_number = input("Could not find card number. Enter the four-digit card number (or 0000 if the purchase was made with cash). ")
			if not self._validate_card_number(card_number):
				card_number = None
		return card_number
