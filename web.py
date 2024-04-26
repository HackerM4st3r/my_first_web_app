import streamlit as st
import functions as func

todos = func.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)

st.title("Aarush's first app")
st.subheader("Welcome!")
st.write("This app is for making notes about what to"
         " do for people who forget easily.Such as YOU!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")