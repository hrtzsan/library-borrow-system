# pages/login_page.py
import streamlit as st
import controller

def render_login():

    # ===== Custom CSS =====
    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
        }

        .main {
            background-color: #f5f5f5;
        }

        .center-box {
            text-align: center;
            margin-top: 80px;
        }

        .main-title {
            font-size: 34px;
            font-weight: 600;
            color: #111111;
            margin-bottom: 10px;
        }

        .sub-info {
            font-size: 14px;
            color: #444444;
            line-height: 1.8;
        }

        hr {
            border: 1px solid #d1d5db;
            margin-top: 20px;
            margin-bottom: 30px;
        }

        .stTextInput>div>div>input {
            height: 45px;
        }

        .stButton>button {
            width: 100%;
            height: 45px;
            background-color: #111111;
            color: white;
            font-weight: 600;
            border-radius: 4px;
        }

        .stButton>button:hover {
            background-color: #333333;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # ===== จัดให้อยู่กลาง =====
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("""
            <div class="center-box">
                <div class="main-title">🔒 เข้าสู่ระบบ</div>
                <div class="sub-info">
                    จัดทำโดย : นางสาวสุวพิชชา บัวระพา<br>
                    หมู่เรียน : ว.6706<br>
                    รหัสนักศึกษา : 6740259120
                </div>
            </div>
            <hr>
        """, unsafe_allow_html=True)

        # ===== Login Form =====
        with st.form("login_form"):
            username = st.text_input("ชื่อผู้ใช้", placeholder="เช่น admin")
            password = st.text_input("รหัสผ่าน", type="password", placeholder="เช่น 1234")
            submitted = st.form_submit_button("เข้าสู่ระบบ")

        if submitted:
            ok, msgs, user_info = controller.login(username, password)
            if not ok:
                for m in msgs:
                    st.error(m)
            else:
                for m in msgs:
                    st.success(m)

                st.session_state["is_logged_in"] = True
                st.session_state["user"] = user_info
                st.session_state["page"] = "books"
                st.rerun()