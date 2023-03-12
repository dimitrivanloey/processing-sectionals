from PIL import Image
import requests
from datetime import datetime

HOUR_LIST = ['1315', '1350', '1425', '1500', '1535', '1610', '1645']
VENUE = 'sandown-park'
DATE = '20230311'


url = 'https://www.racingtv.com/api/sectional'
headers = {"API-KEY": "01511c49-22ae-45ca-8f86-c2d0a8eafb53"}

# ADJUSTED_HOUR_LIST = []

# # Adjusting the hours winter/summer time
# for n in range(len(HOURS_LIST)):
#     if datetime.now() == datetime.utcnow():
#         adjusted_hour = int(HOURS_LIST[n])
#         ADJUSTED_HOUR_LIST.append(adjusted_hour)
#     else:
#         adjusted_hour = int(HOURS_LIST[n]) - 100
#         ADJUSTED_HOUR_LIST.append(adjusted_hour)

# print(ADJUSTED_HOUR_LIST)

# Creating PDFs
for n in range(len(HOUR_LIST)):
    image1 = Image.open(fr'{VENUE}_{DATE}_{HOUR_LIST[n]}.png')
    im1 = image1.convert('RGB')
    im1.save(f'{VENUE}_{DATE}_{HOUR_LIST[n]}.pdf')

# Sending to the RacingTV API
for n in range(len(HOUR_LIST)):
    my_file = open(f"{VENUE}_{DATE}_{HOUR_LIST[n]}.pdf", "rb")

    test_response = requests.post(url, headers=headers, files={"sectional_document[pdf]": my_file})

    if test_response.ok:
        print(f"Upload completed successfully! for {VENUE}_{DATE}_{HOUR_LIST[n]}.pdf")
        print(test_response.status_code)
    else:
        print(f"Something went wrong! for {VENUE}_{DATE}_{HOUR_LIST[n]}.pdf")
        print(test_response.status_code)