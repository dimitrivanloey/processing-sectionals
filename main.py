import pandas as pd
import numpy as np
import webbrowser
import os
import imgkit

from user_input import VENUE, HOURS_LIST, TITLES_LIST, DATE, FILE
from date_format import date_format

FORMATTED_DATE = date_format(DATE)


for n in range(len(HOURS_LIST)):
    df = pd.read_excel(FILE, sheet_name=HOURS_LIST[n])
    # rounded_df = df.round({'Last 3f (%)': 2})
    type_df = df.astype({'Pos': 'int32'})
    rounded_df = type_df.round({'Pos': 3, 'Last 1/2 mile (%)': 2})
    # df.round({"A":1, "B":2, "C":3, "D":4})
    new_df = rounded_df.replace(np.nan, '', regex=True)
    html_table = new_df.to_html(index=False, classes="horses", border=0)

    TIME = HOURS_LIST[n]
    HH = TIME[0:2]
    MM = TIME[2:4]

    html_string = '''
    <!DOCTYPE html>
<html>
<head>
<title>Post Race Reports</title>
<style>
</style>
<link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>
   <div class="all">
       <div class="header1">
           <div class="race-logo"><img src="logos/{venue}.png" alt="{venue} Logo" style="width:180px;height:80px;">
           </div>
           <div class="title-date-container">
               <h2>{title}</h2>
               <h3>{date}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: {hh}:{mm}</h3>
           </div>
           <div class="racingTV-logo"><img src="racingTV.png" alt="Racing TV logo"
               style="width:300px;height:81px;">
           </div>
       </div>
    {table}
   </div>
   <div class="lower-banner">
       <div class="times-accuracy">
           <p>Times accurate to +/- 0.2s or more excluding the location accuracy +/-0.5m (approximately 0.03s).
               </br>One horse length is run in approximately 0.167 seconds on good or firmer ground, 0.18 seconds on
               good to soft ground and 0.2 seconds or more on soft.</p>
       </div>
       <div class="email" style="text-align:right;"><a href="mailto:sectionals@racingtv.com">For enquiries, please contact sectionals@racingtv.com</a>
       </div>
   </div>
</div>
</body>
</html>
    '''

    with open(f'{VENUE}_{HOURS_LIST[n]}.html', 'w') as website_file:
        website_file.write(
            html_string.format(table=new_df.to_html(index=False, classes="horses", border=0), title=TITLES_LIST[n],
                               date=FORMATTED_DATE, time=TIME, venue=VENUE, hh=HH, mm=MM))

    filename = 'file:///' + os.getcwd() + '/' + f'{VENUE}_{HOURS_LIST[n]}.html'
    webbrowser.open_new_tab(filename)



# imgkit.from_file('perth_1342.html', 'out.jpg')