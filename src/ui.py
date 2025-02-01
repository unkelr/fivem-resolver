from tkinter import Tk, Frame, Text, Entry, Button, END, LEFT
import requests
from colorama import Fore

class AppUI:
    def __init__(self, master):
        self.master = master
        self.master.title("FiveM Resolver")
        self.master.geometry("600x400")
        self.master.configure(bg='#2e2e2e')

        self.frame = Frame(self.master, bg='#2e2e2e')
        self.frame.pack(pady=10)

        self.output_box = Text(self.frame, height=15, width=70, bg='#3e3e3e', fg='white', wrap='word', font=('Helvetica', 10))
        self.output_box.pack(side=LEFT, fill='both', expand=True)
        self.output_box.config(state='disabled')

        self.input_area = Entry(self.master, width=50, bg='white', fg='black', font=('Helvetica', 10))
        self.input_area.pack(pady=10)

        self.submit_button = Button(self.master, text="Submit", command=self.fetch_data, bg='#4CAF50', fg='white', font=('Helvetica', 10))
        self.submit_button.pack(pady=5)

        self.clear_button = Button(self.master, text="Clear Console", command=self.clear_console, bg='#f44336', fg='white', font=('Helvetica', 10))
        self.clear_button.pack(pady=5)

    def fetch_data(self):
        query = self.input_area.get()
        self.output_box.config(state='normal')
        self.output_box.delete(1.0, END)
        self.output_box.insert(END, f"{Fore.GREEN}cfx -> {query}\n")
        self.get_server_data(query)
        self.output_box.config(state='disabled')

    def get_server_data(self, query):
        url = f"https://servers-frontend.fivem.net/api/servers/single/{query}"
        headers = {
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0'
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            self.output_box.config(state='normal')
            if 'Data' in data:
                ip = data['Data'].get('connectEndPoints', ['N/A'])[0]
                mxclients = data['Data'].get('sv_maxclients', 'N/A')
                clients = data['Data'].get('clients', 'N/A')
                hostname = data['Data'].get('hostname', 'N/A')
                upvotepower = data['Data'].get('upvotePower', 'N/A')
                ownername = data['Data'].get('ownerName', 'N/A')
                ownerprofile = data['Data'].get('ownerProfile', 'N/A')
                discord_link = data['Data']['vars'].get('Discord', 'N/A')

                self.output_box.insert(END, f"""
                IP: {ip}
                Max Clients: {mxclients}
                Clients: {clients}
                Hostname: {hostname}
                Upvote Power: {upvotepower}
                Owner Name: {ownername}
                Owner Profile: {ownerprofile}
                Discord: {discord_link}
                """)
            else:
                self.output_box.insert(END, "No server found\n")
            self.output_box.config(state='disabled')
        except requests.RequestException as e:
            self.output_box.config(state='normal')
            if response.status_code == 429:
                self.output_box.insert(END, "Wait a minute you snail\n")
            else:
                self.output_box.insert(END, f"Error: {e}\n")
            self.output_box.config(state='disabled')
        except ValueError:
            self.output_box.config(state='normal')
            self.output_box.insert(END, "Failed to decode JSON\n")
            self.output_box.config(state='disabled')

    def clear_console(self):
        self.output_box.config(state='normal')
        self.output_box.delete(1.0, END)
        self.output_box.config(state='disabled')