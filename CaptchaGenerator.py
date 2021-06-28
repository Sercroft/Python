from captcha.image import ImageCaptcha

image = ImageCaptcha()

data = image.generate('abc')
image.write('abc', 'car.png')
