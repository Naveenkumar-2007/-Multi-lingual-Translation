import streamlit as st
import pandas as pd
from src.pipeline.translation_pipeline import TranslationPipeline
from src.pipeline.localization_pipeline import LocalizationPipeline
from src.components.batch_processor import BatchProcessor

# Page config
st.set_page_config(page_title="Multi-lingual Translator", page_icon="🌍", layout="wide")

# Title
st.title("🌍 Multi-lingual Translation & Localization Tool")
st.markdown("---")

# Load pipelines lazily to avoid eager model downloads at startup
@st.cache_resource
def _create_pipelines():
    return TranslationPipeline(), LocalizationPipeline(), BatchProcessor()

def get_pipelines():
    """Return pipelines, creating them on first use."""
    return _create_pipelines()

# Languages
LANGUAGES = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
    'Hindi': 'hi', 'Chinese': 'zh', 'Arabic': 'ar', 'Russian': 'ru', 'Japanese': 'ja','Telugu':'te'
}

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Translation", "🌐 Localization", "📦 Batch Processing"])

# TAB 1: Translation
with tab1:
    st.subheader("Simple Translation")
    
    col1, col2 = st.columns(2)
    with col1:
        src_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), key='src1')
        input_text = st.text_area("Enter text:", height=150, key='input1')
    
    with col2:
        tgt_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1, key='tgt1')
    
    if st.button("🔄 Translate", type="primary"):
        if input_text:
            with st.spinner("Translating..."):
                trans_pipeline, _, _ = get_pipelines()
                result = trans_pipeline.translate(input_text, LANGUAGES[src_lang], LANGUAGES[tgt_lang])
                st.success("✅ Translation Complete!")
                st.text_area("Translation:", value=result['translated'], height=150)
                
                col_m1, col_m2 = st.columns(2)
                col_m1.metric("Original Length", len(input_text))
                col_m2.metric("Translated Length", len(result['translated']))
        else:
            st.warning("⚠️ Please enter text")

# TAB 2: Localization
with tab2:
    st.subheader("Translation with Localization")
    
    col1, col2 = st.columns(2)
    with col1:
        src_lang2 = st.selectbox("Source Language", list(LANGUAGES.keys()), key='src2')
        input_text2 = st.text_area("Enter text:", height=150, key='input2')
    
    with col2:
        tgt_lang2 = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1, key='tgt2')
        currency = st.selectbox("Currency", ['USD', 'EUR', 'GBP', 'INR', 'JPY'])
        units = st.radio("Units", ['metric', 'imperial'])
    
    if st.button("🌐 Translate & Localize", type="primary"):
        if input_text2:
            with st.spinner("Processing..."):
                _, local_pipeline, _ = get_pipelines()
                result = local_pipeline.localize(
                    input_text2, LANGUAGES[src_lang2], LANGUAGES[tgt_lang2], currency, units
                )
                st.success("✅ Localization Complete!")
                st.text_area("Localized Translation:", value=result['translated'], height=150)
        else:
            st.warning("⚠️ Please enter text")

# TAB 3: Batch Processing
with tab3:
    st.subheader("Batch Translation from CSV")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Preview:", df.head())
        
        text_col = st.selectbox("Select text column:", df.columns)
        src_lang3 = st.selectbox("Source Language", list(LANGUAGES.keys()), key='src3')
        tgt_lang3 = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1, key='tgt3')
        
        if st.button("📦 Translate All"):
            with st.spinner("Processing batch..."):
                _, _, batch_processor = get_pipelines()
                result_df = batch_processor.process_dataframe(
                    df, text_col, LANGUAGES[src_lang3], LANGUAGES[tgt_lang3]
                )
                st.success("✅ Batch translation complete!")
                st.dataframe(result_df)
                
                csv = result_df.to_csv(index=False)
                st.download_button("📥 Download", csv, "translations.csv", "text/csv")