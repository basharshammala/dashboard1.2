import streamlit as st
import time

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
    """
    st.header('تعرف على تطبيق قطفه')
    # text = "قطفه هي أداة تحليلات متقدمة على منصة زد، تمكّن أصحاب المتاجر من الحصول على رؤى شاملة حول أداء مبيعاتهم وسلوك عملائهم من خلال تحليل دقيق ومفصل للبيانات. توفر قطفة تحليلات مالية، وبيانات حول استخدام القسائم الشرائية، وأداء المنتجات، مما يساعد على اتخاذ قرارات تسويقية فعّالة. الأداة تم تصميمها خصيصًا لتحسين استراتيجية المبيعات وزيادة الأرباح عبر عرض معلومات حيوية وقابلة للتنفيذ."
    # for word in text.split(" "):
    #     yield word + " "
    #     time.sleep(0.05)
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

page_customer = st.Page(customers, title='عملاؤنا')
page_about = st.Page(about, title='نبذة عنا')
page_services = st.Page(services, title='خدماتنا')
page_price = st.Page(price, title='الأسعار')

right_col, middel_col, left_col = st.columns([1,3,1])
with left_col :
    st.button('تسجيل الدخول ⬅️')

with right_col :
    st.image(r"image/logo4.png")
    # st.logo(r"C:\Users\HKH\Downloads\WhatsApp_Image_2025-10-13_at_8.25.26_PM-removebg-preview.png", size = 'large')

with middel_col  :
    col1, col2, col3, col4 =  st.columns(4)
    with col1 :
        st.page_link(page_price)
    with col2 :
        st.page_link(page_services)
    with col3 :
        st.page_link(page_about)
    with col4 :
        st.page_link(page_customer)

    pages = {
        'about' : [page_about],
        'customers' : [page_customer],
        'services' : [page_services],
        'price' : [page_price]
    }
    nav =  st.navigation(pages,position='hidden')
    nav.run()


