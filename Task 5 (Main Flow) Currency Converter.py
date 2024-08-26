#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
import json
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x270")
root.title("Currency Converter")
root.iconbitmap('C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\currency_conv.ico')
root.maxsize(600,270)
root.minsize(600,270)

image = Image.open("C:\\Users\\Gaurvi\\OneDrive\\Desktop\\Calculator\\17.jpg")
zoom = 0.5

# Multiple image size by zoom
pixels_x, pixels_y = tuple([int(zoom*x) for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
panel = Label(root, image=img)
panel.place(x=190, y=35)

def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    
    # Replace with your actual API key
    api_key = "YOUR_API_KEY" 
    url = f"https://v6.exchangerate-api.com/v6/a94f9d7a9e401c131061b9ec/latest/USD"
    
    if amount == '':
        messagebox.showerror("Currency Converter", "Please fill the amount.")
    elif to_currency == '':
        messagebox.showerror("Currency Converter", "Please choose the currency.")
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors

            data = response.json()

            if 'error' in data:
                messagebox.showerror("Currency Converter", data['error'])
            else:
                currency = from_currency.strip() + to_currency.strip()

                # Handle the case where the currency pair is not found
                if to_currency in data['conversion_rates']:
                    amount = float(amount)
                    cc = data['conversion_rates'][to_currency]
                    cur_conv = cc * amount
                    E2.insert(0, cur_conv)
                    text.insert('end', f'{amount} {from_currency} equals {cur_conv} {to_currency} \n\nLast update: {datetime.now()}')
                else:
                    messagebox.showerror("Currency Converter", f"Conversion rate for {currency} not found.")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Currency Converter", f"Error connecting to the API: {e}")
        except json.JSONDecodeError:
            messagebox.showerror("Currency Converter", "Invalid data received from the API.")
        except KeyError as e:
            messagebox.showerror("Currency Converter", f"Missing data in the API response: {e}")

def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')

l1 = Label(root, text="USD Currency Converter using Python", font=('verdana', 10, 'bold'))
l1.place(x=150, y=15)

amt = Label(root, text='Amount', font=('roboto', 10, 'bold'))
amt.place(x=20, y=15)
E1 = Entry(root, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E1.place(x=20, y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()
currencychoose1 = ttk.Combobox(root, width=20, textvariable=c1, state='readonly', font=('verdana', 10, 'bold'))

# Adding combobox drop down list
currencychoose1['values'] = ('USD',)
currencychoose1.place(x=300, y=40)
currencychoose1.current(0)

E2 = Entry(root, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E2.place(x=20, y=80)

currencychoose2 = ttk.Combobox(root, width=20, textvariable=c2, state='readonly', font=('verdana', 10, 'bold'))

# Adding combobox drop down list
currencychoose2['values'] = (
    'AFN', 'ARS', 'AWG', 'AUD', 'AZN', 'BSD', 'BSD', 'BBD', 'BYN', 'BZD', 'BMD', 'BOD', 'BAM', 'BWP', 'BGN',
    'BND', 'KHR', 'CAD', 'KYD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'XCD', 'EGP', 'SVC',
    'EUR', 'FKP', 'FJD', 'GHS', 'GIP', 'GTQ', 'GGP', 'GYD', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR',
    'IMP', 'ILS', 'JMD', 'JPY', 'KZT', 'KPW', 'KRW', 'KGS', 'LAK', 'LBP', 'LRD', 'MKD', 'MYR', 'MUR', 'MXN',
    'MNT', 'MZN', 'NAD', 'NPR', 'ANG', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 'PAB', 'PYG', 'PEN', 'PHP',
    'PLN', 'QAR', 'RON', 'RUB', 'SHP', 'SAR', 'RSD', 'SCR', 'SGD', 'SBD', 'SOS', 'ZAR', 'LKR', 'SEK', 'CHF',
    'SRD', 'SYP', 'TWD', 'THB', 'TTD', 'TRY', 'TVD', 'UAH', 'GBP', 'UYU', 'UZS', 'VEF', 'VND', 'YER', 'ZWD'
)

currencychoose2.place(x=300, y=80)

text = Text(root, height=7, width=52, font=('verdana', 10, 'bold'))
text.place(x=100, y=120)

B = Button(root, text="Search", command=show_data, font=('verdana', 10, 'bold'), borderwidth=2, bg="red", fg="white")
B.place(x=20, y=120)

clear = Button(root, text="Clear", command=clear, font=('verdana', 10, 'bold'), borderwidth=2, bg="blue", fg="white")
clear.place(x=20, y=170)

root.mainloop()


# In[ ]:




