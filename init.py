import matplotlib
import matplotlib.font_manager as fm
def initilize():
    font_location = 'C:/Users/승주/Downloads/FontPackgeWindow/12롯데마트드림Bold.ttf'  

    font_name = fm.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family = font_name)
