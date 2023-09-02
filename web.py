import streamlit as st
import functions


todos = functions.get_todos()

st.set_page_config(layout='wide')

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.write('This app is to increase <b>productivity</b>',
            unsafe_allow_html = True)
st.write('<b>Please check the item</b> in below list to complete that task',unsafe_allow_html=True)
st.text_input(label="Enter todo:",placeholder='Add new todo...',
              on_change=add_todo, key = 'new_todo')


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




# st.session_state