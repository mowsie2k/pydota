import tkinter as tk
import engine as e
from PIL import ImageTk, Image
from tkinter import ttk

# Top level window
window = tk.Tk()
window.title('PyDotaTk')
#window.geometry = '400x200'

def get_input_accountid():
    input = input_accountid.get(1.0, "end-1c")
    e.write_local_player_data(input)
    personaname_label.config(text=e.get_local_personaname())
    steamid_label.config(text=e.get_local_steamid())
    profileurl_label.config(text=e.get_local_profileurl())
    account_id_label.config(text=e.get_local_account_id())

img = Image.open("avatarmedium.jpg")
avatarmedium = ImageTk.PhotoImage(img)
tk.Label(window,image=avatarmedium).grid(row=0,column=0,padx=5,pady=5,rowspan=4,columnspan=1)

tk.Label(window,text='Steam Nickname:').grid(row=0,column=1,sticky='nw')
tk.Label(window,text='Steam ID:').grid(row=1,column=1,sticky='w')
tk.Label(window,text='Steam URL:').grid(row=2,column=1,sticky='w')
tk.Label(window,text='DotA2 Account ID:').grid(row=3,column=1,sticky='w')

window.columnconfigure(2,minsize=100)

personaname_label = tk.Label(window,text='placeholder')
personaname_label.grid(row=0,column=3,sticky='ne',columnspan=2)
steamid_label = tk.Label(window,text='placeholder')
steamid_label.grid(row=1,column=3,sticky='e')
profileurl_label = tk.Label(window,text='placeholder')
profileurl_label.grid(row=2,column=3,sticky='e')
account_id_label = tk.Label(window,text='placeholder')
account_id_label.grid(row=3,column=3,sticky='e')

#window.rowconfigure(4,minsize=100)

tk.Button(window,text='Search',command=get_input_accountid).grid(row=5,column=0,columnspan=2,sticky='ne')
input_accountid = tk.Text(window,height=1,width=10)
input_accountid.grid(row=5,column=2,columnspan=2,padx=5,pady=5,sticky='w')
input_accountid.insert(1.0,"Account ID")

tab_control = ttk.Notebook(window)

overview_frame = ttk.Frame(tab_control)
matches_frame = ttk.Frame(tab_control)
heroes_frame = ttk.Frame(tab_control)
records_frame = ttk.Frame(tab_control)

tab_control.add(overview_frame, text='Overview')
tab_control.add(matches_frame, text='Matches')
tab_control.add(heroes_frame, text='Heroes')
tab_control.add(records_frame, text='Records')

tab_control.grid(row=4,column=0,columnspan=4)

window.mainloop()
