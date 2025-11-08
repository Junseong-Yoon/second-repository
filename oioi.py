import pandas as pd

# 예시 데이터 만들기
data = {
    "이름": ["철수", "영희", "민수"],
    "나이": [25, 22, 30],
    "도시": ["서울", "부산", "인천"]
}

df = pd.DataFrame(data)

print(df)
print("\n나이 평균:", df["나이"].mean())

#업로드 연습하는데 오류계속나온다