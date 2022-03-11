# QR-Code Generator by Yara
# 09.03.2022
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas

def yara_qr_code(barcode_value):
    file_Name = canvas.Canvas("yara_youtube_qr-code.pdf")
    qr_code = qr.QrCodeWidget(barcode_value)
    qr_code.barWidth = 145
    qr_code.barHeight = 145
    qr_code.qrVersion = 1
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing()
    d.add(qr_code)
    renderPDF.draw(d, file_Name, 15, 405)
    file_Name.save()

if __name__ == "__main__":
    #yara_qr_code("www.youtube.com/watch?v=Hx_JWNmfJKU")
    #yara_qr_code(("www.youtube.com/watch?v=2YSXVGtj3xU"))
    yara_qr_code("www.youtube.com/watch?v=-5u_QqI4Hbg&t=81s")