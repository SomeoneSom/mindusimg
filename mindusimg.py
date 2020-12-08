from os import getcwd
from PIL import Image
#write result cell1 0
dir = getcwd() + "/"
fname = input("Image name?\n")
output = open(dir + "out.txt", 'w')
with Image.open(dir + fname) as im:
	im = im.resize((80, 80))
	bstr = ''
	count = 0
	for x in range(0, 80):
		for y in range(79, -1, -1):
			r, g, b, alpha = im.getpixel((x, y))
			bstr = ("1" if r > 127 else "0") + bstr
			bstr = ("1" if g > 127 else "0") + bstr
			bstr = ("1" if b > 127 else "0") + bstr
			if len(bstr) == 63:
				bstr = "0b" + bstr
				output.write("write " + bstr + " bank1 " + str(count) + "\n")
				count += 1
				bstr = ''
while len(bstr) < 63:
	bstr = "000" + bstr
bstr = "0b" + bstr
output.write("write " + bstr + " bank1 " + str(count))
output.write("""
set x 0
set y 79
set a -1
op add a a 1
read pixels bank1 a
set b -1
op add b 1 b
op mod r pixels 2
op mul r r 255
op shr pixels pixels 1
op mod g pixels 2
op mul g g 255
op shr pixels pixels 1
op mod bl pixels 2
op mul bl bl 255
op shr pixels pixels 1
draw color r g bl 255 0 0
draw rect x y 1 1 0 0
drawflush display1
op add x x 1
jump 328 lessThan x 80
op sub y y 1
set x 0
jump 311 lessThan b 20
jump 308 lessThan a 304""")
print('Done!')
output.close()
