from PIL import Image

from PIL import ImageFilter

import math

 

# Ecuacion Operador Logarı́tmico

def logTransform(c, f):

    g = c * math.log(float(1 + f),10);

    return g;

 

#Aplicando logarithmic para la transformación de la imágen

def logTransformImage(image, outputMax = 255, inputMax=255):

    c = outputMax/math.log(inputMax+1,20);

   

    # Obteniendo Obtenga el valor de píxel en la posición (x, y) de la imagen

    for i in range(0, img.size[0]-1):

        for j in range(0, img.size[1]-1):

            # Obteniendo el valor de píxel en la posición (x, y) de la imagen

            f = img.getpixel((i,j));

           

            # Haciendo la transformación del registro del píxel

            redPixel    = round(logTransform(c, f[0]));

            greenPixel  = round(logTransform(c, f[1]));

            bluePixel   = round(logTransform(c, f[2]));

 

            # Modificando la imagen con los valores de píxeles transformados

            img.putpixel((i,j),(redPixel, greenPixel, bluePixel));

 

    return image;

   

# Mostrando la imagen original
imageFileName = "exp_5.jpg";

img = Image.open(imageFileName);

img.show();

 

# Mostrando la imagen después de aplicar la transformación logarítmica

logTransformedImage = logTransformImage(img);

logTransformedImage.show();