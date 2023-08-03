from PIL import Image
import os

def clean_image_data(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.ANTIALIAS) 
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))

    return new_im

if __name__ == '__main__':
    path = "images/raw_images"
    dirs = os.listdir(path)
    final_size = 512

    new_path = "images/cleaned_images"
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    for n, item in enumerate(dirs[:5], 1): # Limit/increase number of processed images
        try
            image = Image.open(path + item)
            new_image = clean_image_data(final_size, image)
            new_image.save(f'{new_path}{n}_resized.jpg')
        except
            print(f'Resizing failed for {item}.')