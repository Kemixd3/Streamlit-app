

import pandas as pd
import os
import sys
import subprocess
import numpy as np
import streamlit as st
import time
import random
from random import randint
from streamlit_player import st_player
from streamlit_autorefresh import st_autorefresh
import altair as alt
import back as fl



#from dist.tost import pyarmor_runtime
#import dist.tost as fl

#import dist.tost as fl
#fl.pyarmor_runtime()


#st.set_page_config

st.set_page_config(
    page_title="Really cool app",
    page_icon="random",
    #page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
     )

st.sidebar.title("Select Menu")


#st.button(f"Click Me {st.session_state.emoji}", on_click=random_emoji)





option1, option2, option3, option4, option5, usertext1 = False, False, False, False, False, "default_text"
st.title('Hvordan fungerer programmering?')


emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
#st.session_state.emoji = random.choice(emojis)

# initialize emoji as a Session State variable
#if "emoji" not in st.session_state:
    #st.session_state.emoji = "👈"



#font_size = st.sidebar.number_input(
        #"emoji", min_value=0.5, max_value=4.0, value=2.0, step=0.1
    #)


# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
def hello():
    count = st_autorefresh(interval=2000,limit=2, key="fizzbuzzcounter")

    #The function returns a counter for number of refreshes. This allows the
    #ability to make special requests at different intervals based on the count
    if count == 0:
        st.write("Count is zero")
    elif count % 3 == 0 and count % 5 == 0:
        st.write("FizzBuzz")
    elif count % 3 == 0:
        st.write("Fizz")
    elif count % 5 == 0:
        st.write("Buzz")
    else:
        st.write(f"Count: {count}")

#https://discuss.streamlit.io/t/regarding-layout-of-streamlit-web-app/9602/2
#st.write(f"\n|Vil du Søge i databasen så skriv 1.|\n|Vil du se hele databasen skriv 2. |\n|Vil du tilføje til databasen tast 3.|\n|Vil du slette fra databasen tast 4: |\n|Vil du ændre på værdier i databasen tast 6.|\n| Vil du clear cmd tast 5:|\n|")

os.system('"streamlit run dist/usessss.py"')
st.text('Guide til programmering')
#os.system('python dist/usessss.py')
    #input = ""
#st.text_area("Input text")
b = True

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Links", st.write(random.choice(emojis))):
        
        option4 = True
        st.write("https://discuss.codecademy.com/")
        st.write("https://www.w3schools.com/")
        st.write("Vil du have flere kode øvelser? prøv:","https://www.codingame.com/home")
        
        b = False

with c2:
  #l = c2.button("Et eller andet")
  
    if st.button("Click Me", st.write(random.choice(emojis))):
        option3 = True
        b = False
        st.write("Hey")
       
with c3:

    o=st.button("Tilbage til forsiden", st.write(random.choice(emojis)))

#st.header("Tighten up left buttons with empty right columns!")

cont1, cont2, _, _, _, _ = st.columns(6)
#cont1.button("Tight")

#with cont2:
  #st.button("Tighter")

#st.header("You can even control relative size of columns")
#tc1, tc2, _= st.columns([1,1,9])
#tc1.button("Tighty")

#with tc2:
  #st.button("Tighterer")


key = (np.arange(9) * 2)
x3 = ('')
x2 = ('')
x1 = ('')
x5 = ()

#https://www.delftstack.com/howto/python/python-clear-console/
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'cls'):  
        command = 'cls'
    os.system(command)

df = pd.read_csv('out.zip')


total_rows2= len(df.index)+1
total_rows= len(df.index)-1
df4 = pd.DataFrame({'Produkt': 'Cheeseburger nuggets chilicheesetops milkshake bigmac apple cola water bigTastyBacon'.split(),
                   'Butik': 'Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds '.split(),
                   'Pris': 'Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds Macdonalds 20'.split(),
                   'iD': (total_rows)})
#st.write(df)
u = ()

 
#https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
submit1 = ()
submit = ()
submit2 = ()
submit3 = ()
so = ()



#https://discuss.streamlit.io/t/the-button-inside-a-button-seems-to-reset-the-whole-app-why/1051/6
c1, c2, c3 = st.columns([50,60,70])

#if p: 






