import random 
import streamlit as st


st.title('Welcome to Number Guessing Game')
st.subheader('| By Qirat Saeed')

st.markdown('''
<style>
            .stApp{ background-color: #D4EBF8; color: black}
            </style>

''', unsafe_allow_html=True)


# Initailized the session
if 'guessed_number' not in st.session_state:
    st.session_state.guessed_number = random.randint(1,100)
if 'attempts' not in st.session_state:
    st.session_state.attempts =  0
if 'condition' not in st.session_state:
    st.session_state.condition= True

# User guessed input
user_guessed_number = st.number_input('Enter the value from **1 to 100**', min_value=1, max_value=100)

if st.button('Guess'):
    # Correct User guessed
    if st.session_state.attempts==4:
        st.info(f'Game Over! The correct number was {st.session_state.guessed_number}')
        st.session_state.attempts = 0
    else:
     st.session_state.attempts +=1
     if st.session_state.guessed_number ==  user_guessed_number:
        st.balloons()
        st.success(f'You guessed the correct number {st.session_state.attempts}')
        st.session_state.guessed_number = random.randint(1,100)
        st.session_state.attempts =  0
     elif user_guessed_number > st.session_state.guessed_number:
        st.warning('Too High!')
     elif user_guessed_number < st.session_state.guessed_number:
        st.error('Too Low')
     elif st.session_state.attempts>=4:
        st.info(f'Game Over! The correct number was {st.session_state.guessed_number} ')
        st.session_state.attempts = 0
     else:
        st.warning('Invalid Input')

# Display the total attempts
st.warning(f'Your total attempts is {4- st.session_state.attempts}')

st.write('----------------------------------------------------------------------------------------')
st.write('Created By Qirat Saeed')