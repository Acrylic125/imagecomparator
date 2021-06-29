import numpy
from PIL import Image
from numpy import asarray


# Compares both images based on it's pixel RGB values.
# lambdaOnSuccess(tuple1, tuple2) - Executes on success.
# lambdaOnFailure(tuple1, tuple2) - Executes on failure.
def compare(image1, image2, lambdaOnSuccess, lambdaOnFailure):
    data1 = asarray(image1)
    data2 = asarray(image2)
    width1, height1 = image1.size
    width2, height2 = image2.size
    widthForComparison = min(width1, width2)
    heightForComparison = min(width2, height2)

    for w in range(0, widthForComparison):
        for h in range(0, heightForComparison):
            tup1 = data1[h][w]
            tup2 = data2[h][w]
            if tup1[0] == tup2[0] and tup1[1] == tup2[1] and tup1[2] == tup2[2]:
                if lambdaOnSuccess is not None:
                    lambdaOnSuccess(tup1, tup2)
            elif lambdaOnFailure is not None:
                lambdaOnFailure(tup1, tup2)


def increaseCount(tuple1, tuple2):
    global count
    count += 1


count = 0
# Open the image form working directory
image = Image.open('sample.jpg')
width, height = image.size
image = image.crop((0, 140, width, height))
image1 = image.crop((0, 0, width / 2, height))
image2 = image.crop((width / 2, 0, width, height))
image1.save("img1.jpg")
image2.save("img2.jpg")
compare(image1, image2, None, increaseCount)
print(count, " s1=", image1.size, " s2=", image2.size)
image1.show()
image2.show()
