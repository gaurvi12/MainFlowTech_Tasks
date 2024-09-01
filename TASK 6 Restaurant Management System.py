#!/usr/bin/env python
# coding: utf-8

# In[107]:


from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog


def total_bills():
    
    #===== Drink Items Price =====
    
    lassi_price = 50
    coffee_price = 25
    tea_price = 15
    juice_price = 30
    shakes_price = 50
    milk_price = 20
    iced_tea_price = 15
    
    #===== Main Course Items Price =====
    
    roti_price = 10
    dal_makhani_price = 120
    matar_paneer_price = 150
    paneer_parantha_price = 50
    mix_veg_price = 80
    plain_rice_price = 100
    
    #===== Drinks Item Quantity =====
    
    lassi_q = lassi_qty.get()
    coffee_q = coffee_qty.get()
    tea_q = tea_qty.get()
    juice_q = juice_qty.get()
    shakes_q = shakes_qty.get()
    milk_q = milk_qty.get()
    iced_tea_q = iced_tea_qty.get()
    
    #===== Main Course Items Quantity =====
    
    roti_q = roti_qty.get()
    dal_makhani_q = dal_makhani_qty.get()
    matar_paneer_q = matar_paneer_qty.get()
    paneer_parantha_q = paneer_parantha_qty.get()
    mix_veg_q = mix_veg_qty.get()
    plain_rice_q = plain_rice_qty.get()
    
    #===== Drinks Item Validation =====
    
    if lassi_var.get() == 0:
        lassi_q = 0
    elif lassi_var.get() == 1 and lassi_qty.get() == "":
        messagebox.showerror("Error","Please fill the Lassi quantity!")
        lassi_q = 0
        
    if coffee_var.get() == 0:
        coffee_q = 0
    elif coffee_var.get() == 1 and coffee_qty.get() == "":
        messagebox.showerror("Error","Please fill the Coffee quantity!")
        coffee_q = 0
        
    if tea_var.get() == 0:
        tea_q = 0
    elif tea_var.get() == 1 and tea_qty.get() == "":
        messagebox.showerror("Error","Please fill the Tea quantity!")
        tea_q = 0
        
    if juice_var.get() == 0:
        juice_q = 0
    elif juice_var.get() == 1 and juice_qty.get() == "":
        messagebox.showerror("Error","Please fill the Juice quantity!")
        juice_q = 0
        
    if shakes_var.get() == 0:
        shakes_q = 0
    elif shakes_var.get() == 1 and shakes_qty.get() == "":
        messagebox.showerror("Error","Please fill the Shake quantity!")
        shakes_q = 0
        
    if milk_var.get() == 0:
        milk_q = 0
    elif milk_var.get() == 1 and milk_qty.get() == "":
        messagebox.showerror("Error","Please fill the Milk quantity!")
        milk_q = 0
    
    if iced_tea_var.get() == 0:
        iced_tea_q = 0
    elif iced_tea_var.get() == 1 and iced_tea_qty.get() == "":
        messagebox.showerror("Error","Please fill the Iced tea quantity!")
        iced_tea_q = 0
        
    #===== Main Course Items Validation =====
    
    if roti_var.get() == 0:
        roti_q = 0
    elif roti_var.get() == 1 and roti_qty.get() == "":
        messagebox.showerror("Error","Please fill the Roti quantity!")
        roti_q = 0
        
    if dal_makhani_var.get() == 0:
        dal_makhani_q = 0
    elif dal_makhani_var.get() == 1 and dal_makhani_qty.get() == "":
        messagebox.showerror("Error","Please fill the Dal Makhani quantity!")
        dal_makhani_q = 0
        
    if matar_paneer_var.get() == 0:
        matar_paneer_q = 0
    elif matar_paneer_var.get() == 1 and matar_paneer_qty.get() == "":
        messagebox.showerror("Error","Please fill the Matar Paneer quantity!")
        matar_paneer_q = 0
        
    if paneer_parantha_var.get() == 0:
        paneer_parantha_q = 0
    elif paneer_parantha_var.get() == 1 and paneer_parantha_qty.get() == "":
        messagebox.showerror("Error","Please fill the Paneer Parantha quantity!")
        paneer_parantha_q = 0
        
    if mix_veg_var.get() == 0:
        mix_veg_q = 0
    elif mix_veg_var.get() == 1 and mix_veg_qty.get() == "":
        messagebox.showerror("Error","Please fill the Mix Veg quantity!")
        mix_veg_q = 0
        
    if plain_rice_var.get() == 0:
        plain_rice_q = 0
    elif plain_rice_var.get() == 1 and plain_rice_qty.get() == "":
        messagebox.showerror("Error","Please fill the Plain Rice quantity!")
        plain_rice_q = 0
        
        
    #===== Total Drink Items Price =====
    
    total_lassi_price = lassi_price * int(lassi_q)
    total_coffee_price = coffee_price * int(coffee_q)
    total_tea_price = tea_price * int(tea_q)
    total_juice_price = juice_price * int(juice_q)
    total_shakes_price = shakes_price * int(shakes_q)
    total_milk_price = milk_price * int(milk_q)
    total_iced_tea_price = iced_tea_price * int(iced_tea_q)
    
    #===== Total Main Course Items Price =====
    
    total_roti_price = roti_price * int(roti_q)
    total_dal_makhani_price = dal_makhani_price * int(dal_makhani_q)
    total_matar_paneer_price = matar_paneer_price * int(matar_paneer_q)
    total_paneer_parantha_price = paneer_parantha_price * int(paneer_parantha_q)
    total_mix_veg_price = mix_veg_price * int(mix_veg_q)
    total_plain_rice_price = plain_rice_price * int(plain_rice_q)
  
    #===============================================

    E_LASSI= StringVar()
    E_COFFEE= StringVar()
    E_TEA= StringVar()
    E_JUICE= StringVar()
    E_SHAKES= StringVar()
    E_MILK= StringVar()
    E_ICED_TEA= StringVar()

    E_ROTI= StringVar()
    E_DAL_MAKHANI= StringVar()
    E_MATAR_PANEER= StringVar()
    E_PANEER_PARANTHA= StringVar()
    E_MIX_VEG= StringVar()
    E_PLAIN_RICE= StringVar()

    #==========For Calculating Bill Receipt==========
  
    if E_LASSI.get() != "":
        E_LASSI.delete(0,"end")
    else:
        E_LASSI.set(total_lassi_price)
        
        
    if E_COFFEE.get() != "":
        E_COFFEE.delete(0,"end")
    else:
        E_COFFEE.set(total_coffee_price)
        
        
    if E_TEA.get() != "":
        E_TEA.delete(0,"end")
    else:
        E_TEA.set(total_tea_price)
        
        
    if E_JUICE.get() != "":
        E_JUICE.delete(0,"end")
    else:
        E_JUICE.set(total_juice_price)
     
    
    if E_SHAKES.get() != "":
        E_SHAKES.delete(0,"end")
    else:
        E_SHAKES.set(total_shakes_price)
        
        
    if E_MILK.get() != "":
        E_MILK.delete(0,"end")
    else:
        E_MILK.set(total_milk_price)
        
        
    if E_ICED_TEA.get() != "":
        E_ICED_TEA.delete(0,"end")       
    else:
        E_ICED_TEA.set(total_iced_tea_price)
   
 #================FOODS=======================
     
    if E_ROTI.get() != "":
        E_ROTI.delete(0,"end")
    else:
        E_ROTI.set(total_roti_price)
  

    if E_DAL_MAKHANI.get() != "":
        E_DAL_MAKHANI.delete(0,"end")
    else:
        E_DAL_MAKHANI.set(total_dal_makhani_price)
  

    if E_MATAR_PANEER.get() != "":
        E_MATAR_PANEER.delete(0,"end")
    else:
        E_MATAR_PANEER.set(total_matar_paneer_price)
  

    if E_PANEER_PARANTHA.get() != "":
        E_PANEER_PARANTHA.delete(0,"end")
    else:
        E_PANEER_PARANTHA.set(total_paneer_parantha_price)
  

    if E_MIX_VEG.get() != "":
        E_MIX_VEG.delete(0,"end")
    else:
        E_MIX_VEG.set(total_mix_veg_price)
  

    if E_PLAIN_RICE.get() != "":
        E_PLAIN_RICE.delete(0,"end")
    else:
        E_PLAIN_RICE.set(total_plain_rice_price)

        
        
    #===== Total Drinks Cost =====
    
    total_drinks_cost =   total_coffee_price + total_tea_price + total_juice_price + total_shakes_price +total_milk_price + total_iced_tea_price
    
    if drinks_cost.get() != "":
        drinks_cost.delete(0,"end")
        drinks_cost.insert("end",total_drinks_cost)
    else:
        drinks_cost.insert("end",total_drinks_cost)
        
    
    #===== Total Main Course Items Price =====
    
    total_foods_cost = total_roti_price + total_dal_makhani_price + total_matar_paneer_price + total_paneer_parantha_price + total_mix_veg_price + total_plain_rice_price
    
    if foods_cost.get() != "":
        foods_cost.delete(0,"end")
        foods_cost.insert("end", total_foods_cost)
    else:
        foods_cost.insert("end", total_foods_cost)
        
    if service_charge.get() != "":
        service_charge.delete(0,"end")
        service_charge.insert(0,"10")
    else:
        service_charge.insert(0,"10")
        
    fc = int(foods_cost.get())
    dc = int(drinks_cost.get())
    
    total_paid_tax = fc+dc
    total_paid_tax = total_paid_tax * 8/100
    
    if paid_tax != "":
        paid_tax.delete(0,"end")
        paid_tax.insert(0,total_paid_tax)
    else:
        paid_tax.insert(0,total_paid_tax)
        
    total_sub_cost = fc+dc+int(service_charge.get())
    
    if sub_total.get() !="":
        sub_total.delete(0,"end")
        sub_total.insert(0,total_sub_cost)
    else:
        sub_total.insert(0,total_sub_cost)
        
    if total_cost_cost.get() !="":
        total_cost_cost.delete(0,"end")
        total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))
    else:
        total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))

        
 
    #===== Total Bill Receipt =====
    date = datetime.now().date()
    if bill_details.get(1.0,"end") !="":
        bill_details.delete(1.0,"end")
        bill_details.insert(1.0, f"Billno-{random.randint(100, 1000)} \t{date} ===================\n")
        bill_details.insert(END,"Items(q)\t\t"+ "Amount ===================\n")
        if lassi_var.get() ==1:
            bill_details.insert(END,f"Lassi: {str(lassi_q)} \t\t" + E_LASSI.get()+"\n" )
        if coffee_var.get() ==1:
            bill_details.insert(END,f"Coffee: {str(coffee_q)} \t\t" + E_COFFEE.get()+"\n" )
        if tea_var.get() ==1:
            bill_details.insert(END,f"Tea: {str(tea_q)} \t\t" + E_TEA.get()+"\n" )
        if juice_var.get() ==1:
            bill_details.insert(END,f"Juice: {str(juice_q)} \t\t" + E_JUICE.get()+"\n" )
        if shakes_var.get() ==1:
            bill_details.insert(END,f"Shakes: {str(shakes_q)} \t\t" + E_SHAKES.get()+"\n" )
        if milk_var.get() ==1:
            bill_details.insert(END,f"Milk: {str(milk_q)} \t\t" + E_MILK.get()+"\n" )
        if iced_tea_var.get() ==1:
            bill_details.insert(END,f"Iced Tea:{str(iced_tea_q)} \t\t" + E_ICED_TEA.get()+"\n" )
            
        if roti_var.get() ==1:
            bill_details.insert(END,f"Roti: {str(roti_q)} \t\t" + E_ROTI.get()+"\n" )
        if dal_makhani_var.get() ==1:
            bill_details.insert(END,f"Dal Makhani:{str(dal_makhani_q)} \t\t" + E_DAL_MAKHANI.get()+"\n" )
        if matar_paneer_var.get() ==1:
            bill_details.insert(END,f"Matar Paneer:{str(matar_paneer_q)} \t\t" + E_MATAR_PANEER.get()+"\n" )
        if paneer_parantha_var.get() ==1:
            bill_details.insert(END,f"PaneerParantha:{str(paneer_parantha_q)} \t\t" + E_PANEER_PARANTHA.get()+"\n" )
        if mix_veg_var.get() ==1:
            bill_details.insert(END,f"MiX Veg:{str(mix_veg_q)} \t\t" + E_MIX_VEG.get()+"\n" )
        if plain_rice_var.get() ==1:
            bill_details.insert(END,f"Plain Rice:{str(plain_rice_q)} \t\t" + E_PLAIN_RICE.get()+"\n" )
        bill_details.insert(END,"Total Amount:\t\t" + total_cost_cost.get() + "\n")   
        

