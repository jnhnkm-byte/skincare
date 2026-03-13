import streamlit as st

st.set_page_config(page_title="JH 스마트 스킨케어", page_icon="🧴", layout="wide")

st.title("🧴 JH 스마트 스킨케어 추천 시스템")
st.markdown("### 금오공과대학교 경영학과")
st.markdown("**개인별 피부 상태를 분석하고, 전 세계 화장품 중 최적의 제품을 추천합니다.**")
st.markdown("👈 **왼쪽 사이드바**에서 메뉴를 선택하세요.")

st.markdown("---")

cols = st.columns(3)
menus_row1 = [
    ("🌍", "환경·생활 분석", "28개 피부 영향 요인(계절, 온도, 습도, 나이, 생활습관 등) 종합 분석"),
    ("🔬", "피부 진단", "Baumann 16유형 + Fitzpatrick 분류 기반 자가 진단 테스트"),
    ("🦶", "부위별 분석", "12개 신체 부위별 피부 특성과 맞춤 관리법"),
]
for i, (icon, name, desc) in enumerate(menus_row1):
    with cols[i]:
        st.markdown(f"#### {icon} {name}")
        st.markdown(desc)

cols2 = st.columns(3)
menus_row2 = [
    ("💄", "화장품 추천", "진단 + 환경 분석 기반 맞춤 추천, AM/PM 루틴 제안"),
    ("🧪", "성분 사전", "31종 핵심 성분의 효능, 안전 등급, 궁합 체크"),
    ("🎯", "목적별 탐색", "20가지 사용 목적별 제품 탐색 및 목적 조합 추천"),
]
for i, (icon, name, desc) in enumerate(menus_row2):
    with cols2[i]:
        st.markdown(f"#### {icon} {name}")
        st.markdown(desc)

st.markdown("---")

st.markdown("""
##### 🌍 수록 브랜드 (8개국 40+ 브랜드)
**🇰🇷 한국**: 설화수, 이니스프리, 라네즈, COSRX, 닥터지, 닥터자르트, 미샤 등  
**🇯🇵 일본**: SK-II, 시세이도, 하다라보, 비오레, DHC 등  
**🇫🇷 프랑스**: 라로슈포제, 비쉬, 아벤느, 바이오더마, 랑콤, 디올 등  
**🇺🇸 미국**: CeraVe, 디오디너리, 폴라초이스, 에스티로더, 키엘 등  
**🇩🇪 독일**: 유세린, 니베아, 카밀 | **🇬🇧 영국**: 바셀린 | **🇨🇭 스위스**: 웰레다
""")

st.markdown("---")

st.markdown("""
##### 📖 사용 방법
1. **환경·생활 분석** — 계절, 온도, 나이, 생활습관 등 28개 피부 영향 요인 입력
2. **피부 진단** — 간단한 설문으로 나의 Baumann 피부 유형 확인
3. **부위별 분석** — 관심 부위의 피부 특성과 고민 선택
4. **화장품 추천** — 진단 + 환경 분석 종합 맞춤 제품 추천 (AM/PM 루틴 포함)
5. **성분 사전** — 궁금한 성분의 효능과 궁합 확인
6. **목적별 탐색** — 미백, 보습, 안티에이징 등 20가지 목적별 제품 탐색
""")

st.markdown("---")
st.caption("© 2026 JH 스마트 스킨케어 추천 시스템 | 금오공과대학교 경영학과")
