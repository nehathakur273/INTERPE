import customtkinter as ctk
from PIL import Image
import time
from tkinter import font, colorchooser

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %B %d, %Y')
    clock_label.configure(text=current_time)
    date_label.configure(text=current_date)
    clock_label.after(1000, update_time)

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code[1]:
        clock_label.configure(text_color=color_code[1])
        date_label.configure(text_color=color_code[1])
        color_button.configure(text_color=color_code[1])
        bg_color_button.configure(text_color=color_code[1])
        font_button.configure(text_color=color_code[1])
        font_combo.configure(text_color=color_code[1])
def choose_background_color():
    color_code = colorchooser.askcolor(title="Choose background color")
    if color_code[1]:
        clock_frame.configure(fg_color=color_code[1])
        color_button.configure(fg_color=color_code[1])
        bg_color_button.configure(fg_color=color_code[1])
        font_button.configure(fg_color=color_code[1])
        font_combo.configure(fg_color=color_code[1])
def choose_font():
    font_choice = font_combo.get()
    clock_label.configure(font=(font_choice, 48))
    date_label.configure(font=(font_choice, 24))
    
##def resize_image(event):
##    new_width = event.width
##    new_height = event.height
##    image = bg_image.resize((new_width, new_height), Image.LANCZOS)
##    background_photo = ctk.CTkImage(light_image=image, size=(new_width, new_height))
##    background_label.configure(image=background_photo)
##    background_label.image = background_photo

# Create the main window
root = ctk.CTk()
root.title("Digital Clock")
root.geometry("800x600")  # Set initial window size
root.resizable(False,False)
img=Image.open('D:\\softwarecomp\\clck.jpg')
imgedt=ctk.CTkImage(img,size=(1000,600))
imlbl=ctk.CTkLabel(root,image=imgedt,text=None)
imlbl.place(x=-70,y=0)

### Create and place the background label
##background_label = ctk.CTkLabel(root, image=background_photo, text="")
##background_label.place(relwidth=1, relheight=1)


# Create a frame to hold the clock and date labels
clock_frame = ctk.CTkFrame(root, fg_color='#222222', width=400, height=200)
clock_frame.place(relx=0.5, rely=0.5, anchor='w')

# Create a label to display the time
clock_label = ctk.CTkLabel(clock_frame, font=('Helvetica', 48), text_color='white')
clock_label.pack(anchor='center', pady=10)

# Create a label to display the date
date_label = ctk.CTkLabel(clock_frame, font=('Helvetica', 24), text_color='white')
date_label.pack(anchor='center', pady=10)

# Create a frame for settings
settings_frame = ctk.CTkFrame(root,bg_color='transparent')
settings_frame.pack(anchor='s', pady=20)

# Color chooser button
color_button = ctk.CTkButton(settings_frame, text="Change Text Color", font=('Cambria',15,'bold'),command=choose_color,fg_color="#8C3061",hover_color="#522258")
color_button.pack(side='left', padx=10)

# Background color chooser button
bg_color_button = ctk.CTkButton(settings_frame, text="Change Background Color",font=('Cambria',15,'bold'), command=choose_background_color,fg_color="#8C3061",hover_color="#522258")
bg_color_button.pack(side='left', padx=10)

# Font chooser
font_combo = ctk.CTkComboBox(settings_frame, values=font.families(),font=('Cambria',15,'bold'),fg_color="#8C3061",text_color="white")
font_combo.set('Helvetica')
font_combo.pack(side='left', padx=10)

font_button = ctk.CTkButton(settings_frame, text="Change Font", font=('Cambria',15,'bold'),command=choose_font,fg_color="#8C3061",hover_color="#522258")
font_button.pack(side='left', padx=10)

# Start the clock
update_time()

# Run the main event loop
root.mainloop()