def save():
    root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
    if root.filename is None:
        return
    file_save = str(bill_details.get(1.0,END))
    root.filename.write(file_save)
    root.filename.close()
                            
#===== Drinks Check Button Validation =====
                            
def lassi_chk():
    if lassi_var.get() ==1:
        lassi_qty['state'] ="normal"
        lassi_qty['bg'] = "powder blue"
        lassi_qty['fg']="black"
    else:
        lassi_qty['state']="disabled"
                            
def coffee_chk():
    if coffee_var.get() ==1:
        coffee_qty['state'] ="normal"
        coffee_qty['bg'] = "powder blue"
        coffee_qty['fg']="black"
    else:
        coffee_qty['state']="disabled"
                        
def tea_chk():
    if tea_var.get() ==1:
        tea_qty['state'] ="normal"
        tea_qty['bg'] = "powder blue"
        tea_qty['fg']="black"
    else:
        tea_qty['state']="disabled"
                        
def juice_chk():
    if juice_var.get() ==1:
        juice_qty['state'] ="normal"
        juice_qty['bg'] = "powder blue"
        juice_qty['fg']="black"
    else:
        juice_qty['state']="disabled"
                            
def shakes_chk():
    if shakes_var.get() ==1:
        shakes_qty['state'] ="normal"
        shakes_qty['bg'] = "powder blue"
        shakes_qty['fg']="black"
    else:
        shakes_qty['state']="disabled"
                            
