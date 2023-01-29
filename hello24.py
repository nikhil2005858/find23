import openpyxl as op
import streamlit as st
wb=op.load_workbook('Result_N21_130_CS_ALL.xlsx')
st.table(wb)


