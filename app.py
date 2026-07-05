import streamlit as st
from skin_data import skin_data

st.set_page_config(
    page_title="Skin Care Assistant",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 AI Skin Care Assistant")
st.write("Know your skin better and get personalized skincare recommendations.")

st.markdown("---")

st.header("🧴 How to Identify Your Skin Type")

st.info("""
1. Wash your face with a gentle cleanser.

2. Do NOT apply any skincare products.

3. Wait for 30 minutes.

4. Observe your skin.

• Dry Skin
  - Tight feeling
  - Rough texture
  - Flaky skin

• Oily Skin
  - Shiny face
  - Large pores
  - Greasy feeling

• Combination Skin
  - Oily T-zone
  - Dry cheeks

• Normal Skin
  - Comfortable
  - Balanced

• Sensitive Skin
  - Easily irritated
  - Redness
  - Burning or itching
""")

st.markdown("---")

skin_type = st.selectbox(
    "Select Your Skin Type",
    list(skin_data.keys())
)

concerns = list(skin_data[skin_type].keys())

concern = st.selectbox(
    "Select Your Skin Concern",
    concerns
)

if st.button("Get Recommendation"):

    data = skin_data[skin_type][concern]

    st.success("Recommendation Generated Successfully!")

    st.header("📖 Concern Explanation")
    st.write(data["explanation"])

    st.header("🧪 Recommended Ingredients")

    for item in data["ingredients"]:
        st.write("✅", item)

    st.header("🛍️ Product Types")

    for item in data["products"]:
        st.write("🛒", item)

    st.header("🌞 Morning Routine")

    for step in data["morning"]:
        st.write("☀️", step)

    st.header("🌙 Night Routine")

    for step in data["night"]:
        st.write("🌙", step)

    st.header("💡 Extra Tips")

    for tip in data["tips"]:
        st.write("✔", tip)