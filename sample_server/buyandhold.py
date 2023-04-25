import numpy as np
from datetime import datetime
import pandas as pd

def bnh(df, col = 'Close', start = '20000101', end = '20200101'):
    # 문자열타입을 시계열타입으로 바꾸기
    df.index = pd.to_datetime(df.index)
    start = datetime.strptime(start, '%Y%m%d')
    end = datetime.strptime(end,'%Y%m%d')
    df = df.loc[start : end]
    # 결측치와 무한대를 삭제
    df = df.loc[~df.isin([np.nan, np.inf, -np.inf]).any(axis= 'columns')]
    # 수정종가만 있는 데이터 프레임으로 변경
    df = df[[col]]
    # 일변 수익율 변수 생성
    df['daily_rtn'] = df[col].pct_change()
    # 누적 수익율 변수 생성
    df['st_rtn'] = (1 + df['daily_rtn']).cumprod()
    # 데이터프레임을 리턴
    return df