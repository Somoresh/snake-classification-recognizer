from fastai.vision.all import load_learner
import gradio as gr

# import pathlib
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

snake_labels = {
    "Python",
    "Rattle",
    "Cobra",
    "Anaconda",
    "Black Mamba",
    "King Cobra",
    "Coral Snake",
    "Water Snake",
    "Sea Snake",
    "Bushmaster",
    "Rat Snake",
    "Parot Snake",
    "Lora"


}
model =load_learner('models/snake-recognizer-v1.pkl')


def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(snake_labels, map(float, probs)))



image = gr.Image()
label = gr.Label()
examples = [

    'test_images/test_image1.jpg',
    'test_images/test_image2.jpg',
    'test_images/test_image3.jpg',
    'test_images/test_image4.jpg',
    'test_images/test_image5.jpg',
    'test_images/test_image6.jpg',
    'test_images/test_image7.jpg',
    'test_images/test_image8.jpg',
    'test_images/test_image9.png',
    'test_images/test_image10.jpg',
    'test_images/test_image11.JPG',
    'test_images/test_image12.jpg',

    ]
iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False, share=True)
