import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="함수 학습지", page_icon="📘")

st.markdown(
    """
    <style>
      body, .stApp {
        background-color: #fff9c4;
        color: #000000;
      }
      .stApp .css-1d391kg, .stApp .css-1v0mbdj {
        background-color: #fff9c4;
      }
      .stButton>button, .stSlider>div, .stTextArea>div, .stSlider label, .stSlider div label {
        color: #000000;
      }
      .stMetric, .stMetric * {
        color: #000000 !important;
      }
      .stMarkdown, .stText, .stCaption {
        color: #000000;
      }
      .card {
        background: #fff9c4;
        border: 2px solid #fdd835;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 16px;
      }
      .card-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 8px;
      }
      .small-box {
        background: #fffde7;
        border: 1px solid #fbc02d;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
      }
      .match-box {
        background: #ffffff;
        border: 2px dashed #fdd835;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
      }
      .type-card {
        display: inline-block;
        width: auto;
        min-width: 90px;
        padding: 14px;
        margin-bottom: 16px;
      }
      .float-card {
        display: inline-block;
        background: #fff9c4;
        border: 2px solid #fdd835;
        border-radius: 20px;
        padding: 18px;
        margin: 12px;
        box-shadow: 0 12px 25px rgba(0, 0, 0, 0.08);
        transform: translateY(-4px);
      }
      .float-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 16px;
        margin-bottom: 20px;
      }
      .compare-table {
        width: 100%;
        border-collapse: collapse;
      }
      .compare-table th, .compare-table td {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
        padding: 10px 12px;
        text-align: left;
      }
      .compare-table th {
        background: rgba(255, 255, 255, 0.6);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📘 함수 학습지")
st.write("함수는 실생활에서 입력과 출력이 연결되는 관계예요. 아래에서 직접 보고 눌러보며 배워보세요!")

st.header("1. 실생활 함수 예시")
st.markdown(
    """
<div class='card'>
  <div class='card-title'>🌡 온도 조절기</div>
  <div class='small-box'>입력: 설정 온도 20°C → 출력: 방 온도 20°C</div>
</div>
<div class='card'>
  <div class='card-title'>🥤 자판기</div>
  <div class='small-box'>입력: 콜라 선택 → 출력: 1000원</div>
</div>
<div class='card'>
  <div class='card-title'>🍎 사과 가격</div>
  <div class='small-box'>입력: 3개 선택 → 출력: 1500원</div>
</div>
""",
    unsafe_allow_html=True,
)
st.caption("같은 입력에는 같은 출력이 나와야 하는 것이 함수의 특징이에요. 🔁")
count = st.slider("사과 개수 선택", min_value=1, max_value=10, value=1)
unit_price = 500
price = count * unit_price
col1, col2 = st.columns(2)
col1.metric(label="사과 개수", value=f"{count}개")
col2.metric(label="총 금액", value=f"{price}원")
st.markdown("**입력**: 사과 개수 → **출력**: 총 금액")

st.header("2. 수학에서의 함수 정의")
st.markdown(
    """
- 함수란 두 집합 x, y에 대하여 x의 각 원소에 y의 원소가 하나씩만 대응할 때,
  이 대응을 x에서 y로의 함수라 하고 기호로 f: x->y와 같이 나타낸다.
- 정의역 X의 각 원소에 공역 Y의 원소가 오직 하나씩만 대응하는 관계

<div class='small-box'>f: X → Y</div>
""",
    unsafe_allow_html=True,
)

st.header("3. 정의역, 공역, 치역")
col1, col2, col3 = st.columns(3)
col1.markdown(
    """
<div class='type-card'>
  <div class='card-title'>정의역 X</div>
</div>
""",
    unsafe_allow_html=True,
)
col2.markdown(
    """
<div class='type-card'>
  <div class='card-title'>공역 Y</div>
</div>
""",
    unsafe_allow_html=True,
)
col3.markdown(
    """
<div class='type-card'>
  <div class='card-title'>치역</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("---")
st.header("4. 함수 구분해보기")

x1 = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
fig1, ax1 = plt.subplots(figsize=(3, 3))
ax1.plot(x1, y1, marker='o', color='#ff8f00')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_xticks([1, 2, 3, 4])
ax1.set_yticks([2, 4, 6, 8])
ax1.grid(True, linestyle='--', alpha=0.5)

x2 = [1, 1, 2, 3]
y2 = [2, 4, 4, 6]
fig2, ax2 = plt.subplots(figsize=(3, 3))
ax2.scatter([1, 1, 2, 3], [2, 4, 4, 6], color='#d32f2f', s=60)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xticks([1, 2, 3])
ax2.set_yticks([2, 4, 6])
ax2.grid(True, linestyle='--', alpha=0.5)

col1, col2 = st.columns(2)
col1.pyplot(fig1)
col2.pyplot(fig2)

st.markdown("---")
st.header("5. 여러 가지 함수")
st.markdown(
    """
<div class='float-row'>
  <div class='float-card'>
    <div class='card-title'>일대일 함수</div>
    <div class='small-box'>서로 다른 x는 서로 다른 y로 대응</div>
  </div>
  <div class='float-card'>
    <div class='card-title'>일대일 대응</div>
    <div class='small-box'>각 x 원소가 정확히 하나의 y 원소에 대응</div>
  </div>
  <div class='float-card'>
    <div class='card-title'>항등함수</div>
    <div class='small-box'>f(x)=x인 함수</div>
  </div>
  <div class='float-card'>
    <div class='card-title'>상수함수</div>
    <div class='small-box'>모든 x에 대해 같은 값이 나오는 함수</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("### 일대일 함수 vs 일대일 대응")
st.markdown(
    """
<div style='border-top: 1px solid rgba(0,0,0,0.12); padding-top: 12px;'>
<table class='compare-table'>
  <tr>
    <th>구분</th>
    <th>일대일 대응</th>
    <th>일대일 함수</th>
  </tr>
  <tr>
    <td>대응 관계</td>
    <td>x의 각 원소가 y의 원소와 한 번씩 대응</td>
    <td>서로 다른 x는 서로 다른 y로 대응</td>
  </tr>
  <tr>
    <td>공역 관계</td>
    <td>y의 모든 원소까지 대응될 수 있음</td>
    <td>반드시 전사일 필요는 없음</td>
  </tr>
  <tr>
    <td>다른 이름</td>
    <td>전단사 대응</td>
    <td>단사 함수</td>
  </tr>
</table>
</div>
""",
    unsafe_allow_html=True,
)

x_id = [0, 1, 2, 3, 4]
y_id = [0, 1, 2, 3, 4]
fig_id, ax_id = plt.subplots(figsize=(3, 3))
ax_id.plot(x_id, y_id, marker='o', color='#388e3c')
ax_id.set_xlabel('x')
ax_id.set_ylabel('y')
ax_id.set_xticks([0, 1, 2, 3, 4])
ax_id.set_yticks([0, 1, 2, 3, 4])
ax_id.grid(True, linestyle='--', alpha=0.5)

x_const = [0, 1, 2, 3, 4]
y_const = [3, 3, 3, 3, 3]
fig_const, ax_const = plt.subplots(figsize=(3, 3))
ax_const.plot(x_const, y_const, marker='o', color='#1976d2')
ax_const.set_xlabel('x')
ax_const.set_ylabel('y')
ax_const.set_xticks([0, 1, 2, 3, 4])
ax_const.set_yticks([1, 2, 3, 4])
ax_const.grid(True, linestyle='--', alpha=0.5)

col1, col2 = st.columns(2)
col1.pyplot(fig_id)
col2.pyplot(fig_const)
