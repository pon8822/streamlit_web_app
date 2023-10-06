import streamlit as st
from PIL import Image
import pandas as pd

# データ分析関連
df = pd.read_csv('./data/test.csv', index_col='Id')
st.dataframe(df)
st.line_chart(df['LotArea'])
