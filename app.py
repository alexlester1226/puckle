import streamlit as st
import setup as s

st.set_page_config(page_title="PUCKLE", page_icon="🏒", layout="wide")

if not s.init:
    s.read()
    s.selectPlayer()
    s.init = True

with st.container():
    st.title("PUCKLE")
    st.write("WORDLE but for NHL players")

with st.container():
    c1, c2, c3 = st.columns((10, 1, 1))
    with c1:
        options = st.multiselect('Guess a player', s.dataName)
        if len(options) > 1:
            st.warning('Too many players')

    with c2:
        st.write("###")
        if st.button("Guess", type="primary"):
            if len(options) == 1 and not s.win:
                index = s.dataName.index(options[0])
                s.update(s.data[index])
                s.checkGuess(index)
                if s.data[index] == s.selectedPlayer:
                    st.balloons()
                    s.win = True
    with c3:
        st.write("###")
        reset = st.button('Reset', type='primary')

    if reset and not s.win:
        st.warning('The player was: ' + s.selectedPlayer.name)
        s.resetTable()
    elif reset:
        s.resetTable()

with st.container():
    st.markdown(s.display, unsafe_allow_html=True)

with st.sidebar.container():
    st.header("Instructions")
    st.write("- If your guess for one of the categories is :green[green] it is correct")
    st.write("- If your guess for one of the categories is :orange[yellow] it depends the category")
    st.write("- :orange[Team:]  Same division")
    st.write("- :orange[Age:]  ± 2 years age difference")
    st.write("- :orange[Height:]  Same foot (Ex. 5-10 & 5-8)")
    st.write("- :orange[Weight:]  ± 15lbs difference")
    st.write("- If your guess for one of the categories is black it is none of the above")
    st.write("###")
    st.write("###")
    st.write("Enjoy and if you need/want to contact us do so via email")
    st.write("- contact.puckle@gmail.com")
    st.write("###")
    st.caption("Made by: Alex Lester")
  
