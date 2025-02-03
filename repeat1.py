import tkinter as tk
import time

# Определяем start_time на уровне модуля
start_time = 0

def update_time():
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    time_label.config(text=f"{minutes:02}:{seconds:02}")
    root.after(1000, update_time)

def start_timer():
    global start_time
    start_time = time.time()
    update_time()

# Создаем основное окно
root = tk.Tk()
root.title("Секундомер")
root.geometry("200x100")
root.configure(bg="lightgreen")
root.attributes("-topmost", True)

# Создаем метку для отображения времени
time_label = tk.Label(root, text="00:00", font=("Helvetica", 48), fg="red", bg="lightgreen")
time_label.pack(pady=20)

# Создаем кнопку для запуска таймера
start_button = tk.Button(root, text="Старт", command=start_timer)
start_button.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
