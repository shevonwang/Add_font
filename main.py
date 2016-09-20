# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def add_font(path):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    ft = ImageFont.truetype('C:/WINDOWS/Fonts/SIMYOU.TTF', 40)
    draw.text((30, 30), u'兰二娃娃', font=ft, fill='red')
    ft = ImageFont.truetype("C:/WINDOWS/Fonts/SIMYOU.TTF", 40)
    draw.text((30, 100), u'兰二娃娃', font=ft, fill='green')
    ft = ImageFont.truetype("C:/WINDOWS/Fonts/SIMYOU.TTF", 40)
    draw.text((30, 200), u'兰二娃娃', font=ft, fill='blue')
    ft = ImageFont.truetype("C:/WINDOWS/Fonts/SIMLI.TTF", 40)
    draw.text((30, 300), u'兰二娃娃', font=ft, fill='red')
    ft = ImageFont.truetype("C:/WINDOWS/Fonts/STXINGKA.TTF", 40)
    draw.text((30, 400), u'兰二娃娃', font=ft, fill='yellow')
    img.show()
    img.save('E:/other/result.jpg', 'jpeg')


if __name__ == '__main__':
    add_font('E:/other/test1.jpg')