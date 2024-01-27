import requests
from PIL import Image

SAMPLE_IMAGE_URLS = [
    "https://wallpapers-clan.com/wp-content/uploads/2023/11/marvel-iron-man-in-destroyed-suit-desktop-wallpaper-preview.jpg", 
    "https://i.ytimg.com/vi/yGNjoKGMF4Y/maxresdefault.jpg", 
    "https://images.hdqwalls.com/wallpapers/iron-man-abstract-4k-b6.jpg"
]

def load_imgs_html():
    # get_uri = lambda url: url.split('//')[1]
    html_img = lambda img_url: f"<a href='#' id='{img_url}'><img width='70%' src='{img_url}'></a>"
    html_content = ""
    count = 1
    for img_url in SAMPLE_IMAGE_URLS:
        html_content += html_img(img_url) + "<br/>\n"*3
    return html_content