from PIL import Image
from numpy import array, moveaxis, indices, dstack
from pandas import DataFrame


img0= Image.open("Lena.jpg").convert('LA')
img1 =img0.resize((300,300))
img1.save('greyscale.png')
img= Image.open("greyscale.png")

pixels = img.convert("RGB")
rgbArray = array(pixels.getdata()).reshape(img.size + (3,))
indicesArray = moveaxis(indices(img.size), 0, 2)
allArray = dstack((indicesArray, rgbArray)).reshape((-1, 5))

df = DataFrame(allArray, columns=["y", "x", "red","green","blue"])
print(df.head())
df.to_csv("data.csv",index=False)