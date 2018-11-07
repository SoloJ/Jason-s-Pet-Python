import luma.emulator.device
from PIL import Image
im = Image.open("/Users/jasonsolomon/PycharmProjects/Jason-s-Pet-Python/Snake/uen_logo_print_bw.bmp")

luma.emulator.device.pygame.display(im)


