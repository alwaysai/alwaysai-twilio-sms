import time
import edgeiq
import socketio
import requests

"""
Use object detection to detect objects in the frame in realtime. The
types of objects detected can be changed by selecting different models.

To change the computer vision model, follow this guide:
https://docs.alwaysai.co/application_development/application_configuration.html#change-the-computer-vision-model

To change the engine and accelerator, follow this guide:
https://docs.alwaysai.co/application_development/application_configuration.html#change-the-engine-and-accelerator
"""


def main():

    client_socket = ClientSocket()
    target = 'chair'

    obj_detect = edgeiq.ObjectDetection(
        "alwaysai/mobilenet_ssd")
    obj_detect.load(engine=edgeiq.Engine.DNN)

    print("Loaded model:\n{}\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Labels:\n{}\n".format(obj_detect.labels))

    fps = edgeiq.FPS()

    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            # loop detection
            while True:
                frame = video_stream.read()
                results = obj_detect.detect_objects(frame, confidence_level=.5)
                frame = edgeiq.markup_image(
                    frame, results.predictions, colors=obj_detect.colors)

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                    "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for prediction in results.predictions:
                    if target == prediction.label:
                      client_socket.labels(prediction.label)


                    text.append("{}: {:2.2f}%".format(
                        prediction.label, prediction.confidence * 100))

                streamer.send_data(frame, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


class ClientSocket():
    sio = socketio.Client()

    @sio.event
    def connect():
        print('connection established')

    @sio.event
    def labels(self, data):
        self.sio.emit('labels', {'response': data})

    @sio.event
    def disconnect():
        print('disconnected from server')

    sio.connect('http://localhost:3001')


if __name__ == "__main__":
    main()
