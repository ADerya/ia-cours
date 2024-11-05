from PIL import Image

image = Image.open("../../images/image.jpg")

resized_image = image.resize((300,300))

rotated_image = image.rotate(45)

rotated_image.save("../../images/update_image.jpg")

print("toto")