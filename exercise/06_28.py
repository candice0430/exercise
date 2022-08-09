from PIL import Image,ImageDraw,ImageFont
import sys
'''
0000、将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
sss
'''

# img = Image.open('./pic/head.jpg')
# (left, upper, right, lower) = (20, 20, 100, 100)

#     # Here the image "im" is cropped and assigned to new variable im_crop
# im_crop = img.crop((left, upper, right, lower))
# im_crop.save('./pic/a.jpg')
# img1 = img.copy()

# img1.thumbnail((50,50))
# img1.save('./pic/c.jpg')
# # img1.show()
# print(img1.verify())
# print(img1.size)
# print(img.mode,img.size,img.format)
# print(img)

# draw = ImageDraw.Draw(img)
# draw.line((0,0)+img.size,fill=128)
# print((0,0)+img.size)
# draw.line((0, img.size[1], img.size[0], 0), fill=128,width=3,joint='curve')

#     # write to stdout
# # img.save(sys.stdout, "PNG")
# img.save('./pic/d.jpg')
# # img.show()

# with Image.open("./pic/head.jpg").convert("RGBA") as img:

#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", img.size, (255, 0, 0, 0))
#     # get a font
#     fnt = ImageFont.truetype("./pic/FreeMono.ttf", 40)
#     # get a draw context
#     draw = ImageDraw.Draw(txt,"RGBA")
#     # draw text
#     # draw text, half opacity
#     draw.text((10, 10), "Hello", font=fnt, fill=(255, 0, 0, 128))
#         # draw text, full opacity
#     draw.text((img.size[0]-30, 0), "4", font=fnt, fill=(255, 0, 0, 255),)
#     out = Image.alpha_composite(img, txt)
#     out.show()

def add_num(path):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("./pic/FreeMono.ttf", 40)

    draw.text((img.size[0]-30, 0), "4", font=fnt, fill=(255, 0, 0, 255),)
    img.show()

add_num('./pic/head.jpg')

from db import db_operator
print(id(db_operator))

"""
aaaa
"""