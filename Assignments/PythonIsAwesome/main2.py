from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("sunsetSanDiego.jpg")

# Blur the image:
# when radius=1 (slight blur), when radius=10 (very blurry)
blurred = img.filter(ImageFilter.GaussianBlur(radius=5))

# Increase saturation:
# 1.0 = normal, 2.0 = very saturated, 0 = grayscale
enhancer = ImageEnhance.Color(blurred)
saturated = enhancer.enhance(4)  


# Crop the image 
# Crop box = (left, top, right, bottom)
cropped = saturated.crop((50, 50, 1500, 900))

cropped.show()
cropped.save("sunset_blur_sat_crop.jpg")