def milk_chk():
    if milk_var.get() ==1:
        milk_qty['state'] ="normal"
        milk_qty['bg'] = "powder blue"
        milk_qty['fg']="black"
    else:
        milk_qty['state']="disabled"
                            
                            
def iced_tea_chk():
    if iced_tea_var.get() ==1:
        iced_tea_qty['state'] ="normal"
        iced_tea_qty['bg'] = "powder blue"
        iced_tea_qty['fg']="black"
    else:
        iced_tea_qty['state']="disabled"
                            
#===== Main Course Items Check Button Validation =====
                            
def roti_chk():
    if roti_var.get() ==1:
        roti_qty['state'] ="normal"
        roti_qty['bg'] = "powder blue"
        roti_qty['fg']="black"
    else:
        roti_qty['state']="disabled"
                
def dal_makhani_chk():
    if dal_makhani_var.get() ==1:
        dal_makhani_qty['state'] ="normal"
        dal_makhani_qty['bg'] = "powder blue"
        dal_makhani_qty['fg']="black"
    else:
        dal_makhani_qty['state']="disabled"
                            
def matar_paneer_chk():
    if matar_paneer_var.get() ==1:
        matar_paneer_qty['state'] ="normal"
        matar_paneer_qty['bg'] = "powder blue"
        matar_paneer_qty['fg']="black"
    else:
        matar_paneer_qty['state']="disabled"
                            
