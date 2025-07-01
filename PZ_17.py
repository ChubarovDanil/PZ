import tkinter as tk
from tkinter import ttk, filedialog

class ContactForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Form")
        self.root.geometry("500x600")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Contact Form", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Form fields
        self.create_field(main_frame, "Name *", "First & Last Name")
        self.create_field(main_frame, "Email *", "Email")
        self.create_field(main_frame, "Phone Number *", "Phone Number")
        
        # Subject dropdown
        subject_frame = ttk.Frame(main_frame)
        subject_frame.pack(fill=tk.X, pady=10)
        
        subject_label = ttk.Label(subject_frame, text="Subject *", font=("Arial", 10))
        subject_label.pack(anchor=tk.W)
        
        self.subject_var = tk.StringVar()
        subject_combobox = ttk.Combobox(subject_frame, textvariable=self.subject_var)
        subject_combobox['values'] = ('Select Subject', 'Support', 'Sales', 'Feedback')
        subject_combobox.current(0)
        subject_combobox.pack(fill=tk.X, pady=5)
        
        # Message field
        message_frame = ttk.Frame(main_frame)
        message_frame.pack(fill=tk.X, pady=10)
        
        message_label = ttk.Label(message_frame, text="Leave us a few words", font=("Arial", 10))
        message_label.pack(anchor=tk.W)
        
        self.message_text = tk.Text(message_frame, height=5, font=("Arial", 10))
        self.message_text.pack(fill=tk.X)
        
        # Separator
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=20)
        
        # File attachments
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=10)
        
        file_label = ttk.Label(file_frame, text="File Attachments", font=("Arial", 12))
        file_label.pack(anchor=tk.W)
        
        self.file_button = ttk.Button(
            file_frame, 
            text="Choose Files", 
            command=self.choose_files
        )
        self.file_button.pack(pady=5)
        
        self.file_label = ttk.Label(file_frame, text="No file chosen")
        self.file_label.pack(anchor=tk.W)
        
        # reCAPTCHA
        captcha_frame = ttk.Frame(main_frame)
        captcha_frame.pack(fill=tk.X, pady=20)
        
        self.captcha_var = tk.BooleanVar()
        captcha_check = ttk.Checkbutton(
            captcha_frame, 
            text="I'm not a robot", 
            variable=self.captcha_var
        )
        captcha_check.pack(anchor=tk.W)
        
        captcha_label = ttk.Label(captcha_frame, text="reCAPTCHA", font=("Arial", 8))
        captcha_label.pack(anchor=tk.W)
        
        terms_label = ttk.Label(captcha_frame, text="Privacy - Terms", font=("Arial", 8))
        terms_label.pack(anchor=tk.W)
        
        # Submit button
        submit_button = ttk.Button(
            main_frame, 
            text="Submit", 
            command=self.submit_form
        )
        submit_button.pack(pady=20)
    
    def create_field(self, parent, label_text, placeholder):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=10)
        
        label = ttk.Label(frame, text=label_text, font=("Arial", 10))
        label.pack(anchor=tk.W)
        
        entry = ttk.Entry(frame, font=("Arial", 10))
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e: entry.delete(0, tk.END) if entry.get() == placeholder else None)
        entry.bind("<FocusOut>", lambda e: entry.insert(0, placeholder) if not entry.get() else None)
        entry.pack(fill=tk.X)
        
        setattr(self, f"{label_text.replace(' ', '_').replace('*', '').lower()}_entry", entry)
    
    def choose_files(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_label.config(text=f"{len(file_paths)} file(s) selected")
    
    def submit_form(self):
        if not self.captcha_var.get():
            tk.messagebox.showwarning("Warning", "Please verify you're not a robot")
            return
        
        # Get form data
        data = {
            "name": self.name_entry.get(),
            "email": self.email_entry.get(),
            "phone": self.phone_number_entry.get(),
            "subject": self.subject_var.get(),
            "message": self.message_text.get("1.0", tk.END).strip(),
            "files": self.file_label.cget("text")
        }
        
        # Validate required fields
        if not all([data['name'], data['email'], data['phone']]):
            tk.messagebox.showwarning("Warning", "Please fill all required fields (*)")
            return
        
        print("Form submitted with data:", data)
        tk.messagebox.showinfo("Success", "Your form has been submitted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactForm(root)
    root.mainloop()