# import module
from audioop import add
from sqlite3 import adapt
from bs4 import BeautifulSoup as Soup
import pdfkit
import openpyxl
import openpyxl.utils

# load excel with its path
wrkbk = openpyxl.load_workbook("wheelingAssessmentList3.xlsx")


sh = wrkbk.active
html = """
<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">@import url(https://themes.googleusercontent.com/fonts/css?kit=soa_V42eXREs8LDkwBiWS64fnxpW6PVRuPCJ3776g6W3564wZKWgxe7lqyJUI_F2BT-CpE89oaBGkvzEaxwQIY4gGOrlNiKUx8O7TRVoFSTOxcWZehlVvILrEYceq3Jt);.page{text-align:center;width:10.5in;height:11in}.title-container{display:flex;display:-webkit-box;justify-content:flex-start;-webkit-justify-content:start;flex-direction:column;-webkit-flex-direction:column;-webkit-box-orient:vertical;align-items:center;-webkit-align-items:center;-webkit-box-align:center;text-align:left;padding:4rem 0}.title{margin:0;font-size:2.5rem}.subtitle{margin:0;font-size:2rem;padding-bottom:1rem}.contact{margin:0;font-size:1.25rem}.agreement{text-align:center;padding-bottom:4rem;font-size:2rem}.underline{border-bottom:1px solid #000}.description{text-align:left;font-size:1.5rem}.input-title{font-size:2rem}.data-input{display:flex;display:-webkit-box;-webkit-box-pack:center;flex-direction:row;-webkit-flex-direction:row;-webkit-box-orient:horizontal;flex:1;-webkit-flex:1;-webkit-box-flex:1;width:100%;align-items:flex-end;-webkit-align-items:flex-end;-webkit-box-align:end;height:3.5in}.left{display:flex;display:-webkit-box;-webkit-box-pack:center;flex-direction:column;-webkit-flex-direction:column;-webkit-box-orient:vertical;flex:1;-webkit-flex:1;-webkit-box-flex:1;width:50%}.right{display:flex;display:-webkit-box;-webkit-box-pack:center;flex-direction:column;-webkit-flex-direction:column;-webkit-box-orient:vertical;flex:1;-webkit-flex:1;-webkit-box-flex:1;width:50%}.middle{width:10px}.underline-data{display:flex;display:-webkit-box;-webkit-box-pack:start;border-bottom:1px solid #000;flex-direction:row;-webkit-flex-direction:row;-webkit-box-orient:horizontal;flex:1;-webkit-flex:1;-webkit-box-flex:1;font-size:1.25rem;font-weight:700}.input-container{display:flex;display:-webkit-box;-webkit-box-pack:center;flex-direction:row;-webkit-flex-direction:row}.input-row{display:flex;display:-webkit-box;-webkit-box-pack:center;flex-direction:row;-webkit-flex-direction:row;align-items:baseline;-webkit-align-items:baseline;-webkit-box-align:baseline;font-size:1.25rem}.input-title{font-size:1.75rem;padding-bottom:5rem;text-decoration:underline}.input-subtitle{font-size:1.5rem}.signature{display:flex;display:-webkit-box;-webkit-box-pack:start;font-size:1.5rem;flex:2;-webkit-flex:2;-webkit-box-flex:2}li{padding-bottom:1rem}.required-sentence{text-align:right}.required{font-weight:700}.required-text{font-style:italic;font-weight:700}.data-input-item{font-size:1.5rem}</style></head><body><div class="page"><div class="title-container"><h1 class="title">Barry Gimbel & Associates</h1><h2 class="subtitle">Property Tax Refund/Assessment Specialists</h2><h6 class="contact">790 Frontage Road, Suite 330, Northfield, IL 60093</h6><h6 class="contact">Phone 773.631.5500 Fax 847.441.4181</h6><h6 class="contact">Email bga@bgimbel.com</h6></div><div><h1 class="agreement">Retainer Agreement</h1></div><div><div class="description"><div><div><p><span class="underline"><span id="firstname">FIRSTNAME</span><span>&nbsp;</span><span id="lastname">LASTNAME</span></span><span>&nbsp;</span>(Client) residing at&nbsp;<span class="underline"><span id="mailingAddress">ADDRESS</span></span>, who is the owner or the authorized agent of the owner of the property below, does hereby retain Barry Gimbel & Associates (BGA), to perform the following services:</p></div><div><ol><li>To obtain all data needed to determine if the proposed 2022 assessment is equitable, and</li><li>If BGA believes the proposed 2022 assessment is not equitable, BGA will prepare and file the necessary valuation complaint forms with the Assessor and/or Board of Review in the appropriate county.</li></ol></div></div><div><div>For services rendered, Client agrees to pay Barry Gimbel & Associates according to the following:</div><div><ol><li>If a reduction is awarded by the Assessor or the Board of Review for the property noted herein, Client agrees to pay to Barry Gimbel & Associates the amount equal to 35% of the first year???s tax savings.</li><li>Savings are determined by multiplying the assessment reduction by the most recent tax rate (the most recent tax rate is the most recent total assessed value divided by the most recent total tax liability).</li><li>Fees are due and payable upon demand.</li></ol></div></div></div><div class="data-input"><div class="left"><div><h1 class="input-title">Subject Property Information</h1></div><div><div class="input-row"><h2 class="input-subtitle">Address:&nbsp;</h2><span class="underline-data data-input-item"><span id="address">ADDRESS 2</span></span></div><div class="input-row"><h2 class="input-subtitle">City, Zipcode:&nbsp;</h2><span class="underline-data data-input-item"><span id="city">CITY</span>&nbsp;<span id="zip">ZIPCODE</span></span></div><div class="input-row"><h2 class="input-subtitle">PIN:&nbsp;</h2><span class="underline-data data-input-item"><span id="pin">pin</span></span></div></div></div><div class="middle"></div><div class="right"><div><h1 class="input-title">Agreed</h1></div><div><div class="input-row"><h2 class="input-subtitle">*Client Signature:&nbsp;</h2><span class="underline-data signature">&nbsp;</span><h2 class="input-subtitle">&nbsp;*Date:&nbsp;</h2><span class="underline-data">&nbsp;</span></div><div class="input-row"><h2 class="input-subtitle">*Primary Phone:&nbsp;</h2><span class="underline-data">&nbsp;</span><h2 class="input-subtitle">&nbsp;*Cell:&nbsp;</h2><span class="underline-data">&nbsp;</span></div><div class="input-row"><h2 class="input-subtitle">*Email:&nbsp;</h2><span class="underline-data">&nbsp;</span></div></div></div></div><div class="required-sentence">All fields marked<span class="required">&nbsp;*&nbsp;</span>are<span class="required-text">&nbsp;Required</span></div></div></div></body></html>
"""