def paneer_parantha_chk():
    if paneer_parantha_var.get() ==1:
        paneer_parantha_qty['state'] ="normal"
        paneer_parantha_qty['bg'] = "powder blue"
        paneer_parantha_qty['fg']="black"
    else:
        paneer_parantha_qty['state']="disabled"
                            
def mix_veg_chk():
    if mix_veg_var.get() ==1:
        mix_veg_qty['state'] ="normal"
        mix_veg_qty['bg'] = "powder blue"
        mix_veg_qty['fg']="black"
    else:
        mix_veg_qty['state']="disabled"
                            
def plain_rice_chk():
    if plain_rice_var.get() ==1:
        plain_rice_qty['state'] ="normal"
        plain_rice_qty['bg'] = "powder blue"
        plain_rice_qty['fg']="black"
    else:
        plain_rice_qty['state']="disabled"
                            

#===== Calculator Code =====
def nine():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","9")
    else:
        result.insert("end","9")
                            
def eight():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","8")
    else:
        result.insert("end","8")
                    
def seven():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","7")
    else:
        result.insert("end","7")
                            
def six():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","6")
    else:
        result.insert("end","6")
                            
def five():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","5")
    else:
        result.insert("end","5")
                            
def four():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","4")
    else:
        result.insert("end","4")
                            
                            
