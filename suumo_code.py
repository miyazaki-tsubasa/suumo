#必要なライブラリをインポート
import pandas as pd
import streamlit as st

#DF読み込み
df = pd.read_csv('new_df_search.csv')

#Streamlitのマジックコマンドst.write()を使用して物件情報を表示
st.write(df)

#物件の絞り込み機能の追加:
#Streamlitのウィジェットを使用して、家賃、間取り、専有面積などの絞り込み条件を指定できるようにする。

#実行結果をstreamlitで確認する方法
#区じゃなくて、市町村もいれる
#絞った結果を新たにDFとして表示させるようにする。

# 家賃の範囲を指定するスライダー
min_age = st.slider('最低築年数', min_value=0, max_value=int(df['築年数'].max()), step=1)
max_age = st.slider('最高築年数', min_value=0, max_value=int(df['築年数'].max()), step=1)

# 間取りの選択肢
room_types = ['DK', 'K', 'L', 'S']
selected_room_type = st.selectbox('間取り', room_types)

# 区の選択肢
wards = df['区'].unique()
selected_wards = st.selectbox('区', wards)

# 市町村の選択肢
cities = ['すべて選択'] + df['市町村'].unique().tolist()
selected_cities = st.multiselect('市町村', cities)

# 選択された区をリストとして扱う
selected_wards = [selected_wards] if isinstance(selected_wards, str) else selected_wards

# 選択された市町村をリストとして扱う
selected_cities = [selected_cities] if isinstance(selected_cities, str) else selected_cities


# 絞り込み条件に基づいて物件をフィルタリング
if 'すべて選択' in selected_cities:
    filtered_df = df[
        (df['築年数'] >= min_age) & (df['築年数'] <= max_age) &
        (df['間取りDK'] == (selected_room_type == 'DK')) &
        (df['間取りK'] == (selected_room_type == 'K')) &
        (df['間取りL'] == (selected_room_type == 'L')) &
        (df['間取りS'] == (selected_room_type == 'S')) &
        (df['区'].isin(selected_wards))
    ]
else:
    filtered_df = df[
        (df['築年数'] >= min_age) & (df['築年数'] <= max_age) &
        (df['間取りDK'] == (selected_room_type == 'DK')) &
        (df['間取りK'] == (selected_room_type == 'K')) &
        (df['間取りL'] == (selected_room_type == 'L')) &
        (df['間取りS'] == (selected_room_type == 'S')) &
        (df['区'].isin(selected_wards)) &
        (df['市町村'].isin(selected_cities))
    ]

# 絞り込んだ物件情報の表示
st.write(filtered_df.sort_values(by='予測値との差',ascending=True))
