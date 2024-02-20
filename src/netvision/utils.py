from PIL import Image
from os.path import splitext

def create_thumbnail_function(path, size=(256, 256)):
    img = Image.open(path)
    img.thumbnail(size)
    new_path = splitext(path)[0] + "_thumb" + splitext(path)[1]
    img.save(new_path)
    return new_path