def three():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","3")
    else:
        result.insert("end","3")
                            
def two():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","2")
    else:
        result.insert("end","2")
                            
                            
def one():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","1")
    else:
        result.insert("end","1")
                            
                            
def zero():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","0")
    else:
        result.insert("end","0")
                            
def plus():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","+")
    else:
        result.insert("end","+")
                            
                            
def minus():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","-")
    else:
        result.insert("end","-")
                            
def multiply():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","*")
    else:
        result.insert("end","*")
                            
def divide():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","/")
    else:
        result.insert("end","/")
                            
def equal():
    if result.get() == "":
        result.insert("end","Error")
    elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get()[0] == "/":
        result.delete(0,"end")
        result.insert("end","Error")
    elif 'Error' in result.get() or '=' in result.get():
        result.delete(0,"end")
                            
                            
    else: 
        res = result.get()
        res = eval(res)
        result.insert("end","=")
        result.insert("end",res)
                            
def clear():
        result.delete(0,"end")
        

def Send():
        root = tk.Tk()
        root.geometry('300x400')
        root['bg'] = "white"
                    
        frame4 = Frame(root, width=300, height=60, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
        frame4.place(x=0,y=0)
                            
        l2 = Label(frame4, text = "Send Bill", font=('roboto',22,'bold'), bg='#248aa2', fg="#ffffff")
        l2.place(x=85,y=1)
                            
        frame5 = Frame(root, width=300, height=340, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
        frame5.place(x=0,y=55)
                        
        innerframe5 = Frame(frame5,width=285, height=325, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
        innerframe5.place(x=0,y=0)
                            
        l3 = LabelFrame(innerframe5, text="Send Bill Through SMS", width=270,height=310, borderwidth=3, font=('verdana',10,'bold'), fg='#248aa2',relief=RIDGE,highlightbackground= "white", highlightcolor="white", highlightthickness=1)
        l3.place(x=2,y=2)
                            
        l4 = Label(innerframe5, text="Phone Number", font=('verdana',10,'bold'))
        l4.place(x=40,y=40)
                            
        number = Entry(innerframe5, width=30, borderwidth=2)
        number.place(x=40,y=70)
                      
        l5 = Label(innerframe5, text="Bill Details", font=('verdana',10,'bold'))
        l5.place(x=40,y=100)
                            
        b_detail = ScrolledText(innerframe5,width=23, height=7,relief=RIDGE, borderwidth=3)
        b_detail.place(x=40,y=130)
                        
        b_detail.insert(1.0,bill_details.get(1.0,END))
                            
        def send_bill():
            ph_number=number.get()
            messages = b_detail.get("1.0","end-1c")
                        
            if ph_number == "":
                messagebox.showerror("Error",'Please fill the phone number.')
            elif messages == "":
                messagebox.showerror("Error",'Bill details is empty.')
            else:
                url= "https://www.fast2sms.com/dashboard/dev-api"
                api = "pcCednFzbTMP3t8yNOURKv1iBWwmhElju5fZk9gGqLoADVr2HXCb5k3B4FvdMxU1EwpI0NKYVWOmzQo2"
                querystring = {"authorization":api, "sender_id":"FSTSMS", "message": messages, "language":"english","route":"p","numbers":ph_number}
                            
                headers ={"cache-control": "no-cache"}
                requests.request("GET", url, headers = headers, params=querystring)
                            
                messagebox.showinfo("Send SMS", 'Bill has been sent to your number successfully')
                            
        send_msg= Button(innerframe5, text="Send Bill", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'), bg= '#248aa2', fg="white", padx=20, command=send_bill)
        send_msg.place(x=100,y=255)
             
        root.mainloop()
                            
def exit():
    message = messagebox.askquestion('Notepad', "Do you want to exit the application?")
    if message =="yes":
        root.destroy()
    else:
        "return"
                            
def cleared_bills():
    lassi_qty.delete(0,"end")
    lassi.deselect()
    lassi_qty['state']="disabled"
                            
    coffee_qty.delete(0,"end")
    coffee.deselect()
    coffee_qty['state']="disabled"
                            
    tea_qty.delete(0,"end")
    tea.deselect()
    tea_qty['state']="disabled"
                            
    juice_qty.delete(0,"end")
    juice.deselect()
    juice_qty['state']="disabled"
                            
    shakes_qty.delete(0,"end")
    shakes.deselect()
    shakes_qty['state']="disabled"
                            
    milk_qty.delete(0,"end")
    milk.deselect()
    milk_qty['state']="disabled"
                            
    iced_tea_qty.delete(0,"end")
    iced_tea.deselect()
    iced_tea_qty['state']="disabled"
                            
    roti_qty.delete(0,"end")
    roti.deselect()
    roti_qty['state']="disabled"
                            
    dal_makhani_qty.delete(0,"end")
    dal_makhani.deselect()
    dal_makhani_qty['state']="disabled"
                            
                            
    matar_paneer_qty.delete(0,"end")
    matar_paneer.deselect()
    matar_paneer_qty['state']="disabled"
                            
    paneer_parantha_qty.delete(0,"end")
    paneer_parantha.deselect()
    paneer_parantha_qty['state']="disabled"
                            
    mix_veg_qty.delete(0,"end")
    mix_veg.deselect()
    mix_veg_qty['state']="disabled"
                            
    plain_rice_qty.delete(0,"end")
    plain_rice.deselect()
    plain_rice_qty['state']="disabled"
                            
    drinks_cost.delete(0,"end")
    foods_cost.delete(0,"end")
    service_charge.delete(0,"end")
    paid_tax.delete(0,"end")
    sub_total.delete(0,"end")
    total_cost_cost.delete(0,"end")
                            
    bill_details.delete(1.0,"end")
                            
#===== Main Window Code =====
root= tk.Tk()
root.geometry('650x400')
root.maxsize(650,390)
root.minsize(650,390)
root.title("Restaurant Management System")
                            
frame = Frame(root,width=650, height=70, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame.place(x=0,y=0)
                            
l1=Label(frame,text="Restaurant Management System", font=('roboto',30,'bold'),bg='#248aa2', fg="black")
l1.place(x=10,y=4)
                            
frame1= Frame(root, width=450, height=230, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame1.place(x=0,y=70)
                            
innerframe1= Frame(frame1, width=200, height=220, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
innerframe1.place(x=0,y=0)
                            
drinks = LabelFrame(innerframe1,text="Drinks", width=185,height=205, borderwidth=3, font=('verdana',10,'bold'), fg='#248aa2',relief=RIDGE,highlightbackground= "white", highlightcolor="white", highlightthickness=1 )
drinks.place(x=2,y=2)
                            
                    
lassi_var = IntVar()
lassi= tk.Checkbutton(drinks, text="Lassi Rs.50",variable= lassi_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=lassi_chk)
lassi.place(x=2,y=2)                          
lassi_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
lassi_qty.place(x=120,y=2)
lassi_qty.insert(0,"0")
                            
coffee_var = IntVar()
coffee= tk.Checkbutton(drinks, text="Coffee Rs.25",variable= coffee_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=coffee_chk)
coffee.place(x=2,y=22)
coffee_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
coffee_qty.place(x=120,y=22)
                            
tea_var= IntVar()
tea= tk.Checkbutton(drinks, text="Tea Rs.15",variable= tea_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=tea_chk)
tea.place(x=2,y=44)
tea_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
tea_qty.place(x=120,y=44)
                           
juice_var= IntVar()
juice= tk.Checkbutton(drinks, text="Juice Rs.30",variable= juice_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=juice_chk)
juice.place(x=2,y=66)
juice_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
juice_qty.place(x=120,y=66)
                            
shakes_var= IntVar()
shakes= tk.Checkbutton(drinks, text="Shakes Rs.50",variable= shakes_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
shakes_qty.place(x=120,y=88)
                            
milk_var= IntVar()
milk= tk.Checkbutton(drinks, text="Milk Rs.20",variable= milk_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=milk_chk)
milk.place(x=2,y=110)
milk_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
milk_qty.place(x=120,y=110)
                            
iced_tea_var= IntVar()
iced_tea= tk.Checkbutton(drinks, text="IcedTea Rs.15",variable= iced_tea_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=iced_tea_chk)
iced_tea.place(x=2,y=132)
iced_tea_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
iced_tea_qty.place(x=120,y=132)
                            
innerframe2 = Frame(frame1, width=255, height=220, relief=RIDGE, borderwidth=3,bg='#248aa2', highlightbackground="white", highlightcolor= "white", highlightthickness=1)
innerframe2.place(x=185,y=0)
                            
foods= LabelFrame(innerframe2,text="Main Course", width=275,height=205, borderwidth=3, font=('verdana',10,'bold'), fg='#248aa2',relief=RIDGE,highlightbackground= "white", highlightcolor="white", highlightthickness=1 )
foods.place(x=2,y=2)
                            
roti_var= IntVar()
roti= tk.Checkbutton(foods, text="Roti Rs.10",variable= roti_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=roti_chk)
roti.place(x=2,y=2)
roti_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
roti_qty.place(x=180,y=2)
                        
dal_makhani_var= IntVar()
dal_makhani= tk.Checkbutton(foods, text="Dal Makhani Rs.120",variable= dal_makhani_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=dal_makhani_chk)
dal_makhani.place(x=2,y=22)
dal_makhani_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
dal_makhani_qty.place(x=180,y=22)
                            
matar_paneer_var= IntVar()
matar_paneer= tk.Checkbutton(foods, text="Matar Paneer Rs.180",variable= matar_paneer_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=matar_paneer_chk)
matar_paneer.place(x=2,y=44)
matar_paneer_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
matar_paneer_qty.place(x=180,y=44)
                            
paneer_parantha_var= IntVar()
paneer_parantha= tk.Checkbutton(foods, text="Paneer Parantha Rs.50",variable= paneer_parantha_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=paneer_parantha_chk)
paneer_parantha.place(x=2,y=66)
paneer_parantha_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
paneer_parantha_qty.place(x=180,y=66)
                            
mix_veg_var= IntVar()
mix_veg= tk.Checkbutton(foods, text="Mix Veg Rs.80",variable= mix_veg_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=mix_veg_chk)
mix_veg.place(x=2,y=88)
mix_veg_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
mix_veg_qty.place(x=180,y=88)
                            
plain_rice_var= IntVar()
plain_rice= tk.Checkbutton(foods, text="Plain Rice Rs.100",variable= plain_rice_var, font= ('verdana',8,'bold'), onvalue=1, offvalue=0, command=plain_rice_chk)
plain_rice.place(x=2,y=110)
plain_rice_qty = Entry(foods, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
plain_rice_qty.place(x=180,y=110)
                            
                            
frame2 = Frame(root, width=450, height=90, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame2.place(x=0,y=300)
                            
innerframe3= Frame(frame2, width=440, height=80, relief=RIDGE, borderwidth=3, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
innerframe3.place(x=0,y=0)   
                            
cost_of_drinks = Label(innerframe3, text="Cost of Drinks", font=('verdana',8,'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN, validatecommand = drinks_cost)
drinks_cost.place(x=130,y=0)
                            
cost_of_foods = Label(innerframe3, text="Cost of Foods", font=('verdana',8,'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN,)
foods_cost.place(x=130,y=22)
                            
service_charge = Label(innerframe3, text="Service Charge", font=('verdana',8,'bold'))
service_charge.place(x=2,y=46)
service_charge = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
service_charge.place(x=130,y=44)    
                            
paid_tax = Label(innerframe3, text="Paid Tax", font=('verdana',8,'bold'))
paid_tax.place(x=250,y=2)
paid_tax  = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
paid_tax.place(x=330,y=0) 
                            
sub_total = Label(innerframe3, text="Sub Total", font=('verdana',8,'bold'))
sub_total.place(x=250,y=24)
sub_total = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
sub_total.place(x=330,y=22) 
                            
total_cost = Label(innerframe3, text="Total Cost", font=('verdana',8,'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
total_cost_cost.place(x=330,y=44) 
                            

frame3 = Frame(root, width=200, height=320, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame3.place(x=450,y=70)
                            
innerframe4= Frame(frame3, width=185, height=310, relief=RIDGE, borderwidth=3, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=1)
innerframe4.place(x=1,y=0) 
                            
result=Entry(innerframe4,width=28, relief=SUNKEN, borderwidth = 3)
result.place(x=2,y=0)
                            
nine = Button(innerframe4, text="9", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=nine)
nine.place(x=0,y=24)
eight = Button(innerframe4, text="8", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=eight)
eight.place(x=48,y=24)
seven = Button(innerframe4, text="7", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=seven)
seven.place(x=96,y=24) 
plus = Button(innerframe4, text="+", padx = 5, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='white', fg="#248aa2", command=plus)
plus.place(x=144,y=24)
                            
six = Button(innerframe4, text="6", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=six)
six.place(x=0,y=50)                        
five = Button(innerframe4, text="5", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=five)
five.place(x=48,y=50)  
four = Button(innerframe4, text="4", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=four)
four.place(x=96,y=50)
minus = Button(innerframe4, text="-", padx = 7, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='white', fg="#248aa2", command=minus)
minus.place(x=144,y=50)
                            
three = Button(innerframe4, text="3", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=three)
three.place(x=0,y=76)
two = Button(innerframe4, text="2", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=two)
two.place(x=48,y=76)
one = Button(innerframe4, text="1", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=one)
one.place(x=96,y=76)
multiply = Button(innerframe4, text="*", padx = 6, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='white', fg="#248aa2", command=multiply)
multiply.place(x=144,y=76)  
                            
zero = Button(innerframe4, text="0", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=zero)
zero.place(x=0,y=102)
clear = Button(innerframe4, text="C", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=clear)
clear.place(x=48,y=102)
equal = Button(innerframe4, text="=", padx = 15, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='#248aa2', fg="white", command=equal)
equal.place(x=96,y=102)
divide = Button(innerframe4, text="/", padx = 6, relief=RAISED, borderwidth=2, font=('verdana',10,'bold'),bg='white', fg="#248aa2", command=divide)
divide.place(x=144,y=102)    
                            
bill_details = ScrolledText(innerframe4, width=22, height=9, relief=SUNKEN, borderwidth=3, font=('courier',9,'bold'))
bill_details.place(x=0,y=130)
                            
total = Button(innerframe4, text="Total", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'),bg='#248aa2', fg="white", command=total_bills)  
total.place(x=0,y=280)
                            
save = Button(innerframe4, text="Save", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'),bg='#248aa2', fg="white", command=save)  
save.place(x=43,y=280)
                            
send = Button(innerframe4, text="Send", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'),bg='#248aa2', fg="white", command=Send)  
send.place(x=82,y=280)
                            
exit = Button(innerframe4, text="Exit", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'),bg='#248aa2', fg="white", command=exit)  
exit.place(x=124,y=280)
                            
clr = Button(innerframe4, text="C", relief=RAISED, borderwidth=2, font=('verdana',8,'bold'),bg='#248aa2', fg="white", command=cleared_bills)  
clr.place(x=160,y=280)
                            
root.mainloop()                            


# In[ ]:




