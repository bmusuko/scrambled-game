from PIL import Image, ImageDraw, ImageFont
import random

questions = ["Levi", "ONIZUKA"]
out_folder = "image"


def gen_image(idx, msg):
    W, H = (500, 120)

    im = Image.new("RGBA", (W, H), "white")
    fontsize = 24
    font = ImageFont.truetype("arial.ttf", fontsize)
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg, font=font)
    draw.text(
        ((W - w) / 2, (H - h) / 2),
        msg,
        fill="black",
        font=font,
    )

    im.save(f"{out_folder}/{idx}.png", "PNG")


def main():
    i = 1
    for question in questions:
        temp = list(question.replace(" ", "").upper())
        start = temp[0]
        new_temp = temp[1:]
        random.shuffle(new_temp)
        new_temp.insert(random.randint(1, len(new_temp)), start)
        new_temp = "".join(new_temp)
        gen_image(i, new_temp)
        i += 1


main()
