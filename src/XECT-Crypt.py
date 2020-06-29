#!/bin/env python3

import ntpath
import getpass
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import HORIZONTAL
from cryptography.fernet import Fernet

root = tk.Tk()
root.title("XECT-Crypt")
root.geometry("600x500")
root.iconbitmap("lib/icon.ico")

encrypt_input = 0
decrypt_input = 0
keyfile_input = 0

header_image = ImageTk.PhotoImage(Image.open("lib/heading.png"))
heading = tk.Label(root, image=header_image)
heading.grid(row=0, column=0, columnspan=2, sticky=tk.W)

def decryption(inputfile, keyfile):

	with open(keyfile) as file:
		keys2 = file.readlines()

	for key in keys2:
		if key[0] == "#":
			keys2.remove(key)

	global ciphers
	ciphers = []
	for key in keys2:
		cipher = Fernet(key)
		ciphers.append(cipher)

	ciphers.reverse()

	with open(inputfile, 'rb') as file:
		contents2 = file.read()
		for cipher in ciphers:
			contents2 = cipher.decrypt(contents2)

	def find_output_location():
		starting_dir = "C:/Users/" + getpass.getuser() + "/Desktop"
		root.directory3 =  filedialog.asksaveasfilename(initialdir =starting_dir,title ="Save file",filetypes=[("all files","*.*")])
		global outputfile
		outputfile = root.directory3
	find_output_location()

	with open(outputfile, 'wb') as file:
		file.write(contents2)

frame2 = tk.LabelFrame(root)
frame2.grid(row=1, column=1, sticky=tk.W+tk.N)

def decrypt_input_file():
	starting_dir = "C:/Users/" + getpass.getuser() + "/Desktop"
	root.filename2 = filedialog.askopenfilename(initialdir=starting_dir, title="Select File", filetypes=[("all files","*.*")])
	global decrypt_input
	decrypt_input = root.filename2
	if root.filename2:
		decrypt_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=decrypt_input_file, bg="green3")
		decrypt_input_button.grid(row=2, column=1, columnspan=3, pady=3)
decrypt_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=decrypt_input_file)
decrypt_input_button.grid(row=2, column=1, columnspan=3, pady=3)

decrypt_input_label = tk.Label(frame2, text="Select file to Decrypt")
decrypt_input_label.grid(row=3, column=1, columnspan=3)

def keyfile_input_f():
	starting_dir = "C:/Users/" + getpass.getuser() + "/Desktop"
	root.filename3 = filedialog.askopenfilename(initialdir=starting_dir, title="Select File", filetypes=[("all files","*.*")])
	global keyfile_input
	keyfile_input = root.filename3
	if root.filename3:
		keyfile_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=keyfile_input_f, bg="green3")
		keyfile_input_button.grid(row=5, column=2, pady=2)
keyfile_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=keyfile_input_f)
keyfile_input_button.grid(row=5, column=2, pady=2)

keyfile_input_label = tk.Label(frame2, text="Select key file to use")
keyfile_input_label.grid(row=6, column=1, columnspan=3)

def error_no_decrypt_file():
	popup3 = tk.Tk()
	popup3.title("Error")
	popup3.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup3, text="Error: No input file", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup3, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), bg="firebrick1", command=lambda: popup3.withdraw())
	exit_button.pack(pady=15)
	popup3.mainloop()

def error_no_keyfile():
	popup4 = tk.Tk()
	popup4.title("Error")
	popup4.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup4, text="Error: No key file", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup4, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), bg="firebrick1", command=lambda: popup4.withdraw())
	exit_button.pack(pady=15)
	popup4.mainloop()

def error_decrypt_fail():
	popup5 = tk.Tk()
	popup5.title("Error")
	popup5.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup5, text="Error: Decryption failed", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup5, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), bg="firebrick1", command=lambda: popup5.withdraw())
	exit_button.pack(pady=15)
	popup5.mainloop()

def press_decrypt_button():
	if decrypt_input != 0:
		if keyfile_input != 0:
			try:
				decryption(decrypt_input, keyfile_input)
			except:
				error_decrypt_fail()
		else:
			error_no_keyfile()
	else:
		error_no_decrypt_file()

decrypt_button = tk.Button(frame2, text="Decrypt", padx=20, pady=10, font='Helvetica 15 bold', command=press_decrypt_button, bg='firebrick1', borderwidth=3)
decrypt_button.grid(row=8, column=1, columnspan=3)

