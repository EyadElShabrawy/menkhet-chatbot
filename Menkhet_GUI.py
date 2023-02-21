# Import everything inside the Tkinter library
from tkinter import *
from tkinter.scrolledtext import *
import main as bot

# Create the main class of you application (the blueprint)
class menkhet_gui:
    # Start defining your methods to deal with this class and further instances
    
    # Start with defining the "__init__" method, create windows and call methods inside
    def __init__(self):
        # Start by creating your first window
        self.window = Tk()

        # Call any additional methods you created that shall affect your window
        self.custom_window()
        self.widgets()

    # Second create your "run" function, where you will maintain your mainloop of the GUI application    
    def run(self):
        
        # Call the "mainloop" method of your created window
        self.window.mainloop()

    # Define additional methods tailored for your GUI
    # This method is for customizing how our window will look like, we have to call this method 
    #           inside "__init__" method in order for the function to have effect.
    def custom_window(self):

        # Set the title of the window
        self.window.title("Menkhet Chatbot")
        # Set the geometry (width, hight, padding x, padding y) of the window
        self.window.geometry('800x800+50+50')
        # State if the window is resizable with respect to width and height
        self.window.resizable(False,False)
        # Control opacity of the window
        self.window.attributes('-alpha',1)

        #self.window.iconbitmap('./myicon.ico')

        # Set the background of the window (can do more!!)
        self.window.configure(bg="black")
        

    # This method is for adding widgets to your window, we have to call this method inside 
    #           "__init__" method in order for the function to have effect.
    def widgets(self):
        
        # First label widget
        main_label = Label(self.window, bg = "white", fg="green", text="🟩 You are currently talking to our chatbot!", font="Calibri", padx="10", pady="5")
        main_label.place(relwidth=1)


        # First text widget
        self.scrollbar = ScrolledText(self.window, height='10', width='45', wrap=WORD)
        self.text_widget = Text(self.window, width= 29, height = 2, bg="white", fg = "black",font="Calibri",padx=6,pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)



        # First entry widget
        self.msg_entry = Entry(self.window, bg="cyan", fg="black", font="Calibri")
        self.msg_entry.place(relwidth=0.75, relheight=0.06, x=0, y=700)
        self.msg_entry.focus()
        self.msg_entry.delete(0, END)
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Button Widget
        send_button = Button(self.window, text="Send", font="Calibri", width=20, bg="Grey", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, y=700, relheight=0.06, relwidth=0.22)

    previous_selections = []
    def _on_enter_pressed(self, event):
        global user_msg
        user_msg = self.msg_entry.get()
        self._insert_message(user_msg,"You")
        if not self.previous_selections:
            self.bot_message(bot.start)
            self.previous_selections.append("Main message")

        # User chose from main message
        elif len(self.previous_selections) == 1:
            if self.validate(1,4,user_msg) == True:
                self.previous_selections.append(user_msg)

                # User chose make an order
                if self.previous_selections[1] == '1':
                    self.bot_message(bot.show_customer())
                    self.previous_selections.append("Ask type")

                # User chose track shipment
                elif self.previous_selections[1] == '2':
                    self.bot_message("Please let me know your order ID.")
                    self.previous_selections.append("order id")

                # User chose customer support
                elif self.previous_selections[1] == '3':
                    self.previous_selections.append("Name")
                    self.bot_message(bot.customer_name())

                # User chose size chart
                elif self.previous_selections[1] == '4':
                    self.previous_selections.append("size chart")
                    self.bot_message(bot.another_product)

            else: self.bot_message(self.wrong())
            
        
        elif len(self.previous_selections) == 3:
            # Make an order
            if self.previous_selections[2] == 'Ask type':
                if self.validate(1,2,user_msg) == True:
                    self.previous_selections.append(user_msg)
                    if self.previous_selections[3] == '2':
                        self.bot_message(bot.show_products())
                        self.previous_selections.append("Products shown")
                else: self.bot_message(self.wrong())

            # Customer Support
            elif self.previous_selections[2] == 'Name':
                self.bot_message(bot.customer_email())
                self.previous_selections.append(user_msg)
                self.previous_selections.append("Email")

            # Track Shipment
            elif self.previous_selections[2] == 'order id':
                if bot.check_orderid(user_msg):
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.track_shipment())
                else: self.bot_message("Wrong Order ID, please enter a correct one!")

            # Size Chart
            elif self.previous_selections[2] == 'size chart':
                if self.validate(1,8,user_msg):
                    self.previous_selections.append(user_msg)
                    self.previous_selections.append("ask fit")
                    self.bot_message(bot.show_fit(user_msg))
                else: self.wrong()
        
        elif len(self.previous_selections) == 5:
            # Make an order
            if self.previous_selections[4] == "Products shown":
                if self.validate(1,8,user_msg) == True:
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.show_material(user_msg))
                    self.previous_selections.append("Material shown")
                else: self.bot_message(self.wrong())

            # Customer Support
            elif self.previous_selections[4] == "Email":
                self.bot_message(bot.customer_issue())
                self.previous_selections.append(user_msg)
                self.previous_selections.append("Issue")

            # Size Chart
            elif self.previous_selections[4] == 'ask fit':
                if self.previous_selections[3] == '4':
                    if self.validate(1,1,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[3],self.previous_selections[5]))
                    else: self.bot_message(self.wrong())
                elif self.previous_selections[3] == '3':
                    if self.validate(1,2,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[3],self.previous_selections[5]))
                    else: self.bot_message(self.wrong())
                else:
                    if self.validate(1,3,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[3],self.previous_selections[5]))
                    else: self.bot_message(self.wrong())


        elif len(self.previous_selections) == 7:
            # Make an order
            if self.previous_selections[6] == "Material shown":
                if self.previous_selections[5] == '1':
                    if self.validate(1,4,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.bot_message(bot.show_blend())
                        self.previous_selections.append("Blend shown")
                    else: self.bot_message(self.wrong())
                elif self.previous_selections[5] == '2':
                    if self.validate(1,2,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.bot_message(bot.show_blend())
                        self.previous_selections.append("Blend shown")
                    else: self.bot_message(self.wrong())

                elif self.previous_selections[5] == '8':
                    if self.validate(1,3,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        if user_msg == '1':
                            self.bot_message("Twill is versatile and its a common fabric for trousers. Its name comes from the weave used to create it the twill weave. This weave pattern creates diagonal lines across the face of the fabric. These lines can be very obvious or quite subtle, depending on the thread colors used. Twill is very strong, durable, and often mid to heavy in weight, making it perfect for trousers.")
                        elif user_msg == '2':
                            self.bot_message("Linen is a beautiful, sustainable fabric made from the stems of flax plants. This fabric is strong, long-lasting, and gets a more rustic, worn-in look with every wash and wear. Linen is a breathable fabric, making it perfect for summer trousers or everyday wear for hot climates.")
                        elif user_msg == '3':
                            self.bot_message("Wool is a long-lasting, hard-wearing fabric that can be made into durable pants for a variety of purposes from dress pants, to work pants, to cold weather trousers. Its a fabric that will hold up to years of heavy use and will keep you warm and cozy while out in the cold.")
                            
                        self.previous_selections.append("No blend")
                        self.bot_message("Would you like to continue? (Yes or No)")
                    else: self.bot_message(self.wrong())
                else:
                    if self.validate(1,3,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.bot_message(bot.show_blend())
                        self.previous_selections.append("Blend shown")
                    else: self.bot_message(self.wrong())

            # Customer Support
            elif self.previous_selections[6] == "Issue":
                self.previous_selections.append(user_msg)
                self.bot_message("Confirmation email was sent to you! Our support team will contact you ASAP!")
                bot.sendEmail(self.previous_selections[3],self.previous_selections[5],self.previous_selections[7])
                bot.time.sleep(3)
                self.bot_message("Do you need anything else? (Yes or No)")
                self.previous_selections.append("Anything else")

            # Size Chart
            elif self.previous_selections[6] == 'Chart shown':
                if 'y' in user_msg.lower() or "ready" in user_msg.lower():
                    self.new_selections = self.previous_selections.copy()
                    del self.previous_selections[1:]
                    self.bot_message(bot.help)
                elif 'n' in user_msg.lower():
                    self.bot_message("Take your time and tell me when you are ready...")
                else: self.bot_message(self.wrong())
        
        elif len(self.previous_selections) == 9:
            # Make an order process
            if self.previous_selections[8] == "Blend shown":
                if self.validate(1,3,user_msg) == True:
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.show_sizes())
                    self.previous_selections.append("Sizes shown")
                else: self.bot_message(self.wrong())
            elif self.previous_selections[8] == "No blend":
                if 'y' in user_msg.lower() or "ready" in user_msg.lower():
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.show_sizes())
                    self.previous_selections.append("Sizes shown")
                elif 'n' in user_msg.lower():
                    self.bot_message("Take your time and tell me when you are ready...")
                else:
                    self.bot_message(self.wrong())

            # Customer Support
            elif self.previous_selections[8] == "Anything else":
                if 'y' in user_msg.lower():
                    del self.previous_selections[1:]
                    self.bot_message(bot.help)


        elif len(self.previous_selections) == 11:
            # Make an order process
            if self.previous_selections[10] == "Sizes shown":
                if self.size_valid(user_msg,['XS', 'S', 'M', 'L', 'XL', 'XXl']) == True:
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.ask_quant(user_msg))
                    self.previous_selections.append("Asked quantity")
                else: self.bot_message(self.wrong())

        
        elif len(self.previous_selections) == 13:
            # Make an order process
            if self.previous_selections[12] == "Asked quantity":
                if self.quan_valid(user_msg) == True:
                    self.previous_selections.append(user_msg)
                    self.bot_message(bot.show_fit(self.previous_selections[5]))
                    self.previous_selections.append("Fit shown")
                else: self.bot_message(self.wrong())

        elif len(self.previous_selections) == 15:
            # Make an order process
            if self.previous_selections[14] == "Fit shown":
                if self.previous_selections[5] == '4':
                    if self.validate(1,1,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[5],self.previous_selections[15]))
                    else: self.bot_message(self.wrong())
                elif self.previous_selections[5] == '3':
                    if self.validate(1,2,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[5],self.previous_selections[15]))
                    else: self.bot_message(self.wrong())
                else:
                    if self.validate(1,3,user_msg) == True:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Chart shown")
                        self.bot_message("Would you like to continue? (Yes or No)")
                        self.bot_message(self.show_table(self.previous_selections[5],self.previous_selections[15]))
                    else: self.bot_message(self.wrong())
        
        elif len(self.previous_selections) == 17:
            # Make an order process
            if self.previous_selections[16] == "Chart shown":
                if 'y' in user_msg.lower() or "ready" in user_msg.lower():
                    if self.previous_selections[5] == '1' or self.previous_selections[5] == '2' or self.previous_selections[5] == '4':
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Logo asked")
                        self.bot_message("Would you like to add a logo? (Yes or No)")
                    else:
                        self.previous_selections.append(user_msg)
                        self.previous_selections.append("Asked color")
                        self.bot_message("Please choose a color for your product")
                        self.previous_selections.append(bot.color())
                        self.bot_message("Your order is now done! Do you want to add another product? (Yes or No)")
                        self.previous_selections.append("Another")
                elif 'n' in user_msg.lower():
                    self.bot_message("Take your time and tell me when you are ready...")
                else: self.bot_message(self.wrong())

        elif len(self.previous_selections) == 19:
            if self.previous_selections[18] == "Logo asked":
                if 'y' in user_msg.lower():
                    self.previous_selections.append(user_msg)
                    self.bot_message("Where would you like to position your logo (Right, Center, Left)")
                    self.previous_selections.append("Asked pos")
                elif 'n' in user_msg.lower():
                    self.previous_selections.append(user_msg)
                    self.previous_selections.append("Asked print")
                    self.bot_message("Would you like to add a print? (Yes or No)")
                else: self.bot_message(self.wrong())
        
        elif len(self.previous_selections) == 21:
            # Make an order process
            if self.previous_selections[20] == "Another":
                if 'y' in user_msg.lower():
                    self.new_selections = self.previous_selections.copy()
                    del self.previous_selections[5:]
                    self.bot_message(bot.another_product)
                elif 'n' in user_msg.lower():
                    self.previous_selections.append("Name")
                    self.bot_message(bot.ask_name())
                else: self.bot_message(self.wrong())

            elif self.previous_selections[20] == "Asked pos":
                if self.size_valid(user_msg,['RIGHT','CENTER','LEFT']):
                    self.previous_selections.append(user_msg)
                    self.previous_selections.append("Asked print")
                    self.bot_message("Would you like to add a print? (Yes or No)")
                else: self.bot_message(self.wrong())
            
            elif self.previous_selections[20] == "Asked print":
                if 'y' in user_msg.lower():
                    self.previous_selections.append(user_msg)
                    self.bot_message("Where would you like to position your print? (Front or Back)")
                    self.previous_selections.append("Asked print pos")
                elif 'n' in user_msg.lower():
                    print(self.previous_selections)
                    del self.previous_selections[18:]
                    print(self.previous_selections)
                    self.previous_selections.append("Asked color")
                    self.bot_message("Please choose a color for your product")
                    self.previous_selections.append(bot.color())
                    self.bot_message("Your order is now done! Do you want to add another product? (Yes or No)")
                    self.previous_selections.append("Another")
                else: self.bot_message(self.wrong())
        
        elif len(self.previous_selections) == 22:
            # Make an order process
            if self.previous_selections[21] == "Name":
                self.previous_selections.append(user_msg)
                self.previous_selections.append("Email")
                self.bot_message(bot.ask_email())
        
        elif len(self.previous_selections) == 23:
            if self.previous_selections[22] == "Asked print pos":
                if self.size_valid(user_msg,['FRONT','BACK']):
                    print(self.previous_selections)
                    del self.previous_selections[18:]
                    print(self.previous_selections)
                    self.previous_selections.append("Asked color")
                    self.bot_message("Please choose a color for your product")
                    self.previous_selections.append(bot.color())
                    self.bot_message("Your order is now done! Do you want to add another product? (Yes or No)")
                    self.previous_selections.append("Another")
                else: self.bot_message(self.wrong())
            elif self.previous_selections[22] == "Asked print":
                if 'y' in user_msg.lower():
                    self.previous_selections.append(user_msg)
                    self.bot_message("Where would you like to position your print? (Front or Back)")
                    self.previous_selections.append("Asked print pos")
                elif 'n' in user_msg.lower():
                    print(self.previous_selections)
                    del self.previous_selections[18:]
                    print(self.previous_selections)
                    self.previous_selections.append("Asked color")
                    self.bot_message("Please choose a color for your product")
                    self.previous_selections.append(bot.color())
                    self.bot_message("Your order is now done! Do you want to add another product? (Yes or No)")
                    self.previous_selections.append("Another")
                else: self.bot_message(self.wrong())


        elif len(self.previous_selections) == 24:
            # Make an order process
            if self.previous_selections[23] == "Email":
                self.previous_selections.append(user_msg)
                self.previous_selections.append("Phone")
                self.bot_message(bot.ask_num())

        elif len(self.previous_selections) == 25:
            if self.size_valid(user_msg,['FRONT','BACK']):
                print(self.previous_selections)
                del self.previous_selections[18:]
                print(self.previous_selections)
                self.previous_selections.append("Asked color")
                self.bot_message("Please choose a color for your product")
                self.previous_selections.append(bot.color())
                self.bot_message("Your order is now done! Do you want to add another product? (Yes or No)")
                self.previous_selections.append("Another")
            else: self.bot_message(self.wrong())

        elif len(self.previous_selections) == 26:
            # Make an order process
            if self.previous_selections[25] == "Phone":
                self.previous_selections.append(user_msg)
                self.previous_selections.append("Order ID")
                self.previous_selections.append(bot.shipping(self.previous_selections[22],self.previous_selections[24],self.previous_selections[26]))
                self.bot_message(f"""Your order is confirmed! Your order ID is {self.previous_selections[28]}
                You will be contacted once your order is ready!""")





    def validate(self,min,max,msg):
        try:
            if int(msg) < min or int(msg) > max:
                return False
            else: return True
        except:
            return False

    def size_valid(self,msg,range):

        user_lst = msg.upper().split()

        check = all(i in range for i in user_lst)

        if check is True:
            return True
        else: return False

    def quan_valid(self,msg):
        quan = msg.split()
        for i in quan:
            if i.isdigit() == False:
                return False
            else: return True
    
    def wrong(self):
        answers = ["I don't understand, please try again!", "Hmmm I can't understand what you are saying. Try again!", "Choose one of the options please!", "Oops, I don't understand. Try again?"]
        num = bot.random.randint(0,3)
        return answers[num]

    def show_table(self,product,fit):
        top= Toplevel(self.window)

        if product == '1' and fit == '1':
            name = "STANDARD FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Full-Chest", 34, 36, 38, 40, 42, 44],
                    ["Length", 24, 25, 26, 27, 28, 29],
                    ["Sleeve", 7.5, 8, 8, 8.5, 8.5, 9]]
            
        elif product == '1' and fit == '2':
            name = "OVERSIZED FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Full-Chest", 41, 43, 45, 47, 49, 51],
                    ["Length", 28.5, 29.5, 29.5, 30, 30, 32],
                    ["Sleeve", 7.75, 8.25, 8.5, 8.75, 9, 9.25]]
                        
                
        elif product == '1' and fit == '3':
            name = "SLIM FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Full-Chest", 33, 35, 37, 39, 41, 43],
                    ["Length", 23, 24, 25, 26, 27, 28],
                    ["Sleeve", 7.5, 8, 8, 8.5, 8.5, 9]]
                
        elif product == '2' and fit == '1':
            name = "STANDARD FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 20, 20.5, 21.5, 22, 23, 24],
                    ["Length", 27, 27.5, 28.5, 29.5, 30.5, 31.5],
                    ["Sleeve", 24.5, 25, 25.5, 26, 26.5, 27]]
                
        elif product == '2' and fit == '2':
            name = "OVERSIZED FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 21, 22, 22.5, 23, 24, 25],
                    ["Length", 28, 28.5, 29.5, 30.5, 31.5, 32.5],
                    ["Sleeve", 24.5, 25.1, 26, 26.5, 27, 27.5]]
               
        elif product == '2' and fit == '3':
            name = "BAGGY FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 22, 23, 24, 25, 26, 27],
                    ["Length", 28.5, 29, 30, 31, 32, 33],
                    ["Sleeve", 25, 25.5, 27, 27.5, 28, 28.5]]
                
        elif product == '3' and fit == '1':
            name = "STRAIGHT FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 19, 20, 21, 22, 23, 24],
                    ["Length", 27, 28.5, 29, 29.5, 30, 31],
                    ["Sleeve", 24.5, 25, 25.5, 26, 26.5, 27]]
            
        elif product == '3' and fit == '2':
            name = "OVERSIZED FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 20, 21, 22, 23, 24, 25],
                    ["Length", 28, 29.5, 30, 30.5, 31, 32],
                    ["Sleeve", 25, 25.5, 26, 26.5, 27, 27.5]]
                
        elif product == '4' and fit == '1':
            name = "PUFFER JACKET FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Half-Chest", 26.2, 27, 27.8, 28.5, 29.3, 30.2],
                    ["Length", 21.5, 22.5, 23.5, 24.5, 25.5, 26.5],
                    ["Sleeve", 29.5, 30.4, 31.2, 32, 33, 33.5]]
               
        elif product == '5' or product == '6' or product == '7' or product == '8' and fit == '1':
            name = "STRAIGHT FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Waist", '28 - 30', '30 - 32', '32 - 34', '34 - 36', '37 - 38', '39 - 40'],
                    ["Inseam", 25.5, 26, 28.5, 30.5, 32, 33.5],
                    ["Leg Opening", 7, 8, 9, 10, 11, 12],
                    ["Thigh", 11, 12, 12, 13, 14, 15],
                    ["Knee", 9, 9, 10, 11, 12, 13]]
                
        elif product == '5' or product == '6' or product == '7' or product == '8' and fit == '2':
            name = "BAGGY FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Waist", '28 - 30', '30 - 32', '32 - 34', '34 - 36', '37 - 38', '39 - 40'],
                    ["Inseam", 25.5, 26, 28.5, 30.5, 32, 33.5],
                    ["Leg Opening", 8, 9, 10, 11, 12, 13],
                    ["Thigh", 11, 12.5, 14, 16.5, 17, 18],
                    ["Knee", 9, 11.5, 13.5, 15, 17.5, 18.5]]
                
        elif product == '5' or product == '6' or product == '7' or product == '8' and fit == '3':
            name = "SLIM FIT (INCHES)"
            data = [["Measure","XS","S","M","L","XL","XXL"],
                    ["Waist", '28 - 30', '30 - 32', '32 - 34', '34 - 36', '37 - 38', '39 - 40'],
                    ["Inseam", 25, 25.5, 28, 30, 31.5, 33],
                    ["Leg Opening", 6.5, 7.5, 8.5, 9.5, 10.5, 11.5],
                    ["Thigh", 11, 11.5, 11.5, 12, 14, 15],
                    ["Knee", 8.5, 8.5, 9.5, 10.5, 12, 13]]
                


        total_rows = len(data)
        total_columns = len(data[0])

        

        for i in range(total_rows):
                for j in range(total_columns):
                        e = Entry(top, width=10, fg='black', font=('Arial',16))
                        e.grid(row=i, column=j)
                        e.insert(END, data[i][j])
                        e.configure(state=DISABLED)
        top.title(f"Size Chart - {name}")
        top.mainloop()
        

    
    def _insert_message(self,msg,sender):
        if not msg:
            return
        
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.yview(END)

    def bot_message(self,bot_msg):
        msg2 = f"{'Gaafar'}: {bot_msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.yview(END)


if __name__ == "__main__":
    # The first line of code to be executed is to create an instance from your main class
    app = menkhet_gui()
    
    # Second and last thing is to call the "run" method on the main class instance
    app.run()