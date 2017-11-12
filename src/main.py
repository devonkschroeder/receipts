import sys
import logging
import subprocess

from receipt import Receipt
from cards import cards
from meny import MenyReceiptParser

def get_arguments():
	if len(sys.argv) < 3:
		print("Must give store name and at least one image file")
		exit()

	store_name = sys.argv[1]
	images = sys.argv[2:]

	return store_name, images

def read_receipt_images(images):
	receipt_parts = []

	for image in images:
		# send through OCR program
		process = subprocess.Popen(
			["tesseract", image, "stdout", "-l", "nor", "-psm", "4"],
			stdout=subprocess.PIPE)
		(output, err) = process.communicate()
		exit_code = process.wait()
		receipt_parts.append(output.decode())

	full_receipt = "\n".join(receipt_parts)

	receipt_lines = full_receipt.split("\n")
	receipt_lines = list(filter(lambda x: x.strip() != "", receipt_lines))

	return receipt_lines

def main():

	logging.basicConfig(level=logging.DEBUG)

	store_name, images = get_arguments()
	receipt_lines = read_receipt_images(images)

	receipt_parser = None
	if store_name == "Meny":
		receipt_parser = MenyReceiptParser(receipt_lines, cards)

	# elif store_name == "Prix":
		# receipt_parser = CoopReceiptParser(receipt_lines, cards)

	# elif store_name == "Obs":
		# receipt_parser = CoopReceiptParser(receipt_lines, cards)

	# elif store_name == "Bunnpris":
		# receipt_parser = BunnprisReceiptParser(receipt_lines, cards)

	else:
		print("Must give store name: Meny, Prix, Obs, or Bunnpris.")
		exit()



main()
