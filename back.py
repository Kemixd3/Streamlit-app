import pandas as pd
import os
import sys
import subprocess
import numpy as np
import streamlit as st
import time
from random import randint
from streamlit_autorefresh import st_autorefresh
new = ('')

def g():
    st.title('Database')
    # Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
    # after it's been refreshed 100 times.
    def hello():
        count = st_autorefresh(interval=2000,limit=2, key="fizzbuzzcounter")

        # The function returns a counter for number of refreshes. This allows the
        # ability to make special requests at different intervals based on the count
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


    st.write(f"\n|Vil du Søge i databasen så skriv 1. Vil du se hele databasen skriv 2     |\n|Vil du tilføje til databasen tast 3. Vil du slette fra databasen tast 4: |\n|Vil du ændre på værdier i databasen tast 6. Vil du clear cmd tast 5:     |\n|")
    st.text('Informatik, Silas og Nikolai 3.M')
    u = st.text_input("")



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
    st.write(df)


    
    #https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
    submit1 = ()
    submit = ()
    submit2 = ()
    submit3 = ()




    if u == str("3"):
        

        form1 = st.form(key='my-form1')
        x10 = form1.text_input('Indtast Produkt')
        submit1 = form1.form_submit_button('Submit')


        
        form2 = st.form(key='my-form2')
        x20 = form2.text_input('Indtast Butik')
        submit2 = form2.form_submit_button('Submit')

        
        form3 = st.form(key='my-form3')
        x30 = form3.text_input('Indtast pris')
        submit3 = form3.form_submit_button('Submit')
        
        #st.write(f'hello {x1}')
        #st.write("hvilket produkt vil du tilføje?")
        #x11= st.text_input((''), key = '25')
        #st.write("Hvilket butik er produktet fra?")
        #x22= st.text_input((''), key = '24')
        #st.write("Hvad kostede produktet?")
        #x33= st.text_input((''), key = '23')
        #st.write('Press submit to have your name printed below')
        
        
        form = st.form(key='my-form')
        submit = form.form_submit_button('Tilføj til databasen')


        #if submit1:
            #x1 = ({x10})
            
        
        #if submit2:
            #x2 = ({x20})
            
        
        if submit3:
            kl = 0
            for x in df["iD"]:
                if int(x) > kl:
                    kl = int(x)
            new_id = kl+1
            x3 = (x30)
            x2 = (x20)
            x1 = (x10)
            

            df2 = pd.DataFrame({'Produkt': [x1],
                    'Butik': [x2],
                    'Pris': [x3],
                    'iD': (new_id)})
    
            df = df.append((df2), ignore_index=False)
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
            compression_opts = dict(method = 'zip',
                                    archive_name='out.csv')
            df.to_csv('out.zip', index=False,
                        compression=compression_opts)
            hello()
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

   
    line2 = ()
    def sog(l):
        
        df.sort_values(by='Produkt', inplace=True, key=lambda col: col.str.lower())
        
        for line in df['Produkt']:
            if line == '':
                pass
            elif l in str(line).lower():
                st.write(line)
                st.write(df.loc[df['Produkt'] == (line)])
                st.title("Søg globalt i Databasen")
                item = st.text_input(("").lower(), key = 'hey' )
                mask = (df.applymap(lambda x: isinstance(x, str) and item in x)).any(1)
                st.write(df[mask])
            elif l in str(line):
                st.write(df.loc[df['Produkt'] == (line)])
                item = st.text_input((""), key = '82' )
                mask = (df.applymap(lambda x: isinstance(x, str) and item in x)).any(1)
                st.write(df[mask])
            #st.write(df.loc(line).isin(df['Produkt']))
              
                

    if u == str("5"):
        clearConsole()

    if u == str("2"):
        st.title("Sorteret fra a-z")
        df.sort_values(by='Produkt',inplace=True)
        st.write(df)
        
    ur2=()
    ur=5000
    if u == str("1"):
        st.title("Hvilket produkt vil du søge på?")
        
        ur = st.text_input(("").lower(), key = '70' )
        sog(str(ur))

        
        

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


        
        
        
        os.system("python backs.py")

    else:
    
        os.system("backs.py")

        
