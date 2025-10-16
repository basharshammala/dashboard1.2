import streamlit as st
import time
from main import analysis_page
st.set_page_config(
    layout="wide"
)
st.markdown("""
<style>
body, [data-testid="stMarkdownContainer"] {
    direction: rtl;
    text-align: right;
    font-family: "Cairo", "Tahoma", sans-serif;
}
</style>
""", unsafe_allow_html=True)
def stream_ar_text(text: str, delay: float = 0.02):
    # يرجّع كلمة كلمة مع تأخير بسيط
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)
def customers () :
    st.write('the customer')
def about ():
    text = """
    قطفه هي أداة تحليلات متقدمة على منصة زد، تمكّن أصحاب المتاجر من الحصول على رؤى شاملة حول أداء مبيعاتهم وسلوك عملائهم من خلال تحليل دقيق ومفصل للبيانات. توفر قطفة تحليلات مالية، وبيانات حول 
    استخدام القسائم الشرائية، وأداء المنتجات، مما يساعد على اتخاذ قرارات تسويقية فعّالة. الأداة تم تصميمها خصيصًا لتحسين استراتيجية المبيعات وزيادة الأرباح عبر عرض معلومات حيوية وقابلة للتنفيذ.
    """.strip()
    st.header('تعرف على تطبيق قطفه')
    st.write_stream(stream_ar_text(text, delay=0.02))
    st.markdown("""
     <p style='text-align: right; font-weight: bold; margin-top: 30px;'>
     م. بشار أبو شماله
     </p>
     """, unsafe_allow_html=True)

def services () :
    st.write('services')
def price ():
    st.write('price')


right_col, middel_col, left_col = st.columns([1,3,1])
with left_col :
    if st.button('جرب الان ⬅️') :
        st.switch_page(analysis_page)

with right_col :
    st.image(r"image/logo5.png")




with middel_col  :
    st.markdown("""
    <style>
    /* نخلي شريط التبويبات بالنص */
    div[data-baseweb="tab-list"] {
        justify-content: center !important;
    }

    /* نخلي العناوين نفسها فيها مسافة مريحة */
    button[data-baseweb="tab"] {
        margin: 0 25px !important;       /* مسافة يمين ويسار بين التبويبات */
        font-weight: 600 !important;     /* خط عريض شوي */
        font-size: 18px !important;      /* حجم أكبر شوي لو بدك */
    }
    </style>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4 =  st.tabs(["خدماتنا", "عملاؤنا", "نبذة", "الأسعار"], default="نبذة")
    with col1 :
        price()
    with col2 :
        services()
    with col3 :
        about()
    with col4 :
        customers()



