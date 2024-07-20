import streamlit as st
from database_functions import (
    check_user_credentials,
    insert_user,
    username_exists,
    get_user_id,
    get_username,
    like_image,
    comment_on_image,
    get_comments,
    get_like_count
)

def main():
    if 'auth_status' not in st.session_state:
        st.session_state.auth_status = False

    if st.session_state.auth_status:
        home_page()
    else:
        page = st.sidebar.radio("Choose a page", ["Login", "Sign Up"])
        if page == "Login":
            login_page()
        elif page == "Sign Up":
            signup_page()

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_user_credentials(username, password):
            st.session_state.auth_status = True
            st.session_state.user_id = get_user_id(username)
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def signup_page():
    st.title("Sign Up")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    if st.button("Sign Up"):
        if username_exists(username):
            st.error("Username already exists")
        else:
            insert_user(username, password, first_name, last_name)
            st.success("Sign up successful! Please log in.")
            st.session_state.auth_status = False
            st.experimental_rerun()

def home_page():
    st.title("Home Page")

    if 'user_id' not in st.session_state:
        st.error("You need to log in first.")
        return

    user_id = st.session_state.user_id

    for image_id in range(1, 4):
        st.image(f"images/sample_image_{image_id}.jpg", caption=f"Image {image_id}")

        like_action = st.button(f"Like ❤️", key=f"like_{image_id}")
        if like_action:
            result = like_image(user_id, image_id)
            if result == "already_liked":
                st.warning("You have already liked this image.")
            st.experimental_rerun()

        like_count = get_like_count(image_id)
        st.write(f"Likes: {like_count}")

        with st.form(key=f"comment_form_{image_id}"):
            comment_text = st.text_area("Enter your comment", key=f"comment_{image_id}")
            submit_button = st.form_submit_button(label='Submit Comment')

            if submit_button and comment_text.strip():
                comment_on_image(user_id, image_id, comment_text)
                st.experimental_rerun()

        comments = get_comments(image_id)
        st.write("### Comments")
        if comments:
            for comment in comments:
                st.write(f"**{comment['username']}**: {comment['comment']}")
        else:
            st.write("No comments yet.")

    if st.button("Log Out"):
        st.session_state.auth_status = False
        st.experimental_rerun()

if __name__ == "__main__":
    main()
