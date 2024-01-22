from PIL import Image, ImageDraw, ImageFont
from pillow_heif import register_heif_opener
import os

register_heif_opener()

PIXEL_FILL_CHARS_SORTED_INC = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
CHAR_WIDTH, CHAR_HEIGHT = 10, 18 #based on observed font's letter width and height
CHAR_ASPECT_RATIO = CHAR_WIDTH / CHAR_HEIGHT
AVAILABLE_IMAGE_MODES = {
    'RGB Image': 'RGB',
    'Grayscale Image': 'L',
    'Black / White Image': '1',
    '8-bit Image': 'P'
}
AVAILABLE_TEXT_MODES = {
    'ASCII TEXT': 'ascii_text'
}

def get_ascii_char(px_val, fill_vals=''):
    if not fill_vals:
        fill_vals = PIXEL_FILL_CHARS_SORTED_INC
    ind = int((px_val / 256) * len(fill_vals))
    ascii_char = fill_vals[ind]
    return ascii_char

def pre_process(img):
    scale_factor = 0.09
    img = img.resize(
        (int(img.width * scale_factor), int(img.height * scale_factor * CHAR_ASPECT_RATIO))
    )
    return img

def gen_ascii_image(img, mode='RGB'):
    img = pre_process(img)
    px = img.load()
    result_img = Image.new('RGB', (CHAR_WIDTH * img.width, CHAR_HEIGHT * img.height), color=(0, 0, 0))
    result_img_draw = ImageDraw.Draw(result_img)
    font = ImageFont.truetype('fonts/lucon.ttf', 15)

    for h in range(img.height):
        for w in range(img.width):
            r, g, b = px[w, h]
            ascii_char = get_ascii_char(int(sum((r, g, b))/3))
            result_img_draw.text((w*CHAR_WIDTH, h*CHAR_HEIGHT), ascii_char, font=font, fill=(r, g, b))
    
    result_img = result_img.convert(AVAILABLE_IMAGE_MODES[mode])
    return result_img

def gen_ascii_text(img, mode='ascii_text'):
    pass