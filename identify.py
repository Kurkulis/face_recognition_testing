import face_recognition
from PIL import Image, ImageDraw

elon_musk = face_recognition.load_image_file('./img/elonmusk/musk-3.jpg')
elon_encoding = face_recognition.face_encodings(elon_musk)[0]

known_face_encodings = [
    elon_encoding
]

known_face_names = [
    "Elon Musk"
]

group_image = face_recognition.load_image_file('./img/elonmusk/group.jpg')

face_locations = face_recognition.face_locations(group_image)
face_encodings = face_recognition.face_encodings(group_image, face_locations)

pil_image = Image.fromarray(group_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unkown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0),
                   outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5),
              name, fill=(255, 255, 255, 255))

del draw

pil_image.show()
