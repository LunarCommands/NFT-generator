from PIL import Image, ImageDraw
import random


def generate_art():

    # Creating canvas
    image_size_px = (128, 128)
    image_bg_color = (156, 100, 255)
    image = Image.new("RGB", image_size_px, image_bg_color)

    # Drawing rectangle
    draw = ImageDraw.Draw(image)
    rectangle_xy = ((random.randint(15, 113), random.randint(15, 113)), (random.randint(15, 113), random.randint(15, 113)))
    rectangle_color = (0, 0, 0)
    draw.rectangle(rectangle_xy, rectangle_color)

    # Drawing circle
    circle_x = random.randint(15, 113)
    circle_y = random.randint(15, 113)
    draw.ellipse((circle_x, circle_y, circle_x + 50, circle_y + 50), fill='black', outline='black')


    image.save("test_image.png")


if __name__ == '__main__':
    generate_art()
