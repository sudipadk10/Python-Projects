from rembg import remove
from PIL import Image
Input_path = "raw.jpg"
output_path = "output.png"
input = Image.open(Input_path)
output = remove(input)
output.save(output_path)