if st.sidebar.checkbox(f"Projekt 1 - Database"):
    
    from dist.pytransform import pyarmor_runtime
    pyarmor_runtime()
    __pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\x00\x00\x03\x09\x00\x61\x0d\x0d\x0a\x08\x2d\xa0\x01\x00\x00\x00\x00\x01\x00\x00\x00\x40\x00\x00\x00\xef\x00\x00\x00\x00\x00\x00\x00\xd4\x0c\x74\xc0\x06\x34\x69\x5a\x4e\xd5\x0f\x20\xb3\x45\xfb\xbd\x00\x00\x00\x00\x00\x00\x00\x00\x71\x82\x82\x64\x72\x3a\xdf\x24\xb1\xd6\x39\x33\xdf\x8c\xe8\xc5\x04\xa3\x86\xa3\x78\x15\xdf\x21\x0a\x1e\x71\xd9\xf4\x3e\xd2\x7b\xa3\x84\xa1\x45\xdf\xaf\x18\x5f\x5d\x9e\x64\x56\xed\xa6\xbc\x71\x53\x02\x1e\xe7\x41\xbb\x13\xb8\xda\x00\x2e\xae\x8e\x4a\x93\x5c\xf4\xd7\xe7\x33\x35\xe8\x94\xde\xac\x52\xeb\x20\xce\xa9\x07\xe9\xee\x43\x6e\x96\x91\x74\x17\xcc\x38\xe5\x65\xed\x8c\xd5\xf6\xaa\x4d\x30\xc3\x3c\xc3\x97\xf4\x5f\x26\x4d\x82\xb2\xcb\xe0\x0f\xed\x18\x0d\x2a\x80\x81\x38\x3a\x7e\x9f\x8f\x5f\x96\x1e\x65\x96\x63\xef\x09\x32\x45\x77\xaa\x07\x9f\xd0\xf1\x40\x1a\xdc\x4d\xbb\xd6\xcb\x61\x7e\x02\x0e\x12\x62\xf8\x3f\xea\xeb\x03\xc9\x03\xf3\x9c\xe5\xb4\x52\x56\xcb\x4e\xf4\x96\x92\x31\x1a\xe3\x81\x50\x02\x1a\x3d\x91\x36\x70\x21\x1a\xa8\xed\x96\xdb\x35\xc6\xd7\xb9\x32\x57\xac\x24\x72\xec\xad\x1c\xe6\x8d\x56\x58\x16\x11\xe1\xe6\x13\xd4\xdc\x9c\x9c\x3b\xc4\x1f\x9b\x8d\x5e\xce\x4c\xba\x68\x8c\xf4\xaf\x50\x05\xd6\x6a\x59\x52\xf2\xd5\xd3\xaa\xd0\x5c\x08\xb5\x88', 2)
    
   
    option2 = True
    
    st.write(fl.g())
    slider_ph = st.empty()
    info_ph = st.empty()
    b = False

    value = slider_ph.slider("slider", 1, 10, 1, 1)
    info_ph.info(value)
    st.image(str(value) + ".png",)
    
    if st.button('Vis alle slides'):
        b = False

        for x in range(10):

            
            value = int(value)
            value = slider_ph.slider("slider", 0, 10, value + 1, 1)
            info_ph.info(value)
            time.sleep(4)
            
            value = str(value)
            st.image(str(value) + ".png",)
    st.title("What is Recursion?")
    st.write(f"Recursion Defined What is recursion? Sometimes a problem is too difficult or too complex to solve because it is too big. If the problem can be broken down into smaller versions of itself, we may be able to find a way to solve one of these smaller versions and then be able to build up to a solution to the entire problem. This is the idea behind recursion; recursive algorithms break down a problem into smaller pieces which you either already know the answer to, or can solve by applying the same algorithm to each piece, and then combining the results. Stated more concisely, a recursive definition is defined in terms of itself. Recursion is a computer programming technique involving the use of a procedure, subroutine, function, or algorithm that calls itself in a step having a termination condition so that successive repetitions are processed up to the critical step where the condition is met at which time the rest of each repetition is processed from the last one called to the first. \n Don't worry about the details of that definition. The main point of it is that it is defined in terms of itself: Recursion: ... for more information, see Recursion.    \n")
    st.write("https://www.sparknotes.com/cs/recursion/whatisrecursion/section1/")
            
                    
                

    
            

                
                
                

    

