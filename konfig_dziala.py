# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import tkinter as tk
import pandas as pd


def get_prices(product_id):
    df = pd.read_csv('prices.csv', encoding='latin-1')
    price = df[df['product_id'].isin([product_id])]['price']
    return int(price.iloc[0]) if not price.empty else None


selected_elements = []


def update_total_price(final_label):
    total_price = 0
    final_price = 0
    for item, price in selected_elements:
        total_price += price
    total_label.config(text=f'Cena całkowita: {total_price} PLN')
    discount = discount_var.get()
    if discount_var.get() == 0:
        try:          
            discount = int(discount_var.get())
           
        except:
            discount = 0
   
            
    final_price = total_price - (total_price * discount / 100)
    final_price = round(final_price)
    final_label.config(text=f'Cena po rabacie: {final_price} PLN')
    

    with open('selected_elements.txt', "w") as file:
        for item, price in selected_elements:
            file.write(f'{item["name"]}, ID: {item["id"]}, cena: {price}\n')
        file.write(f'\nCałkowita kwota konfiguracji: {total_price} PLN\n')
        file.write(f'Cena po rabacie ({discount}%): {final_price} PLN')




elements = [
    {'name':  '             IS-100 '},
    {'name': '~~Basic items~~'},
    {'name': 'IS-100 Inclusive lamp', 'id': 420000208},
    {'name': 'TLD-100 Trial lens drawer', 'id': 420000213},
    {'name': 'TLD-100XL Trial lens drawer', 'id': 420000222},
    {'name': 'Bracket Power supply CV-5000S', 'id': 420000215},
    {'name': 'VT-670 for IS-100', 'id': 1202281},
    {'name': 'VT-671 for IS-100', 'id': 1202282},
    {'name': 'OC-8 Dark Grey', 'id': 420000209},
    {'name': 'OC-8 Blue', 'id': 420000210},
    {'name': 'OC-9 Dark Grey', 'id': 420000211},
    {'name': 'OC-9 Blue', 'id': 420000212},
    {'name': 'OC-6 / OC-8 Footrest', 'id': 1202290},
    {'name': '~~Optional furniture~~'},
    {'name': 'IS-100 satellite support', 'id': 420000216},
    {'name': 'Bracket Power supply CV-5000S', 'id': 420000215},
    {'name': 'TLD-100 support', 'id': 420000217},
    {'name': 'Projector support for IS-100', 'id': 1202206},
    {'name': 'Footswitch for OC (all)', 'id': 1212901},
    {'name': 'Footswitch cable for IS-100', 'id': 420000223},
    {'name': 'RL-100 Reading light for IS-100', 'id': 420000214},
    {'name': 'PS-100 Slitlamp power supply', 'id': 420000220},
    {'name': 'Tabletop extension for IS-100', 'id': 420000224},
    {'name': 'Accessory tray for IS-100', 'id': 420000226},
    {'name': 'Power Supply Low voltage', 'id': 420000253},
    {'name': 'Chinrest support for position 2', 'id': 420000244 },
    {'name':  ' '},
    {'name':  ' '},
    {'name':  '             IS-600 III'},
    {'name': '~~Unit options LEFT version [L]~~'},
    {'name': 'Left chassis w elevation [L]', 'id': 420001459},
    {'name': 'Left finishing set white [L]', 'id': 420001463},
    {'name': 'Left TL drawer white [L]', 'id': 420001461},
    {'name': 'Left baseplate & cover [L]', 'id': 420001455},
    {'name': 'Left tabletop arm & column [L]', 'id': 420001457},
    {'name': 'Left column fixed to table top [L]', 'id': 420001470},
    {'name':  ' '},
    {'name': '~~Unit options RIGHT version [R]~~' },
    {'name': 'Right chassis w elevation [R]', 'id': 420001458},
    {'name': 'Right finishing set white [R]', 'id': 420001462},
    {'name': 'Right TL drawer white [R]', 'id': 420001460},
    {'name': 'Right baseplate & cover [R]', 'id': 420001454},
    {'name': 'Right tabletop arm & column [R]', 'id': 420001456},
    {'name': 'Right VT-72 [R]', 'id': 1207901},
    {'name': 'Right column fixed to table top [R]', 'id': 420001469},
    {'name':  ' '},
    {'name': '~~Unit common parts [R\L]~~'},
    {'name': 'OC-8 Dark Grey', 'id': 420000209},
    {'name': 'OC-8 Blue', 'id': 420000210},
    {'name': 'OC-9 Dark Grey', 'id': 420000211},
    {'name': 'OC-9 Blue', 'id': 420000212},
    {'name': 'Baseplate&cover wheelchair [R\L]', 'id': 1222208},
    {'name': 'Counterweights [R\L]', 'id': 1202557},
    {'name': 'OC-8 baseplate w/o wheels [R\L]', 'id': 420001464},
    {'name': 'OC-8 baseplate w wheels [R\L]', 'id': 420001465},
    {'name': 'OC-9 baseplate w/o wheels [R\L]', 'id': 420001466},
    {'name': 'VT-74 [R\L]', 'id': 1222223},
    {'name':  ' '},
    {'name': '~~Optional items and accessories~~'},
    {'name': 'PS drawer white', 'id': 1222218},
    {'name': 'Electrobrake', 'id': 420001468},
    {'name': 'Near vision lamp', 'id': 420001467},
    {'name': 'KB-50 satellite support', 'id': 1202241},
    {'name': 'Sliding chinrest support', 'id': 1202580},
    {'name': 'VT-72 adapter for VT-10', 'id': 1207904},
    {'name': 'OC-6 / OC-8 Footrest', 'id': 1202290},
    {'name': 'Footswitch for OC (all) ', 'id': 1212901},
    {'name': 'Series cable footswitch ', 'id': 1202293},
    {'name': 'Table extension strip ', 'id': 420000224},
    {'name': 'PS-100 Power supply ', 'id': 420000220},
    {'name': 'Projector support ', 'id': 1202206},
    {'name': 'Power Supply Kit OC-8/9 stand-alone ', 'id': 420001873},
    
    
                ]

selected_elements = []

root = tk.Tk()
root.title("UNITS CONFIGURATOR")
root.geometry("1000x710")

frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, expand=True, anchor='center')

listbox = tk.Listbox(frame1, font=("Helvetica", 16))
listbox.pack(fill=tk.BOTH, expand=True)

for element in elements:
    listbox.insert(tk.END, element['name'])



price_label = tk.Label(frame2, font=("Helvetica", 22), text='')


total_label = tk.Label(frame2, font=("Helvetica", 22), text='')


discount_var = tk.IntVar()




final_label = tk.Label(frame2, font=("Helvetica", 20), text='')

discount_var.trace("w", update_total_price(final_label))
discount_label = tk.Label(frame2, font=("Helvetica", 20), text="Najpierw podaj rabat w procentach!")
discount_label.pack()
discount_entry = tk.Entry(frame2, font=("Helvetica", 20), textvariable = discount_var)
discount_entry.pack()

price_label.pack()
total_label.pack()
final_label.pack()

def on_select(event):
    selection = event.widget.curselection()
    if not selection:
        return
    item_index = selection[0]
    item = elements[item_index]
    price = get_prices(item['id'])
    if price is not None:
        selected_elements.append((item, price))
        price_label.config(text=f'Cena produktu: {price} PLN')
    else:
        price_label.config(text='Nie znaleziono ceny dla wybranego produktu.')
    update_total_price(final_label)
          

listbox.bind('<<ListboxSelect>>', on_select)
root.mainloop()

