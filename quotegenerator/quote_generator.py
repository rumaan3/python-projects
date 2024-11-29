import tkinter as tk
from tkinter import filedialog, messagebox
from openpyxl import load_workbook

def update_specific_cells(file_path, billing_name, address, email, crm_name, customer_name, ccr, description, estimated_hours):
    try:
        # Load the existing Excel file
        workbook = load_workbook(file_path)
        sheet = workbook.active

        # Update the specific cells with the provided data
        sheet['C7'] = customer_name
        sheet['C8'] = address
        sheet['C9'] = billing_name
        sheet['C10'] = email
        sheet['C12'] = crm_name
        sheet['C16'] = ccr
        sheet['C23'] = description
        sheet['D36'] = estimated_hours

        # Save the changes to the same Excel file
        workbook.save(file_path)
        messagebox.showinfo("Success", "Data successfully updated in the specified cells of the Excel file.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file at {file_path} was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:
        return file_path
    else:
        messagebox.showwarning("Warning", "No file selected.")
        return None

def on_submit():
    file_path = browse_file()
    if file_path:
        billing_name = billing_name_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        crm_name = crm_name_entry.get()
        customer_name = customer_name_entry.get()
        ccr = ccr_entry.get()
        description = description_entry.get()
        estimated_hours = estimated_hours_entry.get()

        update_specific_cells(file_path, billing_name, address, email, crm_name, customer_name, ccr, description, estimated_hours)

# Create the main window
root = tk.Tk()
root.title("Excel Data Entry Tool")

# Create and place labels and entry fields for each data input
tk.Label(root, text="Billing Name").grid(row=0, column=0, padx=10, pady=5)
billing_name_entry = tk.Entry(root)
billing_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=1, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="CRM Name").grid(row=3, column=0, padx=10, pady=5)
crm_name_entry = tk.Entry(root)
crm_name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Customer Name").grid(row=4, column=0, padx=10, pady=5)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="CCR").grid(row=5, column=0, padx=10, pady=5)
ccr_entry = tk.Entry(root)
ccr_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Description").grid(row=6, column=0, padx=10, pady=5)
description_entry = tk.Entry(root)
description_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Estimated Hours").grid(row=7, column=0, padx=10, pady=5)
estimated_hours_entry = tk.Entry(root)
estimated_hours_entry.grid(row=7, column=1, padx=10, pady=5)

# Create the submit button
submit_button = tk.Button(root, text="Submit Data", command=on_submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
