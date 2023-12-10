import io
import base64
import numpy as np
from io import BytesIO
from PIL import Image


def load_image(binary_image):
    image           = Image.open(io.BytesIO(binary_image))
    image_array     = np.array(image)
    image           = image_array / 255.0
    image           = image_array.reshape(28,28,1)
    plot_image      = Image.fromarray(image_array)
    return image,plot_image

def convert_to_binary(file_name):
    with open (file_name,'rb') as file:
        binary_data = file.read()
        return binary_data
    
def base64_decode(base64_encorded):
    image_bytes = base64.b64decode(base64_encorded)
    image       = Image.open(BytesIO(image_bytes))
    image_array = np.array(image)
    return image_array

