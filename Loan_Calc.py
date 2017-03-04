import tkinter as tk
payment_app = tk.Tk()

amount_label = tk.Label(payment_app, text="Loan Amount:")
amount_label.grid(row=0, column=0, sticky=tk.W, padx = 20, pady = 20)

interest_label = tk.Label(payment_app, text="Interest Rate:")
interest_label.grid(row=1, column=0, sticky=tk.W, padx = 20, pady = 20)

period_label = tk.Label(payment_app, text="Loan Period:")
period_label.grid(row=2, column=0, sticky=tk.W, padx = 20, pady = 20)

payment_label = tk.Label(payment_app, text="Payment:")
payment_label.grid(row=3, column=0, sticky=tk.W, padx = 20, pady = 20)

amount_entry = tk.Entry(payment_app)
amount_entry.grid(row=0, column=1, padx = 20)

interest_entry = tk.Entry(payment_app)
interest_entry.grid(row=1, column=1, padx = 20)

period_entry = tk.Entry(payment_app)
period_entry.grid(row=2, column=1, padx = 20)

payment_entry = tk.Entry(payment_app, state='readonly')
payment_entry.grid(row=3, column=1, padx = 20)

def calc(): 
    '''
        calculates loan amount when given loan amount, interest rate, and loan period.
        push button and answer appears in monthly payment box
        checks if loan amount > 0 and for a string with letters
    '''
    amount = amount_entry.get()
    rate = interest_entry.get()
    years = period_entry.get()
    if not amount.isalpha() and not rate.isalpha() and not years.isalpha(): # check for letters
        amount = float(amount)
        rate = float(rate)
        years = float(years)
        if amount > 0:
            r = (rate / 100) / 12
            p = 12 * years
            payment = str(round((r * amount) / (1-(1+r)**-p), 2))
            payment_entry.configure(state='normal')
            payment_entry.delete(0, tk.END)
            payment_entry.insert(0, '$'+payment)
            payment_entry.configure(state='readonly')
    #end if
#end def

compute_button = tk.Button(payment_app, text='Compute Payment', command=calc) 
compute_button.grid(row=4, column=0, columnspan=2, pady = 30)
