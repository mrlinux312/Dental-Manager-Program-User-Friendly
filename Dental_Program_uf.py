import tkinter as tk
from tkinter import ttk, messagebox
import datetime

patients = {}
appointments = []


# Patient Functions


def add_patient():
    pid = entry_pid.get().strip()
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    notes = entry_notes.get().strip()

    if not pid or not name:
        messagebox.showerror("Error", "Patient ID and Name are required.")
        return

    if pid in patients:
        messagebox.showerror("Error", "Patient ID already exists.")
        return

    patients[pid] = {"name": name, "phone": phone, "notes": notes}
    messagebox.showinfo("Success", "Patient added successfully.")
    entry_pid.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_notes.delete(0, tk.END)

def list_patients():
    listbox.delete(0, tk.END)
    if not patients:
        listbox.insert(tk.END, "No patients found.")
        return

    for pid, info in patients.items():
        listbox.insert(tk.END, f"ID: {pid} | {info['name']} | {info['phone']} | {info['notes']}")


# Appointment Functions


def schedule_appointment():
    pid = entry_appt_pid.get().strip()
    date_str = entry_date.get().strip()
    time_str = entry_time.get().strip()
    reason = entry_reason.get().strip()

    if pid not in patients:
        messagebox.showerror("Error", "Patient ID not found.")
        return

    try:
        dt = datetime.datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid date/time format.")
        return

    appointments.append({"patient_id": pid, "datetime": dt, "reason": reason})
    messagebox.showinfo("Success", "Appointment scheduled.")
    entry_appt_pid.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_reason.delete(0, tk.END)

def list_appointments():
    listbox.delete(0, tk.END)
    if not appointments:
        listbox.insert(tk.END, "No appointments scheduled.")
        return

    for appt in sorted(appointments, key=lambda a: a["datetime"]):
        p = patients[appt["patient_id"]]["name"]
        listbox.insert(tk.END, f"{appt['datetime']} | {p} | {appt['reason']}")


# GUI Setup


root = tk.Tk()
root.title("Dental Office Program")
root.geometry("700x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


# Add Patient Tab


tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Add Patient")

tk.Label(tab1, text="Patient ID:").pack()
entry_pid = tk.Entry(tab1)
entry_pid.pack()

tk.Label(tab1, text="Name:").pack()
entry_name = tk.Entry(tab1)
entry_name.pack()

tk.Label(tab1, text="Phone:").pack()
entry_phone = tk.Entry(tab1)
entry_phone.pack()

tk.Label(tab1, text="Notes:").pack()
entry_notes = tk.Entry(tab1)
entry_notes.pack()

tk.Button(tab1, text="Add Patient", command=add_patient).pack(pady=10)


# Schedule Appointment Tab


tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Schedule Appointment")

tk.Label(tab2, text="Patient ID:").pack()
entry_appt_pid = tk.Entry(tab2)
entry_appt_pid.pack()

tk.Label(tab2, text="Date (YYYY-MM-DD):").pack()
entry_date = tk.Entry(tab2)
entry_date.pack()

tk.Label(tab2, text="Time (HH:MM):").pack()
entry_time = tk.Entry(tab2)
entry_time.pack()

tk.Label(tab2, text="Reason:").pack()
entry_reason = tk.Entry(tab2)
entry_reason.pack()

tk.Button(tab2, text="Schedule", command=schedule_appointment).pack(pady=10)


# View Data Tab


tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="View Records")

tk.Button(tab3, text="Show Patients", command=list_patients).pack(pady=5)
tk.Button(tab3, text="Show Appointments", command=list_appointments).pack(pady=5)

listbox = tk.Listbox(tab3, width=80, height=20)
listbox.pack(pady=10)

root.mainloop()

