from pymatting import cutout
import os

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp')

images = 'images'
alpha = 'res'
merged = 'merged'

for name in os.listdir(images):
    # Check if the file is an image file
    if os.path.splitext(name)[1].lower() in IMAGE_EXTENSIONS:
        imalpha = os.path.join(alpha, os.path.splitext(name)[0] + '.png')
        imimages = os.path.join(images, name)
        immerged = os.path.join(merged, os.path.splitext(name)[0] + '.png')
        cutout(imimages, imalpha, immerged)
        print(f'saved in {immerged}')
