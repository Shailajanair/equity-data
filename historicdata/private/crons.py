from datetime import datetime

from equity_data.celery import my_project_celery_object
from urllib.request import urlopen, Request
import pandas as pd

from historicdata.models import HistoricData


@my_project_celery_object.task()
def fetch_equity_data():
    if datetime.now().date().today().weekday() > 4:
        return
    date_today = datetime.now().date()
    URL = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ%s_CSV.zip' % date_today.strftime("%d%m%y")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    # open and save the zip file onto computer
    req = Request(url=URL, headers=headers)
    url = urlopen(req)
    output = open('zipFile.zip', 'wb')
    output.write(url.read())
    output.close()

    # read the zip file as a pandas dataframe
    df = pd.read_csv('zipFile.zip')
    print(df.columns)
    create_list = []
    for i in range(len(df)):
        hist_obj = HistoricData.objects.filter(symbol=df.loc[i, "SC_NAME"], created__date=date_today)
        if not hist_obj.exists():
            create_list.append(
                HistoricData(
                    symbol=df.loc[i, "SC_NAME"],
                    scrip_code=df.loc[i, "SC_CODE"],
                    open_price=df.loc[i, "OPEN"],
                    high_price=df.loc[i, "HIGH"],
                    low_price=df.loc[i, "LOW"],
                    close_price=df.loc[i, "CLOSE"]
                )
            )
    if create_list:
        HistoricData.objects.bulk_create(create_list)
    return

fetch_equity_data()