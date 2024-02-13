from PIL import Image

# Load the AVIF image
avif_image = Image.open("assets/cards.avif")

# Save it as PNG
avif_image.save("assets/cards.png")
