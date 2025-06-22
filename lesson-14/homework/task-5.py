import numpy as np
from PIL import Image

def load_image(path):
    with Image.open(path) as image:
        return np.array(image)

def flip_image(img_arr):
    flipped = np.flip(img_arr, axis=(0, 1))
    return Image.fromarray(flipped)

def add_noise(img_arr, amount=30):
    noise = np.random.randint(-amount, amount + 1, img_arr.shape, dtype='int16')
    noisy_img = np.clip(img_arr.astype('int16') + noise, 0, 255).astype('uint8')
    return Image.fromarray(noisy_img)

def brighten_channels(img_arr, channel='red', value=40):
    channel_map = {'red': 0, 'green': 1, 'blue': 2}
    ch = channel_map.get(channel.lower(), 0)
    bright_img = img_arr.copy()
    bright_img[:, :, ch] = np.clip(bright_img[:, :, ch] + value, 0, 255)
    return Image.fromarray(bright_img)

def apply_mask(img_arr, mask):
    masked_img = img_arr.copy()
    masked_img[~mask] = 0
    return Image.fromarray(masked_img)


img_arr = load_image('images/birds.jpg')

