import sys, os
from reportlab.pdfgen import canvas

class GeneratePDF:
    def __init__(self, file_path):
        self.c = canvas.Canvas(file_path)
        self.__set_template()

    def next_page(self):
        self.c.showPage()
        self.__set_template()

    def apply_data(self, payout_data, well_data):
        self.__set_font(11)
        self.__text([(210, 765, self.__format_date(payout_data[1]))])
        self.__set_font(10, color='blue')
        self.__text([
                (185, 740, well_data[1]),
                (185, 730, str(well_data[2])),
                (185, 720, payout_data[3]),
                (185, 710, well_data[3]),
                (185, 700, payout_data[4]),
                (185, 690, payout_data[5]),
                (185, 680, self.__format_date(payout_data[2])),
                (185, 670, self.__format_date(payout_data[1]))
            ])
        self.__set_font(10, font='Helvetica-Bold')
        self.__centered_text([
                (335, 657, self.__format_date(payout_data[2])),
                (515, 657, self.__format_date(payout_data[1]))
            ])
        self.__set_font(8)
        self.__centered_text([
                (265, 433, str(payout_data[6]) + '%'),
                (265, 420, str(payout_data[7]) + '%'),
                (265, 407, str(payout_data[8]) + '%'),
                (265, 394, str(payout_data[9]) + '%'),
                (265, 381, str(payout_data[10]) + '%')
            ])
        self.__right_text([
                (365, 622, self.__currency(well_data[4])),
                (365, 609, self.__currency(well_data[7])),
                (365, 596, self.__currency(well_data[10])),
                (365, 550, self.__currency(well_data[13])),
                (365, 537, self.__currency(well_data[16])),
                (365, 524, self.__currency(well_data[19])),
                (365, 508, self.__currency(well_data[22])),
                (365, 466, self.__currency(well_data[31])),
                (365, 433, self.__currency(well_data[34])),
                (365, 420, self.__currency(well_data[37])),
                (365, 407, self.__currency(well_data[40])),
                (365, 394, self.__currency(well_data[43])),
                (365, 381, self.__currency(well_data[46])),
                (365, 365, self.__currency(well_data[49])),
                (455, 622, self.__currency(well_data[5])),
                (455, 609, self.__currency(well_data[8])),
                (455, 596, self.__currency(well_data[11])),
                (455, 550, self.__currency(well_data[14])),
                (455, 537, self.__currency(well_data[17])),
                (455, 524, self.__currency(well_data[20])),
                (455, 508, self.__currency(well_data[23])),
                (455, 466, self.__currency(well_data[32])),
                (455, 433, self.__currency(well_data[35])),
                (455, 420, self.__currency(well_data[38])),
                (455, 407, self.__currency(well_data[41])),
                (455, 394, self.__currency(well_data[44])),
                (455, 381, self.__currency(well_data[47])),
                (455, 365, self.__currency(well_data[50])),
                (545, 622, self.__currency(well_data[6])),
                (545, 609, self.__currency(well_data[9])),
                (545, 596, self.__currency(well_data[12])),
                (545, 550, self.__currency(well_data[15])),
                (545, 537, self.__currency(well_data[18])),
                (545, 524, self.__currency(well_data[21])),
                (545, 508, self.__currency(well_data[24])),
                (545, 466, self.__currency(well_data[33])),
                (545, 433, self.__currency(well_data[36])),
                (545, 420, self.__currency(well_data[39])),
                (545, 407, self.__currency(well_data[42])),
                (545, 394, self.__currency(well_data[45])),
                (545, 381, self.__currency(well_data[48])),
                (545, 365, self.__currency(well_data[51]))
            ])
        self.__set_font(8, color='red')
        self.__right_text([
                (365, 495, self.__currency(well_data[25])),
                (365, 482, self.__currency(well_data[28])),
                (455, 495, self.__currency(well_data[26])),
                (455, 482, self.__currency(well_data[29])),
                (545, 495, self.__currency(well_data[27])),
                (545, 482, self.__currency(well_data[30]))
            ])
        self.__set_font(8, font="Helvetica-Bold")
        self.__right_text([(545, 335, self.__currency(well_data[52]))])

    def output_file(self):
        self.c.save()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
    def __set_font(self, size, font='Helvetica', color='black'):
        rgb = {
                'black': (0, 0, 0), 
                'blue': (0.10, 0.10, 1.00),
                'red': (1.00, 0, 0)
            }
        self.c.setFont(font, size)
        self.c.setFillColorRGB(rgb[color][0], rgb[color][1], rgb[color][2])

    def __currency(self, amount):
        if amount == 0.0:
            return "- "
        else:
            return "{:,.2f}".format(amount)

    def __text(self, text_list):
        for t in text_list:
            self.c.drawString(t[0], t[1], t[2])
    
    def __centered_text(self, text_list):
        for t in text_list:
            self.c.drawCentredString(t[0], t[1], t[2])

    def __right_text(self, text_list):
        for t in text_list:
            self.c.drawRightString(t[0], t[1], t[2])


    def __draw_lines(self, coordinate_list):
        for c in coordinate_list:
            self.c.line(c[0], c[1], c[2], c[3])

    def __format_date(self, date):
        m = date[:2]

        if m == '01' or m == '1/':
            m_txt = "Jan"
        elif m == '02' or m == '2/':
            m_txt = "Feb"
        elif m == '03' or m == '3/':
            m_txt = "Mar"
        elif m == '04' or m == '4/':
            m_txt = "Apr"
        elif m == '05' or m == '5/':
            m_txt = "May"
        elif m == '06' or m == '6/':
            m_txt = "Jun"
        elif m == '07' or m == '7/':
            m_txt = "Jul"
        elif m == '08' or m == '8/':
            m_txt = "Aug"
        elif m == '09' or m == '9/':
            m_txt = "Sep"
        elif m == '10':
            m_txt = "Oct"
        elif m == '11':
            m_txt = "Nov"
        elif m == '12':
            m_txt = "Dec"
        else:
            m_txt = "ERROR"

        if date[1] == '/' and date[3] == '/':
            day = date[2]
        elif date[1] == '/':
            day = date[2:4]
        else:
            day = date[3:5]
        
        return m_txt + " " + day + ", 20" +  date[-2] + date[-1]

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
                (410, 670, "Period"),
                (408, 657, "Activity")
            ])
        self.__centered_text([
                (335, 670, "Balance"),
                (515, 670, "Balance")
            ])
        self.c.drawImage(self.resource_path("logo_burned.png"), 460, 720, 64, 76)
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
