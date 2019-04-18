#Purser, Charles N.
#cnp1474
#04-02-2019

import numpy as np 
import matplotlib.image as img 
import matplotlib.pyplot as plt 
from skimage.feature import match_template


def img2gray(pic) : 
    return np.dot(pic[...,:3], [0.2989, 0.587, 0.114])

def findImage(mainImage, template) :
    main = img2gray(img.imread(mainImage))
    tem = img2gray(img.imread(template))

    plt.imshow(main, cmap='gray')
    plt.show()
    plt.imshow(tem, cmap='gray')
    plt.show()

    #correlate and find max value
    results = match_template(main, tem)
    maxcorr = np.where(results == np.max(results))
    x = int(maxcorr[0])
    y = int(maxcorr[1])
    print(tuple((x,y)))

    #black out main where template is 
    for i in range(x,x+len(tem)+1):
        for j in range(y, y+len(tem)+1):
            main[i][j]=0

    plt.imshow(main, cmap='gray')
    plt.show()


#############  main  #############
if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"

    findImage(mainImage, template)

