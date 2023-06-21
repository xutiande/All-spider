import requests
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

url = 'https://preview.xkw.com/resource/oss/preview/rbm-preview-product/rbm/48538329/svg/1.svg?Expires=1682262718&Signature=DHnkNvRtEBAwQLT%2B%2BAj68t%2BAIk4%3D'

response = requests.get(url)

with open('svg\\svg.svg', 'wb') as f:
    f.write(response.content)

pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))

drawing = svg2rlg('svg\\svg.svg')

pdf_buffer = BytesIO()
renderPDF.drawToFile(drawing, pdf_buffer)

with open('pdf\\output.pdf', 'wb') as f:
    f.write(pdf_buffer.getvalue())
