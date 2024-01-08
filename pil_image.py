from PIL import Image
from sklearn.datasets import load_sample_images


def main():
    china = load_sample_images().images[0]
    im_china = Image.fromarray(china)
    #im_china.show()
    im_china.save("./data/china.png")
    im = Image.open("./data/china.png")
    im.show()
    im_grey = im.convert("L") # convert to grey scale
    im_grey.save("./data/china_grey.png")
    china_grey = Image.open("./data/china_grey.png")
    china_grey.show()


if __name__ == "__main__" :
    main()
