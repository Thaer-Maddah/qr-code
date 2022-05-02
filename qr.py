# QR Code Generator
# This code published under General Public License version 2
# feel free to use it, copy, modify, redestribut it.

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.colormasks import SolidFillColorMask

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=4,
                   border=1
                   )
# Your data here
qr.add_data('Mr.Thaer Maddah\r\n') 
qr.add_data('Syrian Virtual University\r\n')
qr.add_data('As Suwayda Telecenter Manager\r\n')
qr.add_data('Email: thaeronline@gmail.com\r\n')
qr.add_data('Mobile: +963-991370060\r\n')
qr.add_data('Whatsapp: +963-991370060\r\n')
qr.add_data('Telegram: +963-991370060\r\n')

qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='orange',
                    # color_mask=SolidFillColorMask(back_color=(255, 255, 255),
                    #                               front_color=(4, 109, 34)),
                    color_mask=RadialGradiantColorMask(back_color=(247, 160, 0),
                                                       center_color=(80,80,80),
                                                       edge_color=(20,20,20)),
                    # color_mask=RadialGradiantColorMask(back_color=(0,0,0),
                    #                                    center_color=(255,255,255),
                    #                                    edge_color=(255,255,255)),

                    image_factory=StyledPilImage,
                    module_drawer=HorizontalBarsDrawer(),
                    # color_mask=SquareGradiantColorMask(),
                    )
#img = qr.make_image(fill_color="Black", back_color="Orange")
img.save('Info.png')
