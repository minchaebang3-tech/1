import streamlit as st
import random

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI 여행지 추천 ✈️",
    page_icon="🌷",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #fff7fb 0%, #f8f5ff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #ff78a8;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #8f8290;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .box {
        background: rgba(255,255,255,0.85);
        border-radius: 25px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 8px 25px rgba(180, 130, 170, 0.12);
        border: 1px solid #f4dce9;
    }

    .place {
        color: #ff6699;
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .tag {
        display: inline-block;
        background: #ffe3ee;
        color: #e95f91;
        padding: 6px 12px;
        border-radius: 20px;
        margin: 4px;
        font-size: 14px;
        font-weight: 600;
    }

    .reason {
        color: #625963;
        font-size: 16px;
        line-height: 1.7;
    }

    .footer {
        text-align: center;
        color: #aaa0aa;
        margin-top: 35px;
        font-size: 13px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 18px;
        border: none;
        background: #ff8db5;
        color: white;
        font-size: 18px;
        font-weight: 700;
        padding: 12px;
    }

    div.stButton > button:hover {
        background: #ff6fa3;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# MBTI 여행지 데이터
# -----------------------------
travel_data = {
    "ISTJ": [
        {
            "place": "🇯🇵 교토",
            "tags": ["차분한 여행", "역사", "전통"],
            "reason": "정돈된 분위기와 전통적인 건축물을 천천히 둘러보며 여유롭게 여행하기 좋은 곳이에요.",
            "activity": "⛩️ 사찰 구경 · 🍵 전통 찻집 · 📸 골목 산책"
        },
        {
            "place": "🇨🇭 취리히",
            "tags": ["깔끔함", "자연", "도시"],
            "reason": "질서정연한 도시와 아름다운 자연을 함께 즐길 수 있어요.",
            "activity": "🚋 트램 여행 · 🏞️ 호수 산책 · ☕ 카페"
        }
    ],

    "ISFJ": [
        {
            "place": "🇯🇵 오사카",
            "tags": ["맛집", "편안함", "쇼핑"],
            "reason": "맛있는 음식과 아기자기한 상점들을 편안하게 즐기기 좋은 여행지예요.",
            "activity": "🍜 맛집 탐방 · 🛍️ 쇼핑 · 🎡 관광"
        },
        {
            "place": "🇫🇷 파리",
            "tags": ["감성", "카페", "문화"],
            "reason": "예쁜 거리와 카페를 천천히 구경하며 감성적인 시간을 보내기 좋아요.",
            "activity": "🥐 베이커리 · ☕ 카페 · 🖼️ 미술관"
        }
    ],

    "INFJ": [
        {
            "place": "🇮🇸 아이슬란드",
            "tags": ["자연", "힐링", "고요함"],
            "reason": "웅장한 자연 속에서 조용히 생각하고 힐링하기 좋은 여행지예요.",
            "activity": "🌌 오로라 · 🌊 폭포 · ♨️ 온천"
        },
        {
            "place": "🇳🇿 뉴질랜드",
            "tags": ["자연", "여유", "감성"],
            "reason": "탁 트인 자연과 여유로운 분위기 속에서 자신만의 시간을 보내기 좋아요.",
            "activity": "🏔️ 트레킹 · 🌿 자연 감상 · 📷 사진"
        }
    ],

    "INTJ": [
        {
            "place": "🇸🇬 싱가포르",
            "tags": ["미래도시", "효율", "건축"],
            "reason": "현대적인 도시 구조와 독특한 건축물을 탐험하기 좋은 곳이에요.",
            "activity": "🏙️ 도시 탐험 · 🌿 가든스 바이 더 베이 · 🏛️ 건축 감상"
        },
        {
            "place": "🇩🇪 베를린",
            "tags": ["역사", "문화", "도시"],
            "reason": "역사와 현대 문화가 공존해서 깊이 있게 둘러볼 거리가 많아요.",
            "activity": "🏛️ 박물관 · 🎨 전시 · 🚶 도시 탐방"
        }
    ],

    "ISTP": [
        {
            "place": "🇳🇴 노르웨이",
            "tags": ["자연", "모험", "드라이브"],
            "reason": "멋진 자연을 직접 돌아다니며 자유롭게 여행하기 좋은 곳이에요.",
            "activity": "🚗 드라이브 · 🏔️ 피오르드 · 🥾 트레킹"
        },
        {
            "place": "🇦🇺 호주",
            "tags": ["액티비티", "자유", "바다"],
            "reason": "정해진 일정에 얽매이지 않고 다양한 활동을 즐기기 좋아요.",
            "activity": "🏄 서핑 · 🐨 동물원 · 🌊 해변"
        }
    ],

    "ISFP": [
        {
            "place": "🇮🇹 피렌체",
            "tags": ["예술", "감성", "여유"],
            "reason": "아름다운 건축물과 예술 작품을 감상하며 천천히 여행하기 좋아요.",
            "activity": "🎨 미술관 · 🍝 맛집 · 🌇 노을 감상"
        },
        {
            "place": "🇵🇹 리스본",
            "tags": ["감성", "골목", "노을"],
            "reason": "알록달록한 건물과 골목길을 구경하며 감성적인 여행을 즐길 수 있어요.",
            "activity": "🚋 트램 · 📸 골목 사진 · 🌅 노을"
        }
    ],

    "INFP": [
        {
            "place": "🇨🇦 밴프",
            "tags": ["자연", "힐링", "감성"],
            "reason": "동화 같은 풍경 속에서 조용히 자연을 즐기며 힐링하기 좋은 곳이에요.",
            "activity": "🏔️ 호수 감상 · 🌲 산책 · 📷 사진"
        },
        {
            "place": "🇫🇷 파리",
            "tags": ["낭만", "예술", "감성"],
            "reason": "예술과 아름다운 풍경을 좋아한다면 감성적인 순간을 많이 만들 수 있어요.",
            "activity": "🖼️ 미술관 · ☕ 카페 · 🌆 야경"
        }
    ],

    "INTP": [
        {
            "place": "🇯🇵 도쿄",
            "tags": ["기술", "문화", "탐험"],
            "reason": "최첨단 기술부터 독특한 문화까지 다양한 관심사를 탐구하기 좋아요.",
            "activity": "🤖 기술 전시 · 🎮 게임 · 🏙️ 도시 탐험"
        },
        {
            "place": "🇩🇪 뮌헨",
            "tags": ["과학", "기술", "문화"],
            "reason": "과학과 기술, 역사에 관심이 있다면 볼거리가 풍부한 도시예요.",
            "activity": "🔬 과학관 · 🚗 자동차 박물관 · 🏛️ 역사 탐방"
        }
    ],

    "ESTP": [
        {
            "place": "🇹🇭 방콕",
            "tags": ["활기", "맛집", "모험"],
            "reason": "거리 음식부터 다양한 볼거리까지 에너지 넘치는 여행을 즐기기 좋아요.",
            "activity": "🍜 길거리 음식 · 🛍️ 시장 · 🛺 시내 탐험"
        },
        {
            "place": "🇦🇪 두바이",
            "tags": ["액티비티", "럭셔리", "도시"],
            "reason": "화려한 도시와 다양한 체험을 한 번에 즐길 수 있어요.",
            "activity": "🏜️ 사막 체험 · 🏙️ 전망대 · 🛍️ 쇼핑"
        }
    ],

    "ESFP": [
        {
            "place": "🇺🇸 뉴욕",
            "tags": ["도시", "쇼핑", "문화"],
            "reason": "볼거리와 먹거리가 가득해서 하루 종일 돌아다녀도 지루할 틈이 적어요.",
            "activity": "🗽 관광 · 🛍️ 쇼핑 · 🍕 맛집"
        },
        {
            "place": "🇪🇸 바르셀로나",
            "tags": ["해변", "예술", "활기"],
            "reason": "예쁜 건축물과 맛있는 음식, 바다까지 다채롭게 즐길 수 있어요.",
            "activity": "🏖️ 해변 · 🎨 건축 감상 · 🥘 음식"
        }
    ],

    "ENFP": [
        {
            "place": "🇪🇸 바르셀로나",
            "tags": ["자유", "예술", "활기"],
            "reason": "새로운 것을 구경하고 즉흥적으로 돌아다니는 재미가 큰 도시예요.",
            "activity": "🎨 가우디 건축 · 🏖️ 해변 · 🍴 맛집"
        },
        {
            "place": "🇵🇹 리스본",
            "tags": ["골목", "감성", "탐험"],
            "reason": "골목마다 새로운 풍경을 발견하는 재미가 있어 자유로운 여행과 잘 어울려요.",
            "activity": "🚋 트램 · 📸 골목 탐험 · 🍮 디저트"
        }
    ],

    "ENTP": [
        {
            "place": "🇺🇸 뉴욕",
            "tags": ["변화", "문화", "도시"],
            "reason": "새로운 사람과 문화, 아이디어를 접하며 계속 새로운 것을 발견할 수 있어요.",
            "activity": "🏙️ 도시 탐험 · 🎭 공연 · 🖼️ 전시"
        },
        {
            "place": "🇯🇵 도쿄",
            "tags": ["기술", "문화", "트렌드"],
            "reason": "전통과 최신 문화가 섞여 있어 새로운 것을 탐험하는 재미가 있어요.",
            "activity": "🎮 게임 · 🤖 기술 체험 · 🍣 맛집"
        }
    ],

    "ESTJ": [
        {
            "place": "🇸🇬 싱가포르",
            "tags": ["깔끔함", "도시", "관광"],
            "reason": "효율적으로 다양한 관광지를 돌아보기 좋은 도시예요.",
            "activity": "🏙️ 관광 · 🌿 정원 · 🛍️ 쇼핑"
        },
        {
            "place": "🇨🇭 스위스",
            "tags": ["자연", "정돈", "풍경"],
            "reason": "도시와 자연을 계획적으로 둘러보면서 다양한 경험을 할 수 있어요.",
            "activity": "🚆 기차 여행 · 🏔️ 알프스 · 🌊 호수"
        }
    ],

    "ESFJ": [
        {
            "place": "🇯🇵 오사카",
            "tags": ["맛집", "쇼핑", "친구"],
            "reason": "친구나 가족과 함께 맛있는 음식을 먹으며 즐거운 시간을 보내기 좋아요.",
            "activity": "🍜 맛집 · 🛍️ 쇼핑 · 🎡 관광"
        },
        {
            "place": "🇮🇹 로마",
            "tags": ["역사", "음식", "문화"],
            "reason": "맛있는 음식과 역사적인 명소를 함께 즐길 수 있어 여행 이야기가 풍성해져요.",
            "activity": "🏛️ 유적지 · 🍕 음식 · 📸 관광"
        }
    ],

    "ENFJ": [
        {
            "place": "🇫🇷 파리",
            "tags": ["문화", "예술", "감성"],
            "reason": "사람들과 함께 예술과 문화를 경험하며 특별한 추억을 만들기 좋아요.",
            "activity": "🖼️ 미술관 · ☕ 카페 · 🌆 야경"
        },
        {
            "place": "🇮🇹 로마",
            "tags": ["역사", "문화", "음식"],
            "reason": "다양한 문화와 역사적인 장소를 함께 경험하기 좋은 여행지예요.",
            "activity": "🏛️ 역사 탐방 · 🍝 맛집 · 📷 사진"
        }
    ],

    "ENTJ": [
        {
            "place": "🇦🇪 두바이",
            "tags": ["미래도시", "건축", "도전"],
            "reason": "빠르게 변화하는 도시와 독특한 건축물을 경험하기 좋아요.",
            "activity": "🏙️ 전망대 · 🏜️ 사막 · 🏗️ 건축 감상"
        },
        {
            "place": "🇸🇬 싱가포르",
            "tags": ["도시", "기술", "효율"],
            "reason": "현대적인 도시 시스템과 독특한 건축물을 둘러보기 좋은 곳이에요.",
            "activity": "🏙️ 도시 탐험 · 🌿 미래형 정원 · 🛍️ 쇼핑"
        }
    ]
}


# -----------------------------
# 화면
# -----------------------------
st.markdown(
    '<div class="main-title">✈️ MBTI 여행 처방전 🌷</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">나의 MBTI에 어울리는 여행지를 찾아보자 🧳</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="box">💌 <b>여행을 떠나고 싶은데 어디로 갈지 모르겠다면?</b><br>'
    'MBTI를 골라주면 찰떡같은 여행지를 추천해줄게요!</div>',
    unsafe_allow_html=True
)

st.write("")

mbti_list = list(travel_data.keys())

mbti = st.selectbox(
    "🌸 나의 MBTI를 선택해줘",
    mbti_list
)

st.write("")

if st.button("🎀 여행지 추천받기"):
    recommendations = travel_data[mbti]
    result = random.choice(recommendations)

    st.balloons()

    st.markdown(
        f"""
        <div class="box">
            <div class="place">{result["place"]}</div>

            <div>
                {"".join(
                    f'<span class="tag">{tag}</span>'
                    for tag in result["tags"]
                )}
            </div>

            <br>

            <div class="reason">
                <b>💗 왜 여기냐면?</b><br>
                {result["reason"]}
            </div>

            <br>

            <div class="reason">
                <b>🌷 추천 활동</b><br>
                {result["activity"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="footer">MBTI는 여행지를 정해주는 운명의 공식이 아니라 재미있는 참고용이에요 🐰</div>',
        unsafe_allow_html=True
    )
