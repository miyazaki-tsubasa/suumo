#必要なライブラリをインポート
import pandas as pd
import streamlit as st
import numpy as np


st.title('お得な物件を簡単検索!!')

st.text('下記の要素から条件を絞って、物件を抽出しましょう')
st.text('"予測値との差"の値が小さいほど、家賃の相場よりも安いということになります。')

st.header('操作説明')
st.text('1. "最低築年数"の値を決める。"最高築年数"の値を決める。')
st.text('2. 希望の"間取り"を選択')
st.text('3. "区""、"市町村"を選択する')


#st.subheader('This is a subheader')
#st.text('Hello World!,this is text')

# st.write()はMarkdown表記対応
#st.write('# headline1')
# 以下のように明示的に書くことも可能
#st.markdown('## headline2')

#st.write('# 全体の流れ')
st.text('↓ 東京新宿区の全ての物件')

#DF読み込み
df = pd.read_csv('new_df_search.csv')

df = df.drop(['間取り'],axis=1)

#Streamlitのマジックコマンドst.write()を使用して物件情報を表示
st.write(df)

#物件の絞り込み機能の追加:
#Streamlitのウィジェットを使用して、家賃、間取り、専有面積などの絞り込み条件を指定できるようにする。

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

# 選択された区,市町村をリストとして扱う
# isin()を使う際にリストである必要がある。
selected_wards = [selected_wards] if isinstance(selected_wards, str) else selected_wards
selected_cities = [selected_cities] if isinstance(selected_cities, str) else selected_cities


# 絞り込み条件に基づいて物件をフィルタリング
#、市町村の選択肢に「すべて選択」が追加され、選択された市町村に基づいて物件を絞り込む処理が行われる。
# また、選択された市町村が「すべて選択」の場合は、市町村の絞り込み条件を無視して区の条件のみを適用
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

#st.write('## 物件を出力!!')

st.text('並び順は予測値との差になってます。')
# 絞り込んだ物件情報の表示
st.write(filtered_df.sort_values(by='予測値との差',ascending=True))

st.text('※下記は、今回の物件とは関係ありません。')
st.text('緯度、経度を入力して結び付ければ、下記のように表示できる。')
#マップをプロット
df_map = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)

# データフレームに緯度と経度の列名を修正
#df_map = df_map.rename(columns={'lat': 'latitude', 'lon': 'longitude'})


st.map(df_map)

st.header('今後の改良点')
st.text('1. 全体的なデザイン')
st.text('2. 列の並び替え')
st.text('3. 間取りも複数選択可にする')
st.text('4. 出力された物件情報がもっと直感的にわかりやすいものにしたい')
st.text('5. 列がonehot-encodingのままなので、整理したい')
st.text('6. 地図の情報、マッピング情報を入れたい')
st.text('7.')
st.text('')

