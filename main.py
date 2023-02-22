"""
 ***************************************************************************************************
 * @file   main.py
 * @author Menkhet Team
 * @brief Implementation for Menkhet Clothing Manufacturer Chatbot application
 ***************************************************************************************************
 """

""" Imports ---------------------------------------------------------------------------------------"""
import time
from tkinter import *
from tkinter import colorchooser
import smtplib
from email.mime.text import MIMEText
import random
import json
from dotenv import load_dotenv
import os

""" Public and private data ------------------------------------------------------------------------"""

"""
 * @brief 
 * @param 
 * @retval 
 * @req/@task
 """

def get_orderid():
    # Provides an order ID that is not taken
    j = 0
    while j == 0:
        order_list = []
        order_id = random.randint(1000,5000)
        with open("orders.json", "r") as f:
            data = json.load(f)

        for key,val in data.items():
            for i in val:
                for key2,val2 in i.items():
                    if key2 == 'order_id':
                        order_list.append(val2)
        for i in order_list:
            if order_id == i:
                break            
            else:
                j = 1 
    return order_id

def add_details(details):
    with open("orders.json", "r") as file:
        data = json.load(file)
    data['customers'].append(details)

    with open("orders.json", "w") as outfile:
        json.dump(data, outfile)

def ask_name():
    return("Now we need your details! What is your name?")

def ask_email():
    return("What is your email? You will receive shipping updates on your email")

def ask_num():
    return("What is your phone number? We need it to contact you for delivery.")


def shipping(name,email,phone_no):
    order_id = get_orderid()

    details = dict(name = name, phone_no = phone_no, email = email, order_id = order_id)
    add_details(details)
    return order_id

def wholesale_size(product_name):
    while True:

        size = int(input("""
Which size do you want? Choose a number: 
    1) Small
    2) Medium
    3) Large
    4) View size chart\n"""))
        if size == 1:
            wholesale_quantity = int(input("How many do you want? Enter an integer:\n"))
            cart_order.append(f"x{wholesale_quantity} {product_name} | Small")
            break

        elif size == 2:
            wholesale_quantity = int(input("How many do you want? Enter an integer:\n"))
            cart_order.append(f"x{wholesale_quantity} {product_name} | Medium")
            break

        elif size == 3:
            wholesale_quantity = int(input("How many do you want? Enter an integer:\n"))
            cart_order.append(f"x{wholesale_quantity} {product_name} | Large")
            break

        elif size == 4:
            size_chart()
            time.sleep(3)
            continue
        
        else: continue

def wholesale_order():
    while True:
        global cart_price
        product = int(input("""
Which product do you want? Choose a number: 
    1) T-Shirts
    2) Hoodies
    3) Knitwear
    4) Jackets
    5) Pants\n"""))

        # Ordering T-Shirts
        if product == 1:
            tshirt = int(input(f"""
We currently have 2 T-Shirts in stock. Which one do you want to add to the cart? Choose a number: 
    1) Oversized T-Shirt (White) - {tshirtprice} EGP
    2) Standard Fit T-Shirt (Black) - {tshirtprice} EGP\n"""))
            if tshirt == 1:
                wholesale_size("Oversized T-Shirt (White)")
                cart_price += tshirtprice
            elif tshirt == 2:
                wholesale_size("Standard Fit T-Shirt (Black)")
                cart_price += tshirtprice
            else: continue

        # Ordering Hoodies
        elif product == 2:
            hoodies = int(input(f"""
We currently have 1 Hoodies in stock. Which one do you want to add to the cart? Choose a number: 
    1) Oversized Hoodie (White) - {hoodieprice} EGP\n"""))
            if hoodies == 1:
                wholesale_size("Oversized Hoodie (White)")
                cart_price += hoodieprice
            else: continue

        # Ordering Knitwear
        elif product == 3:
            knitwear = int(input(f"""
We currently have 1 Sweater in stock. Which one do you want to add to the cart? Choose a number: 
    1) Sweater (Blue) - {knitwearprice} EGP\n"""))
            if knitwear == 1:
                wholesale_size("Sweater (Blue)")
                cart_price += knitwearprice
            else: continue

        # Ordering Jackets
        elif product == 4:
            jackets = int(input(f"""
We currently have 1 Jacket in stock. Which one do you want to add to the cart? Choose a number: 
    1) Jacket (Black) - {jacketprice} EGP\n"""))
            if jackets == 1:
                wholesale_size("Jacket (White)")
                cart_price += jacketprice
            else: continue

        #Ordering Pants
        elif product == 5:
            pants = int(input(f"""
We currently have 3 Pants in stock. Which one do you want to add to the cart? Choose a number: 
    1) Sweatpants (Black) - {pantsprice} EGP
    2) Cargo pants (Grey) - {pantsprice} EGP
    3) Jeans (Blue) - {pantsprice} EGP\n"""))
            if pants == 1:
                wholesale_size("Sweatpants (Black)")
                cart_price += pantsprice
            elif pants == 2:
                wholesale_size("Cargo pants (Grey)")
                cart_price += pantsprice
            elif pants == 3:
                wholesale_size("Jeans (Blue)")
                cart_price += pantsprice
            else: continue


        else: continue

        # Asking for another product
        another = int(input("""
Do you want to add another product? Choose a number:
    1) Yes
    2) No\n"""))
        if another == 2:
        
        # Displaying cart
            print(f"""
Total price will be {cart_price} EGP
This is your cart: """)
            break

