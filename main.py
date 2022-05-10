import cv2

<<<<<<< Updated upstream
#Load opencv pre-trained data on face frontals (haar cascade algorithm)
=======
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

                the_face = (x, y, w, h)
                
                face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

                smile_coordinates = trained_smile_detector.detectMultiScale(face_grayscale, scaleFactor = 1.7, minNeighbors = 20)


                for(x_, y_, w_, h_) in smile_coordinates:
                    cv2.rectangle(frame, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 2)


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
            lbl_video.after(10, visualizar)
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
>>>>>>> Stashed changes
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trained_smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

#Choose an image to detect faces in
img = cv2.imread('RDJ.png')

#Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#To detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangles around the faces
cv2.rectangle(img, (220, 143), (220+219, 143+219), (0, 255, 0), 2)

print(face_coordinates)

#To show img
cv2.imshow('Clever Programmer Face Detector', img)

#In order to pause the execution of the code to be able to se img
cv2.waitKey()

print("Code Completed")