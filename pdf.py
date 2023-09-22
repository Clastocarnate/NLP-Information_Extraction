import jinja2
import pdfkit
from datetime import *
from PretrainedIE import lessor, lesse, rent_amount, security_deposit, from_date, to_date, time_duration



today_date = datetime.today().strftime("%d %b, %Y")

context = {'today_date':today_date, 'lessor':lessor, 'lesse':lesse, 'rent': rent_amount, 'duration': time_duration, 'from_date':from_date,'end_date':to_date}

template_loader =  jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('Agreement.html')
output = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
pdfkit.from_string(output, 'Rent_Agreement.pdf', configuration=config)
# '/Users/madhuupadhyay/miniforge3/lib/python3.10/site-packages (0.2)'