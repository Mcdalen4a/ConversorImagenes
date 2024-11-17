import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convertir_imagen(input_path, output_path, output_format):
    try:
     
        with Image.open(input_path) as img:
        
            img.save(output_path, format=output_format)
            return True
    except Exception as e:
        print(f"Error al convertir la imagen: {e}")
        return False

def seleccionar_archivo():

    archivo = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if archivo:
        entry_input_path.delete(0, tk.END)  
        entry_input_path.insert(0, archivo)  

def seleccionar_carpeta_salida():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de salida")
    if carpeta:
        entry_output_folder.delete(0, tk.END)  
        entry_output_folder.insert(0, carpeta)  

def convertir():
    
    input_path = entry_input_path.get()
    output_folder = entry_output_folder.get()
    output_format = combo_format.get()

    if not input_path or not output_folder:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una imagen y una carpeta de salida.")
        return

 
    filename = os.path.basename(input_path)
    output_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
    output_path = os.path.join(output_folder, output_filename)


    if convertir_imagen(input_path, output_path, output_format):
        messagebox.showinfo("Éxito", f"Imagen convertida y guardada en: {output_path}")
    else:
        messagebox.showerror("Error", "Hubo un problema al convertir la imagen.")

root = tk.Tk()
root.title("Conversor de Imágenes")


label_input = tk.Label(root, text="Selecciona la imagen:")
label_input.pack(pady=5)

entry_input_path = tk.Entry(root, width=50)
entry_input_path.pack(pady=5)

btn_select_file = tk.Button(root, text="Seleccionar Imagen", command=seleccionar_archivo)
btn_select_file.pack(pady=5)

label_output = tk.Label(root, text="Selecciona la carpeta de salida:")
label_output.pack(pady=5)

entry_output_folder = tk.Entry(root, width=50)
entry_output_folder.pack(pady=5)

btn_select_folder = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta_salida)
btn_select_folder.pack(pady=5)

label_format = tk.Label(root, text="Selecciona el formato de salida:")
label_format.pack(pady=5)

combo_format = tk.StringVar()
combo_format.set("PNG")  
formats = ["PNG", "JPEG", "BMP", "GIF"]
dropdown_format = tk.OptionMenu(root, combo_format, *formats)
dropdown_format.pack(pady=5)

btn_convert = tk.Button(root, text="Convertir Imagen", command=convertir)
btn_convert.pack(pady=20)


root.mainloop()
