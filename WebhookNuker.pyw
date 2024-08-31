import tkinter as tk
from tkinter import messagebox
import requests

def send_messages():
    webhook_url = webhook_entry.get()
    message = message_entry.get()
    amount = int(amount_entry.get())

    if not webhook_url or not message or not amount:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    for _ in range(amount):
        try:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code != 204:
                messagebox.showerror("Error", f"Failed to send message, status code: {response.status_code}")
                return
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return
    
    messagebox.showinfo("Success", "Messages sent successfully!")

root = tk.Tk()
root.title("Webhook Nuker")

tk.Label(root, text="Webhook:").pack(pady=5)
webhook_entry = tk.Entry(root, width=50)
webhook_entry.pack(pady=5)

tk.Label(root, text="Message:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(root, width=50)
amount_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_messages)
send_button.pack(pady=20)

root.mainloop()
