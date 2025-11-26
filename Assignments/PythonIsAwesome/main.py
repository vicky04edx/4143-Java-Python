from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Open image
img = Image.open("my_photo.jpg")
draw = ImageDraw.Draw(img)

# Load a font 
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)

# Draw text
draw.text((100, 50), "Hello!", fill="blue", font=font)

# Convert to grayscale, there are 2 ways of 
# converting to grayscale

# Option 1: 
enhanceImg = ImageEnhance.Color(img)
saturatedImg = enhanceImg.enhance(0)  

#Option 2:
# gray_img = img.convert("L")
# small_gray = gray_img.resize((300, 300))

# Resize image
small_gray = saturatedImg.resize((300, 300))   

# Show edited image
small_gray.show()

# Save edited image
small_gray.save("my_photo_gray_small.jpg")