def show_products():
    return("""Which product do you want? Choose a number: 
    1) T-Shirt
    2) Hoodies
    3) Knitwear
    4) Jackets
    5) Cargo pants
    6) Sweatpants
    7) Jeans
    8) Trousers""")

def user_product(prod):
    global product
    product = prod

def ask_order():
    return("We need your order ID in order to track your shipment.")

def track_shipment():
    time=["Your order is currently pending confirmation!","Your order was confirmed, manufacturing will begin shortly!","Your order is out for delivery!","Your order is currently being manufactured, you will be contacted once its ready to be shipped!"]
    x= random.randint(0,3)
    status= time[x]
    
    return status

def check_orderid(order_id):
    order_list = []
    with open("orders.json", "r") as f:
        data = json.load(f)

    for key,val in data.items():
        for i in val:
            for key2,val2 in i.items():
                if key2 == 'order_id':
                    order_list.append(val2)
    try:
        for i in order_list:
            if int(order_id) == i:
                return True
    except:
        return False
    
    return False

def ask_quant(sizes):
    return(f"How many {sizes.upper()} each do you want? Enter the numbers in order seperated by spaces i.e 150 100 200: ")

def show_customer():
    return ("""Great! Lets get started with your order. We need to know what you want. Choose a number:
    1) Wholesale (TO BE IMPLEMENTED)
    2) Fully Factored Manufacturing""")

def size_chart():
    pass

def show_sizes():
    return("Please enter your size separation from XS-XXL, separated by space ie.(XS S M L): ")

def show_fit(product):
    if product == '1':
        return("""Please select your fit type:
        1) Standard
        2) Oversized
        3) Slim""")

    if product == '2':
        return("""Please select your fit type: 
        1) Standard
        2) Oversized
        3) Baggy""")

    if product == '3':
        return("""Please select your fit type: 
        1) Standard
        2) Oversized
        3) Slim""")

    if product == '4':
        return("""Please select your fit type:
        1) Puffer""")
    
    if product == '5' or product == '6' or product == '7' or product == '8':
        return("""Please select your fit type:
        1) Straight
        2) Baggy
        3) Slim""")

def show_pic():
    return(Image.open("sizechart_US_men.jpg"))


# TO BE ADDED IN (SHOWING PICTURES OF FITS)  
  
# def picture_fit(product):

#     # TSHIRT FIT
#     if product == 1:

#                 urllib.request.urlretrieve(
#                     'https://lh3.googleusercontent.com/Moac725q6YIBjWDtwDAoWpW9uxpl8Gs6_Gu4j3kXU8DgnGjiIRQCfyNpEwae7uVFCfE=w2400',
#                     "str8")
#                 fit_img = Image.open("str8")
#                 fit_img.show()

#                 urllib.request.urlretrieve(
#                     'https://lh6.googleusercontent.com/wkLbd3H13ZvJlUmY1U5VElWM6dCKpSWnymAYyGop_bNXfrRJdy4foI7TaX6E7QV4lRk=w2400',
#                     "oversized")
#                 fit_img = Image.open("oversized")
#                 fit_img.show()

#                 urllib.request.urlretrieve(
#                     'https://lh5.googleusercontent.com/-cGpSCVXTubeXLK_iug90hyP47sPhAdPIFVaoYT2WUu-Iy8m_UMcI_tGbFIqOn6wPPA=w2400',
#                     "slim")
#                 fit_img = Image.open("slim")
#                 fit_img.show()


#     # HOODIE FIT
#     elif product == 2:
#                 urllib.request.urlretrieve(
#                     'https://lh5.googleusercontent.com/lprGKkwSyhJkr9NxLPQdhiyUaxWdv89W1rc_jDtfQewAWmeWer9iK0h6BgBs5pPYzZs=w2400',
#                     "standered")
#                 fit_img = Image.open("standered")
#                 fit_img.show()