if st.sidebar.checkbox("Programmerings øvelser"):
    
    option1 = True
    b = False
    st.write("Hvad skal der i opg.1 for at køre loopet 10 gange?")
    

    with c1:
        
        st.header("Opg. 1 \n     for (let i = 0; i < ")
        #st.write("for (let i = 0; i < ")
        st.write("text += cars[i]; }")
        new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
        
    with c2:
        st.header("")
        so = (st.text_input((""), key = '91' ))
        st.write({so})
       

        if so != ("10"):
            st.write("False")
            x1 = int(1)
            #form6 = st.form(key='my-form6')
            #x45 = form6.text_input('')
            #submit4 = form6.form_submit_button('Submit')
            #st.write(x45)
            #so = x45
            #st.write(so) 
    with c3:
        st.header(".\n     ;i++) {")
        
    if so == ("10"):
        original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">True</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        

        x2 = int(2)

    
    c4, c5, c6 = st.columns([50,60,70])



    #if p: 
    st.write("Hvad skal der i opg.2 for at køre loopet 20 gange?")
    with c4:
        st.header("Opg. 2 \n     for (let i = 0; i < ")
        #st.write("for (let i = 0; i < ")
        st.write("text += cars[i]; }")
        new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
        
    with c5:
        st.header("")
        su = (st.text_input((""), key = '910' ))
        st.write({su})

        if su != ("20"):
            st.write("False")
            x1 = int(1)

        
            
            #form6 = st.form(key='my-form6')
            #x45 = form6.text_input('')
            #submit4 = form6.form_submit_button('Submit')
            #st.write(x45)
            #so = x45
            #st.write(so) 
    with c6:
        st.header(".\n     ;i++) {")


        if su == ("20"):
        
            original_title3 = '<p style="font-family:Courier; color:Blue; font-size: 20px;">True</p>'
            st.markdown(original_title3, unsafe_allow_html=True)
            x2 = int(2)
    
    form = st.form(key='my-form')
    submit = form.form_submit_button('Tilføj til Databasen')


    if submit:
        
        df2 = pd.DataFrame({'Antal forkerte svar': [x1],
                'Antal rigtige svar': [x2]})
    
        df = df.append((df2), ignore_index=False)
        
        df = df.append((df2), ignore_index=False)
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
        compression_opts = dict(method = 'zip',
                                archive_name='out.csv')
        df.to_csv('out.zip', index=False,
                    compression=compression_opts)
        
        st.write(df)

if st.sidebar.checkbox("Tilbage til forsiden"):
    option5 = True
    
    initial_sidebar_state: "expanded"
    option1, option2, option3, option4, option5, usertext1 = False, False, False, False, False, "default_text"


if o:
   
    
    
    #form1 = st.form(key='my-form1')
    #x10 = form1.text_input('Indtast Burger')
    #submit1 = form1.form_submit_button('Submit')

    
    
    #form2 = st.form(key='my-form2')
    #x20 = form2.text_input('Indtast Butik')
    #submit2 = form2.form_submit_button('Submit')

    
    #form3 = st.form(key='my-form3')
    #x30 = form3.text_input('Indtast Pris')
    #submit3 = form3.form_submit_button('Submit')
    
    #st.write(f'hello {x1}')
    #st.write("hvilket produkt vil du tilføje?")
    #x11= st.text_input((''), key = '25')
    #st.write("Hvilket butik er produktet fra?")
    #x22= st.text_input((''), key = '24')
    #st.write("Hvad kostede produktet?")
    #x33= st.text_input((''), key = '23')
    #st.write('Press submit to have your name printed below')
    
    
    #form = st.form(key='my-form')
    #submit = form.form_submit_button('Tilføj til Databasen')


    #if submit1:
        #x1 = ({x10})
        
    
    #if submit2:
        #x2 = ({x20})
        
 
    



    if submit3:
      
            
        df2 = pd.DataFrame({'Antal forkerte svar': [x1],
                    'Antal rigtige svar': [x2]})
    
        df = df.append((df2), ignore_index=False)
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
        compression_opts = dict(method = 'zip',
                                archive_name='out.csv')
        df.to_csv('out.zip', index=False,
                    compression=compression_opts)
        
        #df = df.drop([(total_rows)], axis = 0)
    #df = df.drop([(total_rows)], axis = 0)
        #i = st.text_input((''), key = "<25>")
            
        #if i == str("ok"):
            #hello()
        


submit4 = ()
if u == str("4"):
    print("Hvilket række vil du slette?")
    #x5 = int(input())
    
    #x5 = int(st.text_input(''),key='30')
    #df = df.drop([x5], axis = 0)
    
    form4 = st.form(key='my-form4')
    
    x40 = form4.text_input('')
    submit4 = form4.form_submit_button('Submit')
    st.write(x40)
    x5 = x40
   
    if submit4:
        x5 = int(x5)
        st.write(x5)
        df = df.drop([x5], axis=0)
        compression_opts = dict(method = 'zip',
                            archive_name='out.csv')
        df.to_csv('out.zip', index=False,
                compression=compression_opts)
        
        
#df = df.drop([0], axis = 0)
#df = df.set_index("Burger")
#df = df.drop('hej', axis = 0)


x10 = ()
x11 = ()
options = [x10]
search = [x11]
x9 = ()
x8 = ()
if u == str("6"):
    st.write("Hvilken burger vil du ændre på?")
    
    x10 = st.text_input((''), key = '60')
    options = [x10]
    st.write("Indtast gamle værdi")
    x8 = st.text_input((''), key = '61')
    st.write("Indtast nye værdi")
    x9 = st.text_input((''), key = '62')
    
    if st.button('Click func too'):
        
        df[df['Produkt'].isin(options)] = df[df['Produkt'].isin(options)].replace(x8,x9)
        compression_opts = dict(method = 'zip',
                            archive_name='out.csv')
        df.to_csv('out.zip', index=False,
                compression=compression_opts)
    #https://youtu.be/F-gDgQ6kuuk?t=460
    #https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
    
    #rslt_df = df[df['Burger'].isin(options)]
    #print (rslt_df)

#if u == str("3"):
    #df = df.append((df2), ignore_index=False)
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    #compression_opts = dict(method = 'zip',
                            #archive_name='out.csv')
        #df.to_csv('out.zip', index=False,
                #compression=compression_opts)


#x5 = int(input())
#    print(type(x5))

line2 = ()
def søg(l):
    #st.write(df.loc[df[g]])
    
    df.sort_values(by='Produkt', inplace=True, key=lambda col: col.str.lower())
    for line in df['Produkt']:
        if line == '':
            pass
        elif l in str(line).lower():
           st.write(line)
           st.write(df.loc[df['Produkt'] == (line)])
        elif l in str(line):
               st.write(df.loc[df['Produkt'] == (line)])
           #st.write(df.loc(line).isin(df['Produkt']))
            

if u == str("5"):
    clearConsole()

#if o: 
    #st.title("Sorteret fra a-z")
    #df.sort_values(by='Produkt',inplace=True)
    #st.write(df)
    
ur2=()
ur=5000
if u == str("1"):
    st.title("Hvad vil ud søge på?")
   
    ur = st.text_input(("").lower(), key = '70' )
    søg(str(ur))

    
    
if b == True:
    st_player("https://www.youtube.com/watch?v=r5kfkpYtOiw")
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')

#if ur == str("5"):
    # = st.text_input((''), key = '77' )
   # for x in range(len([df['Butik']])):
    #    if df['Butik'[x]] in h:
    #st.write(df.loc[df['Butik'] == h])

#if ur == str("6"):
    #b = (input(''))
    #b = st.text_input((''), key = '71' )
    
    #x11 = input('')
    #search = [x11]
    #st.write(df.loc[df['Pris'] == b])
    #print(df.loc[['Pris'].isin[(search)] == b])
     
    #print(df.loc[['Pris'] == b])
#if ur == str("7"):
    #c = st.text_input((''), key = '73' )
    #st.write(df.loc[df['iD'] == c])
#if ur == str("8"):
    #d = st.text_input((''), key = '72' )
    #st.write(df.loc[df['Produkt'] == d])


#os.system("web.py")
input = ""
    
      





