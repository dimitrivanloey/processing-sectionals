from PIL import Image
import requests

from user_input import HOURS_LIST, VENUE, DATE


url = 'https://www.racingtv.com/api/sectional'
headers = {"API-KEY": "01511c49-22ae-45ca-8f86-c2d0a8eafb53"}

ADJUSTED_HOUR_LIST = []

# Adjusting the hours winter/summer time
for n in range(len(HOURS_LIST)):
    adjusted_hour = int(HOURS_LIST[n])
    ADJUSTED_HOUR_LIST.append(adjusted_hour)

# Creating PDFs
for n in range(len(HOURS_LIST)):
    image1 = Image.open(fr'{VENUE}_{DATE}_{HOURS_LIST[n]}.png')
    im1 = image1.convert('RGB')
    im1.save(f'{VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf')

# Sending to the RacingTV API
for n in range(len(HOURS_LIST)):
    my_file = open(f"{VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf", "rb")

    test_response = requests.post(url, headers=headers, files={"sectional_document[pdf]": my_file})

    if test_response.ok:
        print(f"Upload completed successfully! for {VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf")
        print(test_response.text)
    else:
        print(f"Something went wrong! for {VENUE}_{DATE}_{ADJUSTED_HOUR_LIST[n]}.pdf")
        print(test_response.text)