#                 urllib.request.urlretrieve(
#                     'https://lh5.googleusercontent.com/ZGaJ38cfJein6VwUwWgyQEDI3077DKBDrDo-9TQwDtkRDDyCXQzZYPUOGLlhFRJdcTw=w2400',
#                     "oversized")
#                 fit_img = Image.open("oversized")
#                 fit_img.show()

#                 urllib.request.urlretrieve(
#                     'https://lh6.googleusercontent.com/A_sYh0w00ggpder5OgxDRhFmDe7mwqSqjnISv5a10HPHndoNxfYVJ3LIPccQqv1wChI=w2400',
#                     "baggy")
#                 fit_img = Image.open("baggy")
#                 fit_img.show()
#                 cyn = input("Would you like to view another fit type (Yes or No)? ").lower()


#     # KNITWEAR FIT
#     elif product == 3:


#                 urllib.request.urlretrieve(
#                     'https://lh4.googleusercontent.com/mzU0QVkJ_X-3Pf1VnCKXkEphAf5RDdVln5PnKuDylFJJceCKReEKUPYOIBYMmOHm5wU=w2400',
#                     "Standard")
#                 fit_img = Image.open("Standard")
#                 fit_img.show()

#                 urllib.request.urlretrieve(
#                     'https://lh6.googleusercontent.com/WhLQuv-aKwJVU_ZNAuhj_wp2QlXRgcbJuTk_IYXbwQt8xf7YsDb-vOoiN1zsKgNb_Uo=w2400',
#                     "oversized")
#                 fit_img = Image.open("oversized")
#                 fit_img.show()


#     # JACKETS FIT
#     elif product == 4:

#         urllib.request.urlretrieve(
#             'https://lh4.googleusercontent.com/rYFuJFJyG_csCn7N5f4BQtzmM0xbWOux_Ix4hiCwU0i-SaK3KBajHSfo7sYsE6gbgiI=w2400',
#             "puffer")
#         fit_img = Image.open("puffer")
#         fit_img.show()

#     # PANTS FIT
#     elif product == 5:

#                 if 'cargo' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/xxTkMNhQF7-vnnwwVX6GLx30wWJTBI7SHohsHFPQj2RGmJgfbfHbWiMnKGWoWGlSDOg=w2400',
#                         "cargo straight")
#                     fit_img = Image.open("cargo straight")
#                     fit_img.show()

#                 elif 'jean' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/VOGpRkEv_nMoYi9F7FHnZi3SWkWS64iIDvAyCJVHSHgCuM5KG6dl8_yqQ1kE9XsOqV4=w2400',
#                         "jeans straight")
#                     fit_img = Image.open("jeans straight")
#                     fit_img.show()

#                 elif 'trousers' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh5.googleusercontent.com/6tqwIOX351S9Nr9tMe_JO1Lb7q-IDVEAwRl76BqA6Ffp8UJBpCjfIWWA-wiyaO8NN9g=w2400',
#                         "trousers straight")
#                     fit_img = Image.open("trousers straight")
#                     fit_img.show()

#                 elif 'sweatpants' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh5.googleusercontent.com/AMAoJEmbonwIdsmx9uqL165i2GY-Kc7pUT1XzHPBl3M7aLPs8t_U-2beqchQXH54Fso=w2400',
#                         "sweatpants straight")
#                     fit_img = Image.open("sweatpants straight")
#                     fit_img.show()


#             elif "baggy" in fit.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/ttTFLVsQ4lXWcfhYefmo1s-Czt1tR8cRDGCk83Npn5v3f_Tdhhr7KUZ-7VKo8QaXgko=w2400',
#                         "cargo baggy")
#                     fit_img = Image.open("cargo baggy")
#                     fit_img.show()

#                 elif 'jean' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh4.googleusercontent.com/EyJilegrOBFTcNcAhOBF4LFQXEzCg1yQushMVaLr0lrop0E3qO-9W80Ill2SDmvoB3Q=w2400',
#                         "jeans baggy")
#                     fit_img = Image.open("jeans baggy")
#                     fit_img.show()

#                 elif 'trousers' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/N_aDnFqsI0_MB6qi82YlYg_Jx97A-09n5iF4mAsRbpHF2sqhSnDwfbVFwXFMo9pTkL0=w2400',
#                         "trousers baggy")
#                     fit_img = Image.open("trousers baggy")
#                     fit_img.show()

#                 elif 'sweatpants' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/Ewwt_XN1ywCBYOh7a6n9usaqoPBIh9Gjt0meC83o3FMSPwaGqWtYVmypSrJSOtxpORU=w2400',
#                         "sweatpants baggy")
#                     fit_img = Image.open("sweatpants baggy")
#                     fit_img.show()

