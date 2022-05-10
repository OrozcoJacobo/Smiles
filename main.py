from tkinter import *
from tkinter import filedialog 
from PIL import Image, ImageTk
import cv2
import imutils
 

def finalizarJugadores():
    global cap_jugadores
    cap_jugadores.release()


def visualizarJugadores():
    global cap_jugadores
    global trained_face_data
    if cap_jugadores is not None:
        ret, frame = cap_jugadores.read() 
        if ret == True:
            grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
            

            for (x, y, w, h) in face_coordinates:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                the_face = frame[y: y + h, x: x + w]
                
                face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

                smile_coordinates = trained_smile_detector.detectMultiScale(face_grayscale, scaleFactor = 1.7, minNeighbors = 20)


                for(x_, y_, w_, h_) in smile_coordinates:
                    cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 2)

                    if len(smile_coordinates) > 0:
                        cv2.putText(frame, 'smiling', (x, y + h + 40), fontScale = 3, fontFace = cv2.FONT_HERSHEY_PLAIN, color = (255,255,255))




            frame = imutils.resize(frame, width=640, height= 480)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lbl_jugadores.configure(image=img)
            lbl_jugadores.image = img

            lbl_jugadores.after(10, visualizarJugadores)
        else: 
            lbl_jugadores.image = ""
            cap_jugadores.release()   

def iniciarJugadores():
    global cap_jugadores
    cap_jugadores = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizarJugadores()

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read() 
        if ret == True:
            frame = imutils.resize(frame, width=640, height= 480)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lbl_video.configure(image=img)
            lbl_video.image = img
            lbl_video.after(30, visualizar)
        else: 
            lbl_info_video_path.configure(text="Aun no se ha seleccionado un video")
            lbl_video.image = ""
            cap.release()

def elegirVideo():
    global cap
    if cap is not None:
        lbl_video.image = ""
        cap.release()
        cap = None
    video_path = filedialog.askopenfilename(filetypes= [
        ("all video format", ".mp4"),
        ("all video format", ".avi")])
    if len(video_path) > 0:
        lbl_info_video_path.configure(text=video_path)
        cap = cv2.VideoCapture(video_path)
        visualizar()
    else:
        lbl_info_video_path.configure(text="Aun no se ha seleccionado un video")



cap = None
cap_jugadores = None
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trained_smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

root = Tk()

btn_visualizar_video = Button(root, text="Elegir y visualizar video", command=elegirVideo)
btn_visualizar_video.grid(column=0, row=0, padx=5, pady=5, columnspan= 2)

lbl_info_video = Label(root, text = "Video de entrada: ")
lbl_info_video.grid(column=0, row=1)

lbl_info_video_path = Label(root, text = "Aun no se ha seleccionado un video")
lbl_info_video_path.grid(column=1, row=1)



lbl_video = Label(root)
lbl_video.grid(column=0, row=4, columnspan=2)


btn_iniciar_jugadores = Button(root, text = "Iniciar", command=iniciarJugadores)
btn_iniciar_jugadores.grid(column=20, row=0, padx=2, pady=2)

btn_finalizar_jugadores = Button(root, text = "Finalizar", command=finalizarJugadores)
btn_finalizar_jugadores.grid(column=21, row=0, padx=2, pady=2)

lbl_info_jugadores = Label(root, text = "A continuacion se muestran los jugadores")
lbl_info_jugadores.grid(column=20, row=1)

lbl_jugadores = Label(root)
lbl_jugadores.grid(column=20, row=4, columnspan=2)


root.mainloop()