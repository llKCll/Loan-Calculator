import tkinter as tk
payment_app = tk.Tk()

# tkinter title bar
payment_app.title("Monthly Loan Payment Calculator")

# Create the labels to identify the information to input.
amount_label = tk.Label(payment_app, text="Loan Amount:")
amount_label.grid(row=0, column=0, sticky=tk.W, padx = 20, pady = 20)

interest_label = tk.Label(payment_app, text="Interest Rate:")
interest_label.grid(row=1, column=0, sticky=tk.W, padx = 20, pady = 20)

period_label = tk.Label(payment_app, text="Loan Period (years):")
period_label.grid(row=2, column=0, sticky=tk.W, padx = 20, pady = 20)

payment_label = tk.Label(payment_app, text="Monthly Payment:")
payment_label.grid(row=3, column=0, sticky=tk.W, padx = 20, pady = 20)

# Create entry boxes to input the loan information.
amount_entry = tk.Entry(payment_app)
amount_entry.grid(row=0, column=1, padx = 20)

interest_entry = tk.Entry(payment_app)
interest_entry.grid(row=1, column=1, padx = 20)

period_entry = tk.Entry(payment_app)
period_entry.grid(row=2, column=1, padx = 20)

payment_entry = tk.Entry(payment_app, state='readonly')
payment_entry.grid(row=3, column=1, padx = 20)

'''
    Calculates loan amount when given loan amount, interest rate, and loan period in years.
    Push compute button and answer appears in monthly payment box
    checks if loan amount > 0 and for a string with letters
'''
def calc(): 
    amount = amount_entry.get()
    rate = interest_entry.get()
    years = period_entry.get()
    
    # Check for letters
    if not amount.isalpha() and not rate.isalpha() and not years.isalpha(): 
        amount = float(amount)
        rate = float(rate)
        years = float(years)

        # Calculate the result.
        if amount > 0:
            r = (rate / 100) / 12
            p = 12 * years
            payment = (r * amount) / (1-(1+r)**-p)
            payment = round(payment, 2)
            payment = str(payment)
            
            # Update the montly payment result in the entry box.
            payment_entry.configure(state='normal')
            payment_entry.delete(0, tk.END)
            payment_entry.insert(0, '$'+payment)
            payment_entry.configure(state='readonly')
    #end if
#end def

# Create the button to calculate the entries.
compute_button = tk.Button(payment_app, text='Compute Payment', command=calc) 
compute_button.grid(row=4, column=0, columnspan=2, pady = 30)
