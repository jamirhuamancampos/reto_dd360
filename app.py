#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests.exceptions import SSLError
import os
from datetime import timedelta
from io import BytesIO
import pandas as pd
import requests
import gzip
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pd.options.mode.chained_assignment = None

def send_request():
    try:
        url = "https://smn.conagua.gob.mx/webservices/index.php?method=1"
        verify = False
        headers = {'Content-Encoding': 'gzip', 'Content-Type': 'x-application/x-gzip'}
        r = requests.get(url=url, headers=headers, verify=verify, stream=True)
        f = BytesIO()
        f.write(r.raw.read())
        f.seek(0)
        return f
    except SSLError as e:
        print(e)
    except IOError as e:
        print(e)


def get_dataframe():
    response = send_request()
    df = pd.read_json(response,  compression='gzip')
    df['dloc'] = df['dloc'].astype(str)
    df['tmax'] = df['tmax'].astype(float)
    df['tmin'] = df['tmin'].astype(float)
    df['day'] = pd.to_datetime(df['dloc'].str[:8], format='%Y%m%d')
    return df


def df_to_csv():
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y_%H")
    file_name = "data/{}.csv".format(dt_string)
    df = get_dataframe()
    df.to_csv(file_name, index=False, mode='w', encoding='utf-8')


def get_dataframe_last_two_hours():
    before_now = datetime.now() - timedelta(hours=1)
    before_dt_string = before_now.strftime("%d%m%Y_%H")
    before_file_name = "data/{}.csv".format(before_dt_string)
    file_exists = os.path.exists(before_file_name)
    df_ = get_dataframe()
    if file_exists:
        df_before = pd.read_csv(before_file_name, sep=',', encoding="utf-8")
        union = pd.concat([df_, df_before], ignore_index=True)
    else:
        union = df
    return union


def get_dataframe_average():
    df_ = get_dataframe_last_two_hours()
    df_avg = df_[['ides', 'idmun', 'nes', 'nmun', 'tmax', 'tmin']]
    df_avg[['tmax']] = df_avg[['tmax']].astype(float)
    df_avg[['tmin']] = df_avg[['tmin']].astype(float)
    mean_df = df_avg.groupby(['ides', 'idmun', 'nes', 'nmun']).mean()
    mean_df = mean_df.reset_index()
    return mean_df


def create_directory(path):
    path_script = os.path.dirname(os.path.abspath(__file__))
    print(path_script)
    isExist = os.path.exists(path_script + '/' + path)
    if not isExist:
        os.makedirs(path_script + '/' + path)
        print("The new directory is created!")


def df_to_csv_average_last_two_hours():
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y_%H")
    file_name = "avg/{}.csv".format(dt_string)
    df = get_dataframe_average()
    df.to_csv(file_name, index=False, mode='w', encoding='utf-8')


if __name__ == '__main__':
    create_directory('data')
    create_directory('avg')
    df = get_dataframe()
    print(df)
    df_to_csv()
    df = get_dataframe_last_two_hours()
    print(df)
    df = get_dataframe_average()
    print(df)
    df_to_csv_average_last_two_hours()



