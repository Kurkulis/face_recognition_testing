import face_recognition

elon_musk = face_recognition.load_image_file('./img/elonmusk/musk-3.jpg')
elon_encoding = face_recognition.face_encodings(elon_musk)[0]

unkown = face_recognition.load_image_file(
    './img/elonmusk/91263a74-211d-310e-b5c6-11645b7ec4b6.jpeg')
unkown_encoding = face_recognition.face_encodings(unkown)[0]

results = face_recognition.compare_faces([elon_encoding], unkown_encoding)

if results[0]:
    print('This is Elon')
else:
    print('No no no')
