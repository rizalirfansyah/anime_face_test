import face_recognition
from PIL import Image, ImageDraw

image_of_souma = face_recognition.load_image_file('./img/known/Yukihira Souma.jpg')
souma_face_encoding = face_recognition.face_encodings(image_of_souma)[0]
image_of_eren = face_recognition.load_image_file('./img/known/Eren Jaeger.png')
eren_face_encoding = face_recognition.face_encodings(image_of_eren)[0]
image_of_senku = face_recognition.load_image_file('./img/known/ishigami Senku.jpg')
senku_face_encoding = face_recognition.face_encodings(image_of_senku)[0]
image_of_itadori = face_recognition.load_image_file('./img/known/Itadori Yuuji.jpg')
itadori_face_encoding = face_recognition.face_encodings(image_of_itadori)[0]
image_of_killua = face_recognition.load_image_file('./img/known/Killua zoldyck.jpg')
killua_face_encoding = face_recognition.face_encodings(image_of_killua)[0]
image_of_naruto = face_recognition.load_image_file('./img/known/Uzumaki Naruto.jpg')
naruto_face_encoding = face_recognition.face_encodings(image_of_naruto)[0]

TOLERANCE = 0.45

known_face_encodings = [
    souma_face_encoding,
    eren_face_encoding,
    senku_face_encoding,
    itadori_face_encoding,
    killua_face_encoding,
    naruto_face_encoding
]

known_face_names = [
    "Yukihira Souma",
    "Eren Jaeger",
    "Ishigami Senku",
    "Itadori Yuuji",
    "Killua Zoldyck",
    "Uzumaki Naruto"
]

test_image = face_recognition.load_image_file('./img/unknown/87399.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, TOLERANCE)

    name = "Unknown Character"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0),
               outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

pil_image.show()
