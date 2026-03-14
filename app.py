import streamlit as st
from pdf_utils import extract_pdf_text
from report_generator import generate_ddr
import os

st.title("🏠 AI DDR Report Generator")

st.write("Upload Inspection and Thermal Reports to generate a Diagnostic Report.")

inspection_file = st.file_uploader(
    "Upload Inspection Report", type=["pdf"]
)

thermal_file = st.file_uploader(
    "Upload Thermal Report", type=["pdf"]
)

if st.button("Generate DDR Report"):

    if inspection_file and thermal_file:

        with st.spinner("Extracting report data..."):

            inspection_text = extract_pdf_text(inspection_file)
            thermal_text = extract_pdf_text(thermal_file)

        with st.spinner("Generating DDR report using AI..."):

            report = generate_ddr(inspection_text, thermal_text)

        os.makedirs("outputs", exist_ok=True)

        with open("outputs/final_report.md", "w", encoding="utf-8") as f:
            f.write(report)

        st.success("DDR Report Generated!")

        st.markdown(report)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="DDR_Report.md",
            mime="text/markdown"
        )

    else:
        st.warning("Please upload both reports.")