top_padder2 = tk.Label(frame2, text=" ", pady=8)
top_padder2.grid(row=1, column=0, columnspan=5)
left_padder2 = tk.Label(frame2, text=" ", padx=35)
left_padder2.grid(row=1, column=0, rowspan=11)
right_padder2 = tk.Label(frame2, text=" ", padx=40)
right_padder2.grid(row=1, column=4, rowspan=11)
middle_padder2 = tk.Label(frame2, text=" ", pady=6)
middle_padder2.grid(row=4, column=0, columnspan=5)
bottom_padder2 = tk.Label(frame2, text=" ", pady=29)
bottom_padder2.grid(row=7, column=0, columnspan=5)
lowest_padder = tk.Label(frame2, text=" ", pady=18)
lowest_padder.grid(row=9, column=1, columnspan=5)

def help_popup():
	popup5 = tk.Tk()
	popup5.title("Help")
	popup5.iconbitmap("lib/icon.ico")

	top_padder = tk.Label(popup5, text=" ")
	top_padder.grid(row=0, column=0, columnspan=2)

	e_help_heading = tk.Label(popup5, text="How to Encrypt", font='Helvetica 13 bold', padx=5)
	e_help_heading.grid(row=1, column=0)
	e_help_msg = tk.Label(popup5, text="To get started choose a file to encrypt by pressing the \n'Select' button on the left sideof the screen. Then choose the level of \nencryption (how many iterations to encrypt with), then simply\n press the 'Encrypt' button.")
	e_help_msg.grid(row=2, column=0, padx=15)

	padder1 = tk.Label(popup5, text=" ")
	padder1.grid(row=3, column=0, columnspan=2)

	d_help_heading = tk.Label(popup5, text="How to Decrypt", font='Helvetica 13 bold', padx=5)
	d_help_heading.grid(row=4, column=0)
	d_help_msg = tk.Label(popup5, text="First select the encrypted file you would like to decrypt by pressing \nthe top 'Select' button on the right side of the window. Then \nselect the key file used to encrypt it by pressing the next button below. \nThen simply press the 'Decrypt' button.")
	d_help_msg.grid(row=5, column=0)

	padder2 = tk.Label(popup5, text=" ")
	padder2.grid(row=6, column=0, columnspan=2)

	o_help_heading = tk.Label(popup5, text="Other Infomation", font='Helvetica 13 bold', padx=5)
	o_help_heading.grid(row=7, column=0)
	o_help_msg = tk.Label(popup5, text="The level of encryption you choose will detirmine how many 32-byte \nkeys will be used to encrypt your file. Also be warned that encrypting a \nlarge file with the highest encryption setting can cause the file \nto inflate dramastically taking up space.")
	o_help_msg.grid(row=8, column=0, padx=15)

	bottom_padder = tk.Label(popup5, text=' ')
	bottom_padder.grid(row=9, column=0, columnspan=2, pady=5)

	name = tk.Label(popup5, text="Created by Treebug842")
	name.grid(row=10, column=0, sticky=tk.W)

	popup5.mainloop()

help_button = tk.Button(frame2, text="Help", padx=10, font='Helvetica 13 bold', command=help_popup)
help_button.grid(row=10, column=0, sticky=tk.W)

def encryption(inputfile1, recursion):
	global outputfile
	global keyfile

	global keys
	keys = []
	for i in range(1, (recursion + 1)):
		key = Fernet.generate_key()
		keys.append(key)

	global ciphers
	ciphers = []
	for key in keys:
		cipher = Fernet(key)
		ciphers.append(cipher)

	with open(inputfile1, 'rb') as file:
		contents = file.read()

	for cipher in ciphers:
		contents = cipher.encrypt(contents)

	def find_save_location():
		starting_dir = "C:/Users/" + getpass.getuser() + "/Desktop"
		root.directory1 =  filedialog.asksaveasfilename(initialdir =starting_dir,title ="Save file",filetypes=[("all files","*.*")])
		global outputfile
		outputfile = root.directory1
		global keyfile
		keyfile = ntpath.dirname(outputfile) + "/key.txt"
	find_save_location()

	with open(outputfile, 'wb') as file:
		file.write(contents)

	keyfile = open(keyfile, 'wb')
	keyfile.write(b"############## Encryption Key ##############\n")
	for key in keys:
		keyfile.write(key)
		keyfile.write(b"\n")
	endstring = ("#Filename: " + ntpath.basename(inputfile1) + ", Iterations: " + str(recursion))
	keyfile.write(endstring.encode())
	keyfile.close()

