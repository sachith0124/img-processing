from PIL import Image, ImageDraw, ImageFont
from pillow_heif import register_heif_opener
import os

register_heif_opener()

CACH_PATH = 'cache'

def get_ascii_char(px_val, fill_vals=''):
    PIXEL_FILL_CHARS_SORTED_INC = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    if not fill_vals:
        fill_vals = PIXEL_FILL_CHARS_SORTED_INC
    ind = int((px_val / 256) * len(fill_vals))
    ascii_char = fill_vals[ind]
    return ascii_char

def img2ascii_image(img, format='RGB'):
    # img = Image.open(img_file)
    CHAR_WIDTH, CHAR_HEIGHT = 10, 18 #based on observed font's letter width and height
    CHAR_ASPECT_RATIO = CHAR_WIDTH / CHAR_HEIGHT
    scale_factor = 0.09

    img = img.resize(
        (int(img.width * scale_factor), int(img.height * scale_factor * CHAR_ASPECT_RATIO))
    )
    img_width, img_height = img.size

    px = img.load()

    output_image = Image.new('RGB', (CHAR_WIDTH * img_width, CHAR_HEIGHT * img_height), color=(0, 0, 0))
    output_image_draw = ImageDraw.Draw(output_image)
    font = ImageFont.truetype('fonts/lucon.ttf', 15)

    for h in range(img_height):
        for w in range(img_width):
            r, g, b = px[w, h]
            ascii_char = get_ascii_char(int(sum((r, g, b))/3))
            output_image_draw.text((w*CHAR_WIDTH, h*CHAR_HEIGHT), ascii_char, font=font, fill=(r, g, b))
    return output_image
