#必要なライブラリをインポート
import pandas as pd
import streamlit as st

#DF読み込み
df = pd.read_csv('new_df_search.csv')

#Streamlitのマジックコマンドst.write()を使用して物件情報を表示
st.write(df)

#物件の絞り込み機能の追加:
#Streamlitのウィジェットを使用して、家賃、間取り、専有面積などの絞り込み条件を指定できるようにする。

# 家賃の範囲を指定するスライダー
min_age = st.slider('最低築年数', min_value=0, max_value=df['築年数'].max(), step=1)
max_age = st.slider('最高築年数', min_value=0, max_value=df['築年数'].max(), step=1)

# 間取りの選択肢
room_types = ['DK', 'K', 'L', 'S']
selected_room_type = st.selectbox('間取り', room_types)

# 区の選択肢
wards = df['区'].unique()
selected_ward = st.selectbox('区', wards)

# 絞り込み条件に基づいて物件をフィルタリング
filtered_df = df[
    (df['築年数'] >= min_age) & (df['築年数'] <= max_age) &
    (df['間取りDK'] == (selected_room_type == 'DK')) &
    (df['間取りK'] == (selected_room_type == 'K')) &
    (df['間取りL'] == (selected_room_type == 'L')) &
    (df['間取りS'] == (selected_room_type == 'S')) &
    (df['区'] == selected_ward)
]

# 絞り込んだ物件情報の表示
st.write(filtered_df)