frame1 = tk.LabelFrame(root)
frame1.grid(row=1, column=0, sticky=tk.W)

def encrypt_input_file():
	starting_dir = "C:/Users/" + getpass.getuser() + "/Desktop"
	root.filename1 = filedialog.askopenfilename(initialdir=starting_dir, title="Select File to Encrypt", filetypes=[("all files","*.*")])
	global encrypt_input
	encrypt_input = root.filename1
	if root.filename1:
		encrypt_input_button = tk.Button(frame1, text="Select", padx=10, font='Helvetica 13 bold', command=encrypt_input_file, bg="green3")
		encrypt_input_button.grid(row=2, column=2)
encrypt_input_button = tk.Button(frame1, text="Select", padx=10, font='Helvetica 13 bold', command=encrypt_input_file)
encrypt_input_button.grid(row=2, column=2)
encrypt_label = tk.Label(frame1, text="Select file to Encrypt")
encrypt_label.grid(row=3, column=1, columnspan=3, pady=3)

slider = tk.Scale(frame1, from_=1, to=12, orient=HORIZONTAL, length=200)
slider.grid(row=5, column=1, columnspan=3)
slider_label = tk.Label(frame1, text="Select level of encryption")
slider_label.grid(row=6, column=1, columnspan=3)

def error_no_input():
	popup1 = tk.Tk()
	popup1.title("Error")
	popup1.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup1, text="Error: No input file", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup1, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), bg="firebrick1", command=lambda: popup1.withdraw())
	exit_button.pack(pady=15)
	popup1.mainloop()

def error_encrypt_fail():
	popup2 = tk.Tk()
	popup2.title("Error")
	popup2.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup2, text="Error: Encryption failed", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup2, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), bg="firebrick1", command=lambda: popup2.withdraw())
	exit_button.pack(pady=15)
	popup2.mainloop()

def press_encrypt_button():
	if encrypt_input != 0:
		recursion = slider.get()
		try:
			encryption(encrypt_input, recursion)
		except:
			error_encrypt_fail()
	else:
		error_no_input()
global encrypt_button
encrypt_button = tk.Button(frame1, text="Encrypt", padx=20, pady=10, font='Helvetica 15 bold', command=press_encrypt_button, bg="firebrick1", borderwidth=3)
encrypt_button.grid(row=8, column=1, columnspan=3)

top_padder = tk.Label(frame1, text=" ", pady=10)
top_padder.grid(row=1, column=0, columnspan=5)
left_padder = tk.Label(frame1, text=" ", padx=19)
left_padder.grid(row=1, column=0, rowspan=11)
right_padder = tk.Label(frame1, text=" ", padx=19)
right_padder.grid(row=1, column=4, rowspan=11)
middle_padder = tk.Label(frame1, text=" ")
middle_padder.grid(row=4, column=0, columnspan=5)
bottom_padder = tk.Label(frame1, text=" ", pady=30)
bottom_padder.grid(row=7, column=0, columnspan=5)
lowest_padder = tk.Label(frame1, text=" ", pady=18)
lowest_padder.grid(row=9, column=0, columnspan=5)


def reset_screen():
	global decrypt_input_button
	decrypt_input_button.grid_remove()
	decrypt_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=decrypt_input_file)
	decrypt_input_button.grid(row=2, column=1, columnspan=3, pady=3)

	global keyfile_input_button
	keyfile_input_button.grid_remove()
	keyfile_input_button = tk.Button(frame2, text="Select", padx=10, font='Helvetica 13 bold', command=keyfile_input_f)
	keyfile_input_button.grid(row=5, column=2, pady=2)

	global encrypt_input_button
	encrypt_input_button.grid_forget()
	encrypt_input_button = tk.Button(frame1, text="Select", padx=10, font='Helvetica 13 bold', command=encrypt_input_file)
	encrypt_input_button.grid(row=2, column=2)

	global slider
	slider.grid_remove()
	slider = tk.Scale(frame1, from_=1, to=12, orient=HORIZONTAL, length=200)
	slider.grid(row=5, column=1, columnspan=3)

	global encrypt_input
	global decrypt_input
	global keyfile_input
	encrypt_input = 0
	decrypt_input = 0
	keyfile_input = 0

clear_button = tk.Button(frame1, text="Clear", padx=10, font='Helvetica 13 bold', command=reset_screen)
clear_button.grid(row=10, column=3, columnspan=2, sticky=tk.E)

root.mainloop()
