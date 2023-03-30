from unidecode import unidecode
import fitz
import pandas as pd

print('Hello, world!')

# add your imports to the top

my_path = "/Volumes/MobileDev/learning/python/Naushad Nizar Ali.pdf"

doc = fitz.open(my_path)

output = []

for page in doc:

    output += page.get_text("blocks")

previous_block_id = 0  # Set a variable to mark the block id

for block in output:

    if block[6] == 0:  # We only take the text

        # if previous_block_id != block[5]:  # Compare the block number

        #     print("\n")

        plain_text = unidecode(block[4])

print(plain_text)
