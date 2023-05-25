import matplotlib.font_manager as fonm
font_list = [font.name for font in fonm.fontManager.ttflist]
for f in font_list:
    print(f"{f}.ttf")