import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main ():
    df = pd.read_csv('./data/fuel_econ.csv')

    st.header('자동차 데이터 분석')



    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)
    else :
        st.text('')


    st.text('컬럼을 선택하면, 중복제거한 데이터의 갯수를 보여줍니다.')

    choice=st.selectbox('컬럼선택', df.columns)
    
    count=df[choice].nunique()

    st.text('{} 컬럼의 중복제거한 데이터의 갯수는 {}개 입니다.'.format(choice, count))

    selected_list=st.multiselect('두개의 컬럼을 선택하세요', df.columns[8: ],max_selections=2)

    if len(selected_list) == 2 :
        fig=plt.figure()
        plt.scatter(data=df,x=selected_list[0],y=selected_list[1])
        plt.title(selected_list[0]+'Vs'+selected_list[1])
        plt.xlabel(selected_list[0])
        plt.ylabel(selected_list[1])
        st.pyplot(fig)
        
        st.text('상관계수')

        st.dataframe(df[ selected_list ].corr())

    


if __name__ == '__main__':
    main()