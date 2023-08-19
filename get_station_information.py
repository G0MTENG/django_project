import pandas as pd
df = pd.read_csv('station_arrive_information_csv.csv', encoding='cp949', index_col=False)


#출발역 도착역 입력
st_nm = input("출발역 입력 : ")
ar_nm = input("도착역 입력 : ") 


#'역' 글자 입력 제외하고 검색
st_nm_with_station = st_nm.rstrip('역')
ar_nm_with_station = ar_nm.rstrip('역')

st_result = df[df['STATN_NM'] == st_nm_with_station]
ar_result = df[df['STATN_NM'] == ar_nm_with_station]

#데이터 둘중에 하나라도 없으면 false 출력
if st_result.empty or ar_result.empty:
    print("false")
else:
    print("역정보있음")