# https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR201224.zip
# https://nsearchives.nseindia.com/archives/sme/bhavcopy/sme201224.csv

from datetime import datetime, timedelta
import os, requests

start_date = datetime(2024, 4, 12)  # Format: YYYY, MM, DD
end_date = datetime(2024, 12, 20)
delta = end_date - start_date

folder = "bhavcopy_data"
os.makedirs(folder, exist_ok=True)

for i in range(delta.days + 1):
    date = start_date + timedelta(days=i)
    formatted_date = date.strftime('%d%m%y')  # Changed to %y for 2-digit year
    url = f'https://nsearchives.nseindia.com/archives/sme/bhavcopy/sme{formatted_date}.csv'
    print(f"Attempting to download data for: {date.strftime('%d-%m-%y')}")
    
    try:
        response = requests.get(url,stream=True)
        if response.status_code == 200:
            file_path = os.path.join(folder, f'sme_bhavcopy_{formatted_date}.csv')
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded data for {formatted_date}")
        else:
            print(f"Failed to download data for {formatted_date}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading data for {formatted_date}: {str(e)}")