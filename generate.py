from PIL import Image, ImageDraw, ImageFont
import random

questions = ["Levi", "ONIZUKA"]


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

    im.save(f"char/{idx}.png", "PNG")


def main():
    i = 1
    for question in questions:
        temp = list(question.replace(" ", "").upper())
        random.shuffle(temp)
        temp = "".join(temp)
        gen_image(i, temp)
        i += 1


main()

# gen_image(0, "CODEGEASS")