for i, row in enumerate(sh.iter_rows(min_row=1, min_col=1, max_col=16)):
    dict = {
        "pin": "",
        "firstname": "",
        "lastname": "",
        "address": "",
        "city": "",
        "state": "",
        "zipcode": "",
        "mailingAddress": "",
        "mailingCity": "",
        "mailingState": "",
        "mailingZipcode": ""
    }
    for cell in row:
        column = cell.column
        name = ""

        if (cell.value):
            name = cell.value
        else:
            name = ""

        if column == 1:
            dict['pin'] = name
        elif column == 2:
            dict['firstname'] = name
        elif column == 3:
            dict['lastname'] = name
        elif column == 4:
            dict['address'] = name
        elif column == 5:
            dict['city'] = name
        elif column == 6:
            dict['state'] = name
        elif column == 7:
            dict['zipcode'] = name
        elif column == 10:
            dict['mailingAddress'] = name
        elif column == 11:
            dict['mailingCity'] = name
        elif column == 12:
            dict['mailingState'] = name
        elif column == 13:
            dict['mailingZipcode'] = name
        else:
            "You're too young to party"

    formatAddress = dict['address'].replace(" ", "_")
    fileName = "retainer_agreement_{}.html".format(formatAddress)
    Func = open(fileName, "wb")
    newhtml = html
    soup = Soup(newhtml, 'html.parser')

    wrongFirstname = soup.find(id="firstname")
    wrongFirstname.string.replace_with(dict['firstname'])

    wrongLastname = soup.find(id="lastname")
    wrongLastname.string.replace_with(dict['lastname'])

    wrongAddress1 = soup.find(id="mailingAddress")
    if (dict['mailingAddress'] and dict['mailingAddress'] != ""):
        mailingAddress = "{} {} {}, {}".format(
            dict['mailingAddress'], dict['mailingCity'], dict['mailingState'], dict['mailingZipcode'])
        wrongAddress1.string.replace_with(mailingAddress)
    else:
        mailingAddress = "{} {} {}, {}".format(
            dict['address'], dict['city'], dict['state'], dict['zipcode'])
        wrongAddress1.string.replace_with(mailingAddress)

    wrongAddress2 = soup.find(id="address")
    wrongAddress2.string.replace_with(dict['address'])

    wrongCity = soup.find(id="city")
    wrongCity.string.replace_with(dict['city'])

    wrongZip = soup.find(id="zip")
    wrongZip.string.replace_with(dict['zipcode'])

    wrongPin = soup.find(id="pin")
    wrongPin.string.replace_with(dict['pin'])

    Func.write(soup.encode('utf-8'))
    Func.close()

    pdfName = "wheeling_retainer_agreements/retainer_agreement_{}.pdf".format(
        formatAddress)
    pdfkit.from_file(fileName, pdfName)
