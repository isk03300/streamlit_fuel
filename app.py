import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb







def main() :
    st.title('자동차 데이터 분석~')

    df = pd.read_csv('./data/fuel_econ.csv')

    if st.checkbox('데이터프레임 보기'):
        st.dataframe(df)
    else :
        st.text('')

    st.info('컬럼을 선택하면, 중복제거한 데이터의 개수를 보여줍니다.')

    choice = st.selectbox('컬럼 선택',df.columns)

    count =  df[choice].nunique()

    
    st.text('{} 컬럼의 중복제거한 개수는 {}개 입니다.'.format(choice,count))

    selected_list = st.multiselect('두 개의 컬럼을 선택하세요.' , df.columns[ 8 : ], max_selections=2 )

    if len(selected_list) == 2 :

        fig = plt.figure()
        plt.scatter(data = df, x=selected_list[0], y=selected_list[1])
        plt.title(selected_list[0] + 'vs' + selected_list[1])
        plt.xlabel(selected_list[0])
        plt.ylabel(selected_list[1])
        plt.show()
        st.pyplot(fig)

        st.text('상관계수')
        st.dataframe(df[selected_list].corr())

    


if __name__ == '__main__' :
    main()