from reportlab.pdfgen import canvas

class GeneratePDF:
    def __init__(self, file_path):
        self.c = canvas.Canvas(file_path)
        self.__set_template()

    def next_page(self):
        self.c.showPage()
        self.__set_template()

    # def apply_data(self, payout_data, well_data):

    def output_file(self):
        self.c.save()

    def __set_template(self):
        self.__set_font(14, color='blue')
        self.__text([(54, 780, "Payout Statement")])
        self.__set_font(12)
        self.__text([(54, 765, "Through Production Period:  ")])
        self.__set_font(10, color='blue')
        self.__text([
                (64, 740, "Well Name"), 
                (64, 730, "Well ID"),
                (64, 720, "Operator"), 
                (64, 710, "API"), 
                (64, 700, "Payout Type"), 
                (64, 690, "Owner"), 
                (64, 680, "Previous Statement Date"),
                (64, 670, "Current Statement Date")
            ])
        self.__set_font(10, font='Helvetica-Bold')
        self.__text([(54, 635, "Gross Sales Volumes:")])
        self.__set_font(10)
        self.__text([
                (64, 622, "Gas (mcf)"), 
                (64, 609, "Condensate (bbl)"),
                (64, 596, "NGL (gal)")
            ])
        self.__set_font(10, font='Helvetica-Bold')
        self.__text([(54, 576, "Revenues:")])
        self.__set_font(10)
        self.__text([
                (64, 563, "Gross Sales Revenue"), 
                (74, 550, "Gas"),
                (74, 537, "Condensate"), 
                (74, 524, "NGL"), 
                (84, 508, "Total Gross Sales Revenue"),
                (74, 495, "Less: Royalty Interest"), 
                (74, 482, "Less: Production Taxes"),
                (84, 466, "Total Net Sales Revenue")
            ])
        self.__set_font(10, font='Helvetica-Bold')
        self.__text([(54, 446, "Expenditures:")])
        self.__set_font(10)
        self.__text([
                (64, 433, "Intangible Drilling & Completion Costs"), 
                (64, 420, "Tangible Equipment Costs"),
                (64, 407, "Lease Operating Expenses"),
                (64, 394, "Workover Costs"),
                (64, 381, "Marketing & Transportation Costs"),
                (74, 365, "Total Expenditures"),
                (245, 446, "Penalties")
            ])
        self.__set_font(10, font='Helvetica-Bold')
        self.__text([
                (175, 335, "Payout Balance"),
                (320, 670, "Balance"),
                (410, 670, "Period"),
                (408, 657, "Activity"),
                (500, 670, "Balance")
            ])
        self.c.drawImage("logo_burned.png", 460, 720, 64, 76)
        self.c.setLineWidth(0.8)
        self.__draw_lines([
                (390, 650, 460, 650),
                (300, 650, 370, 650),
                (480, 650, 550, 650),
                (300, 518, 370, 518),
                (300, 476, 370, 476),
                (300, 375, 370, 375),
                (390, 518, 460, 518),
                (390, 476, 460, 476),
                (390, 375, 460, 375),
                (480, 518, 550, 518),
                (480, 476, 550, 476),
                (480, 375, 551, 375),
                (480, 346, 550, 346),
                (480, 332, 550, 332),
                (480, 330, 550, 330)
            ])
        self.__set_font(11, font='Helvetica-Bold')
        self.__text([
                (303, 507, "$"),
                (303, 465, "$"),
                (303, 364, "$"),
                (393, 507, "$"),
                (393, 465, "$"),
                (393, 364, "$"),
                (483, 507, "$"),
                (483, 465, "$"),
                (483, 364, "$"),
                (483, 335, "$")
            ])

    def __set_font(self, size, font='Helvetica', color='black'):
        rgb = {'black': (0, 0, 0), 'blue': (0.10, 0.10, 1.00)}
        self.c.setFont(font, size)
        self.c.setFillColorRGB(rgb[color][0], rgb[color][1], rgb[color][2])

    def __text(self, text_list):
        for t in text_list:
            self.c.drawString(t[0], t[1], t[2])

    def __draw_lines(self, coordinate_list):
        for c in coordinate_list:
            self.c.line(c[0], c[1], c[2], c[3])

pdf = GeneratePDF("test.pdf")
pdf.next_page()
pdf.output_file()