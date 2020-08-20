import tkinter as tk                                                            ## import tkinter GUI library

## checks for palindrome and populates output label accordingly
def reverse(s): 
	s = s.strip().lower()                                                   ## Trims entry text
	r = s[::-1]                                                             ## stores reversed text in r
	print(type(s))
	if s == r:                                                              
		results['text'] = '{}\nIs a Palindrome\nCongratulations!'.format(str(s))        ## Congratualtions .. Palindrome!
	else:
		results['text'] =  '({}) \nis not the same as \n({})\n\n{} Is Not a Palindrome'.format(s,r,s) ## Not a palindrome :(

root = tk.Tk()                                                                  ## root widget created

root.attributes('-alpha', 0.8)                                                  ## GUI Opacity Set

canvas = tk.Canvas(root, height=400, width=600)                                 ## Canvas dimentions set and tied to root
canvas.pack()                                                                   ## canvas drawn

background_image = tk.PhotoImage(file='MatrixCode.png')                         ## background image set                    
background_label = tk.Label(root, image = background_image)                     ## BG label set
background_label.place(relwidth=1, relheight=1)                                 ## BG label drawn

title = tk.Label(root, anchor='n', justify='center', bd=4)                      ## Title drawing
title.config(font=('Consolas',18), bg='black', fg='white')                      
title.place(relx=0.15,relwidth=.73, relheight=.1)
title['text'] = 'Is your word a palindrome?'

frame = tk.Frame(root,bg='Dark Green',bd=5)                                     ## frame for textbox and button
frame.place(relx=0.5, rely=0.12, relwidth =0.85, relheight=0.15, anchor="n")

entry = tk.Entry(frame, font=('Courier',28),fg='Dark Green')                    ## textbox set and drawn
entry.place(relwidth =0.65, relheight=1)
entry.focus()                                                                   ## focus set to texbox on load

## button drawn and click event is wired to get_weather function
button = tk.Button(frame, text="Palindrome?",font=('Courier',14), command=lambda: reverse(entry.get()))
button.place(relx=0.7 , relheight=1, relwidth =0.3)

lower_frame = tk.Frame(root, bg='green', bd=10)                                 ## lower frame for output label
lower_frame.place(relx=0.5, rely=0.30, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'black'
results = tk.Label(lower_frame, anchor='n', justify='center', bd=4)             ## Result label drawn
results.config(font=('Courier',18), bg=bg_color, fg='light green')
results.place(relwidth=1, relheight=1)

root.mainloop()                                                                 ## root main