#             elif "slim" in fit.lower():
#                 if 'cargo' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh6.googleusercontent.com/n_aK6MRJj-gixTpKUEFFBaYk4ZRAm9McOB-8zOyom7U3tVPwRa9RqLpouotyx6WK6ww=w2400',
#                         "cargo slim")
#                     fit_img = Image.open("cargo slim")
#                     fit_img.show()

#                 elif 'jean' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh3.googleusercontent.com/7FPbyIdfrVIgyCpLQ27qrZCeCOAWNCyHz1nBJY72AN_1gSfZg4mduY7zQN3N5nJ_8Ew=w2400',
#                         "jeans slim")
#                     fit_img = Image.open("jeans slim")
#                     fit_img.show()
#                 elif 'trousers' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh3.googleusercontent.com/szpkllAmRyxIr7fDZNuGJ3mLrXmE8G4mxGgPEjJkHtXqBJGigeHtpLQnW6YUtTdJm1c=w2400',
#                         "trousers slim")
#                     fit_img = Image.open("trousers slim")
#                     fit_img.show()
#                 elif 'sweatpants' in pants_typ.lower():
#                     urllib.request.urlretrieve(
#                         'https://lh5.googleusercontent.com/6kG-EXS9IGrFFViHLRa2yCsgojSK40q5boMC8a9Z8fofZPMqmiVMrVfqxPD0rxXF9zk=w2400',
#                         "sweatpants slim")
#                     fit_img = Image.open("sweatpants slim")
#                     fit_img.show()


def show_material(product):
    if product == '1':
        return("""What material would you like to use for your t-shirts? 
    1) Barasola
    2) Pique
    3) Summer Melton
    4) Single Lycra""")

    elif product == '2':
        return("""What material would you like to use for your hoodies?
    1) Summer Melton
    2) Melton""")

    elif product == '3':
        return("""What material would you like to use for your hoodies?
    1) Cotton Twill
    2) Linen
    3) Cotton Gabardine""")

    elif product == '4':
        return("""What material would you like to use for your jackets?
    1) Summer Melton
    2) Melton
    3) Baize""")

    elif product == '5':
        return("""What material would you like to use for your pants?
        1) Summer Melton
        2) Melton
        3) Gabardine""")

    elif product == '6':
        return("""What material would you like to use for your pants?
    1) Summer Melton
    2) Melton
    3) Gabardine""")

    elif product == '7':
        return("""What type would you like to use for your jeans?
    1) 100% cotton Denim
    2) Sanforized Denim
    3) Raw denim""")

    elif product == '8':
        return("""Please choose the material for your desired trousers
    1) Cotton Twill
    2) Linen
    3) Recycled Wool""")

def show_blend():
    return ("""There are differnt options for fabrcic blends; these are the blends available:
    1) 100% cotton (The fabric shrinkage is 1%-3%)
    2) 65% cotton 35% polyster (The fabric shrinkage is 2%-4%)
    3) 50% cotton 50% polyster (The fabric shrinkage is 3%-5%)""")

def color():
    p_color= colorchooser.askcolor()[1]
    return p_color

def customer_issue():
    return("Please tell us your issue: ")

def customer_name():
    return("We will be opening a ticket for you. First of all, what is your name?")

def customer_email():
    return("What is your email? We will send you a confirmation email and your ticket ID.")

def sendEmail(name,email,issue):
    load_dotenv()
    e_email = os.environ.get("EMAIL")
    e_pw = os.environ.get("PW")
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = e_email
    password = e_pw
    sender = e_email
    targets = [email]

    msg = MIMEText(f'''
Hello {name},

    Thank you for contacting Menkhet Support Team. Your ticket ID is {random.randint(100,500)} This is your issue:

    "{issue}"

    We will get back to you as soon as possible.
        
Best Regards,
Menkhet Support Team''')
    msg['Subject'] = 'Menkhet Support team'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()


# Cart
cart_price = 0
cart_order = [" "]

# Prices
tshirtprice = 300
hoodieprice = 500
jacketprice = 450
pantsprice = 300
knitwearprice = 450

"""
 * Start of code execution
 """

# Welcome message and initial options

start = """Welcome to Menkhet!
My name is Gaafar and I will be assisting you.
How can I help you today? Choose a number: 
    1) Make an order
    2) Track my shipment
    3) Contact customer support
    4) View size chart"""

another_product = """Which product do you want? Choose a number: 
    1) T-Shirt
    2) Hoodies
    3) Knitwear
    4) Jackets
    5) Cargo pants
    6) Sweatpants
    7) Jeans
    8) Trousers"""

help = """How can I help you? Choose a number: 
    1) Make an order
    2) Get a quote
    3) Track my shipment
    4) Contact customer support
    5) View size chart"""



""" End of file --------------------------------------------------------------------------------"""