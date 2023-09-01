# -*- coding: utf-8 -*-
import lightgbm as lgb 
import xgboost as xgb 
import streamlit as st 

def main():
    st.write("LightGBM Version: ", lgb.__version__)
    st.write("XGBoost Version: ", xgb.__version__)
    st.write("Streamlit Version: ", st.__version__)

if __name__ == "__main__":
    main()