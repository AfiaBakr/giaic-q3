

import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import json
import os
import datetime
from datetime import datetime
import time
import random
import plotly.express as px
import plotly.graph_objects as go
import requests
import json

st.set_page_config(
    page_title= "Personal Library Managment System",
    page_icon="📚", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header{
        font-size: 3rem !important;
        color: #1e3aba;
        font-weight: 700;
        margin-bottom: 1rem;
        font-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header{
        font-size: 1.8rem !important;
        color: #3882f6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .success-message{
        padding: 1rem;
        background-color: gray;
        border-left: 5px solid #10b981;
        border-radius: 0.375;        
    }
    .warning-message{
        padding: 1rem;
        background-color: #fef3c7;
        border-left: 5px solid #f59e0b;
        border-radius: 0.375;        
    }
    .book-card{
        padding: 1rem;
        background-color: #f3f4f6;
        margin-bottom: 1rem;
        border-radius: 0.5;
        border-left: 5px solid #3b82f6;
        transition: transform 0.3s ease;      
    }
    .book-card-hover{
        transition: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);        
    }
    .read-badge{
        background-color: #10b981;
        padding: 0.25rem 0.75; 
        color: gray;
        border-radius: 1rem;
        font-size: 0.875rem !important;
        font-weight: 600;        
    }
    .unread-badge{
        background-color: #f87171;
        padding: 0.25rem 0.75; 
        color: white;
        border-radius: 1rem;
        font-size: 0.875rem !important;
        font-weight: 600;        
    }
    .action-button{
        margin-right: 0.5rem;    
    }
    .stButton>button{
        border-radius: 0.375rem;
    }
</style>
""", unsafe_allow_html=True)


# Get Start

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()
    except:
        return None
    
if 'library' not in st.session_state:
    st.session_state.library = []
if 'research_result' not in st.session_state:
    st.session_state.research_result = []
if 'book_added' not in st.session_state:
    st.session_state.book_added = False
if 'remove_books' not in st.session_state:
    st.session_state.remove_books = False
if 'current_view' not in st.session_state:
    st.session_state.current_view = "library"
if 'library' not in st.session_state:
    st.session_state.library = []

# Load Library
def load_library():
    try:
        if os.path.exists('library.json'):
            with open ('library.json','r') as file:
                st.session_state.library = json.load(file)
                return True
            return False
    except Exception as e:
        st.error(f"Error loading Library: {e}")
        return False
    
# Save library
def save_library():
    try:
        
        with open ('library.json','w') as file:
            json.dump(st.session_state.library, file)
            return True
        
    except Exception as e:
        st.error(f"Error loading Library: {e}")
        return False

# Add a Book to Library
def book_added (book_title, book_author, publication_year, genre, read_status, add_book, date_time):
    book = {
        "book_title" : book_title,
        "book_author" : book_author,
        "publication_year" : publication_year,
        "genre" : genre,
        "read_status" : read_status,
        "add_book" :add_book,
        "date_time" : datetime.now().strftime("%Y-%m-%d %h:%m"),
    }
   

    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True
    time.sleep(0.5) #animation time

# Remove Books
def remove_books(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()
        st.session_state.remove_books = True
    return False

# Search Books
def search_books(search_term, search_by):
    search_term = search_term.lower()
    results= []

    for book in st.session_state.library:
        if search_by == "Title" and search_term in book["book_title"].lower():
            results.append(book)
        elif search_by == "Author" and search_term in book["book_author"].lower():
            results.append(book)
        elif search_by == "Genre" and search_term in book["genre"].lower():
            results.append(book)
        st.session_state.search_books = results

# Calculate Library States
def get_library_state():
    total_books = len(st.session_state.library)
    read_books = sum( 1  for book in st.session_state.library if book ['read_status'])
    percentage_books = ( read_books / total_books * 100) if total_books > 0 else 0

    genres = {}
    authors = {}
    decades = {}

    for book in st.session_state.library:
        if book('genre') is genres:
            genres[book['genres']] +=1
        else:
           genres[book['genres']] =1 

        if book('book_author') is authors:
            authors[book['book_author']] +=1
        else:
           authors[book['book_author']] =1

        decades = (book["publication_year"] // 10) * 10
        if decades in decades:
            decades[decades] += 1
        else:
            decades[decades] = 1

# Sort Count
    genres = dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
    authors = dict(sorted(authors.items(), key=lambda x: x[1], reverse=True))
    decades = dict(decades.items(), key=lambda x: x[0])

    return {
        "total_books" : total_books,
        "read_books" : read_books,
        "percentage_books" : percentage_books,
        "genres" :genres,
        "authors" : authors,
        "decades" :decades
    }

# Visualization States
def create_visual(states):
    if states ["total_books"] > 0:
        figure_read_status = go.Figure(data=[go.pie(
            lable = ['read', 'unread'],
            value = [states['read_books'], states['total_books'] - states['read_books']],
            hole = 0.5,
            marker_color = ['#ff9b9b','#7BC882']
        )])
        figure_read_status.update_layout(
            title_books = "Read vs Unread Books",
            show_legend = True,
            height = 400
        )
        st.plotly_chart(figure_read_status, use_container_width=True)

        if states ['genres']:
            genres_df = pd.DataFrame({
                'Genre': list(states['genres'].key()),
                'Count': list(states['genres'].values())
            })
            figure_genre =px.bar(
                genres_df,
                X = 'Genre',
                Y = 'Count',
                color= 'Count',
                color_continuous_scale= px.colors.sequential.Blues
            )
            figure_genre.update_layout(
                title_text ='Book Genres',
                xaxis_title = 'Genre',
                yaxis_title = 'Number of Books',
                height = 400
            )
        
        st.plotly_chart(figure_genre, use_container_width= True)

        if states ['decades']:
            decades_df = pd.DataFrame({
                'Decade' : [f"{decade}s" for decade in states['decades'].key()],
                'Count': list(states['decades'].values())
            })
            figure_decades = px.line(
                decades_df,
                x = 'Decade',
                y = 'Count',
                markers= True,
                line_shape= 'spline'
            )
            figure_decades.update_layout(
                title_text ='Book By Publication Decades',
                xaxis_title = 'Decades',
                yaxis_title = 'Number of Books',
                height = 400
            )
        st.plotly_chart(figure_decades, use_container_width= True)

load_library()
st.sidebar.markdown("<h1 style = 'text-align: center:'>Navigation</h1>", unsafe_allow_html=True)
lottie_book =load_lottieurl('http://assists9.lottiefiles.com/temp/1f20_aKAfIn.json')
if lottie_book:
    with st.sidebar:
        st.lottie(lottie_book, height = 200, key='book_animation')

nav_sidebar =st.sidebar.radio(
    "Choose an Option",
    ["View Library", "Search Book", "Add book", "Library Statistics"]
)
if nav_sidebar == 'View Library':
    st.session_state.current_view = 'library'
elif nav_sidebar == 'Search Book':
    st.session_state.current_view = 'search'
elif nav_sidebar == 'Add Book':
    st.session_state.current_view = 'add'
elif nav_sidebar == 'Library Statistics':
    st.session_state.current_view = 'statistics'


# main heading
st.markdown("<h1 class = 'main-header'>Library Manager</h1>", unsafe_allow_html=True)
if st.session_state.current_view == "add":
    st.markdown("<h1 class = 'sub-header'>Adda new Book</h1>", unsafe_allow_html=True)

    # adding book input form
    with st.form(key='add_book_form'):
        col1, col2 = st.columns(2)

        with col1:
            book_title = st.text_input("Book Title", max_chars = 100)
            book_author = st.text_input("Book Author", max_chars = 100) 
            publication_year = st.number_input("Publication Year", min_value=1000, max_value=datetime.now().year, step=1, value=2023) 
        with col2:
            genre = st.selectbox("Genre", [
                "Art", "Bio Graphy", "Bussiness", "Commerce", "Engineering", "Fantasy", "Fiction", "Finance", "Geogrphy", "Health", "History", "Litrature", "Non Fiction", "Poetry", "Religious", "Romance", "Science", "Story", "Technology", "Others"
            ]) 
            read_status = st.radio("Read Status", ["Read", "UnRead"], horizontal= True)
            read_bool = read_status == "Read"
        sumition_button = st.form_submit_button(label="Add Book")
        if sumition_button and book_title and book_author:            
            add_book(book_title, book_author, publication_year, genre, read_bool)

if st.session_state.book_added:
    st.markdown("<div class= 'success-message'>Book added Successfully</div>", unsafe_allow_html=True)
    st.balloons()
    st.session_state.book_added =False
else:
    st.session_state.current_view ==" Library"

st.markdown("<h2 class = 'sub-header'>Your Library</h>", unsafe_allow_html=True)
        
if not st.session_state.library:
    st.markdown("<div class = 'error-message'>Your Libary is Empty. Add some Book to get Started !</div>", unsafe_allow_html=True)
else:
    cols = st.columns(2) 
    for i, book in enumerate(st.session_state.library):
        with cols[i % 2]:
            st.markdown(f""" <div class= 'book-card'>
                    <h3><strong>Book Title:</strong>{book['book_title']}</h3>
                    <p><strong>Author:</strong> {book['book_author']}</p>
                    <p><strong>Publication Year:</strong> {book['publication_year']}</p>
                    <p><strong>Genre:</strong> {book['genre']}</p>
                    <p><span class='{"read_badge" if book["read_status"] else "unread_badge"}'>
                    {"Read" if book["read_status"] else "Unread"}
                    </span></p>
                    </div>
            """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
                    if st.button("Remove", key=f"remove_{i}"):
                        if remove_books(i):
                            st.rerun()
        with col2:
            new_status = not book['read_status']
            status_label = "Mark as Read" if not book ["read_status"] else "Mark as Unread"
            if st.button(status_label, key=f"status_{i}"):
                st.session_state.library[i]['read_status'] = new_status
                save_library()
                st.rerun()
    if st.session_state.remove_books:
        st.markdown("<div class = 'success-message'>Book Removed Successfully !</div>", unsafe_allow_html=True)
        st.session_state.remove_books = False
    elif st.session_state.current_view == "search":
        st.markdown("<div class = 'sub-header'>Search Books</div>", unsafe_allow_html=True)
                