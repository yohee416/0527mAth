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
      .stButton>button {
        color: #ffffff !important;
        background-color: #333333 !important;
        border: 1px solid #000000 !important;
      }
      .stButton>button:hover {
        background-color: #555555 !important;
      }
      .stSlider>div, .stTextArea>div, .stSlider label, .stSlider div label {
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
      @keyframes floaty {
        0% { transform: translateY(0px); }
        25% { transform: translateY(-8px); }
        50% { transform: translateY(-12px); }
        75% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📘 함수 학습지")
st.write("함수는 실생활에서 입력과 출력이 연결되는 관계예요. 아래에서 직접 눌러봅시다!")

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

st.markdown("<div style='height:160px'></div>", unsafe_allow_html=True)

st.header("3. 정의역, 공역, 치역")
col1, col2, col3 = st.columns(3)
col1.markdown(
    """
<div class='float-card'>
  <div class='card-title'>정의역 X</div>
</div>
""",
    unsafe_allow_html=True,
)
col2.markdown(
    """
<div class='float-card'>
  <div class='card-title'>공역 Y</div>
</div>
""",
    unsafe_allow_html=True,
)
col3.markdown(
    """
<div class='float-card'>
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
    <th>일대일 함수</th>
    <th>일대일 대응</th>
  </tr>
  <tr>
    <td>수학적 정의</td>
    <td>x1 ≠ x2이면 f(x1) ≠ f(x2)이다.</td>
    <td>일대일 함수이면서 치역이 공역과 같다.</td>
  </tr>
  <tr>
    <td>대응 관계</td>
    <td>정의역의 서로 다른 원소는 공역의 서로 다른 원소에 대응함.</td>
    <td>서로 다른 원소끼리 짝을 지으면서, 공역에 남는 원소가 없음.</td>
  </tr>
  <tr>
    <td>공역과 치역</td>
    <td>공역에 화살표를 받지 못한 빈 원소(방)가 있어도 됨.</td>
    <td>공역의 모든 원소가 화살표를 받아 공역과 치역이 일치함.</td>
  </tr>
  <tr>
    <td>특징/조건</td>
    <td>그래프가 항상 증가하거나 항상 감소함.</td>
    <td>역함수가 존재할 조건이 됨.</td>
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
ax_id.set_title('항등함수', fontweight='bold')
ax_id.set_xlabel('x')
ax_id.set_ylabel('y')
ax_id.set_xticks([0, 1, 2, 3, 4])
ax_id.set_yticks([0, 1, 2, 3, 4])
ax_id.grid(True, linestyle='--', alpha=0.5)

x_const = [0, 1, 2, 3, 4]
y_const = [3, 3, 3, 3, 3]
fig_const, ax_const = plt.subplots(figsize=(3, 3))
ax_const.plot(x_const, y_const, marker='o', color='#1976d2')
ax_const.set_title('상수함수', fontweight='bold')
ax_const.set_xlabel('x')
ax_const.set_ylabel('y')
ax_const.set_xticks([0, 1, 2, 3, 4])
ax_const.set_yticks([1, 2, 3, 4])
ax_const.grid(True, linestyle='--', alpha=0.5)

col1, col2 = st.columns(2)
col1.pyplot(fig_id)
col2.pyplot(fig_const)

st.markdown("---")
st.header("5-1. 여러가지 함수")

if 'function_mode' not in st.session_state:
    st.session_state.function_mode = 'constant'
if 'selected_domain' not in st.session_state:
    st.session_state.selected_domain = None

mode_cols = st.columns(4)
if mode_cols[0].button("일대일 함수 모드", key='mode_injective'):
    st.session_state.function_mode = 'injective'
    st.session_state.selected_domain = None
if mode_cols[1].button("일대일 대응 모드", key='mode_bijection'):
    st.session_state.function_mode = 'bijection'
    st.session_state.selected_domain = None
if mode_cols[2].button("상수함수 모드", key='mode_constant'):
    st.session_state.function_mode = 'constant'
    st.session_state.selected_domain = None
if mode_cols[3].button("항등함수 모드", key='mode_identity'):
    st.session_state.function_mode = 'identity'
    st.session_state.selected_domain = None

mode_label = {
    'constant': '상수함수',
    'identity': '항등함수',
    'injective': '일대일 함수',
    'bijection': '일대일 대응',
}[st.session_state.function_mode]
st.markdown(f"**현재 모드:** {mode_label}")
st.markdown("왼쪽의 정의역 X 버튼을 누르면, 오른쪽 공역 Y가 바로 색칠됩니다.")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("**정의역 X**")
    left_cols = st.columns(3)
    for i, c in enumerate(left_cols, start=1):
        if c.button(str(i), key=f"x_{i}"):
            st.session_state.selected_domain = str(i)

with col_right:
    st.markdown("**공역 Y**")
    if st.session_state.function_mode == 'constant':
        labels = ['1', '2', '3']
    elif st.session_state.function_mode == 'identity':
        labels = ['1', '2', '3']
    elif st.session_state.function_mode == 'injective':
        labels = ['1', '2', '3', '4']
    else:
        labels = ['5', '6', '7']

    for label in labels:
        if st.session_state.selected_domain is not None:
            if st.session_state.function_mode == 'constant':
                highlight = (label == '1')
            elif st.session_state.function_mode == 'identity':
                highlight = (label == st.session_state.selected_domain)
            elif st.session_state.function_mode == 'injective':
                mapping = {'1': '1', '2': '2', '3': '3'}
                highlight = (label == mapping[st.session_state.selected_domain])
            else:
              mapping = {'1': '7', '2': '5', '3': '6'}
              highlight = (label == mapping[st.session_state.selected_domain])
        else:
            highlight = False
        color = '#fff59d' if highlight else '#ffffff'
        st.markdown(
            f"<div style='border:2px solid #d6b500; border-radius:12px; background:{color}; padding:16px; margin:6px 0; text-align:center; font-weight:700;'>{label}</div>",
            unsafe_allow_html=True,
        )

if st.button("초기화", key='reset'):
    st.session_state.selected_domain = None

if st.session_state.selected_domain is None:
    st.info("정의역 숫자를 누르면 공역이 색칠됩니다.")
