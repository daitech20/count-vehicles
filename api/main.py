import cv2
from .vehicle_detector import detect_vehicles , setup_model, display_vehicles

def detect(video):
    model = setup_model(accuracy_level=5)
    cam = cv2.VideoCapture('media/'+str(video.video))

    out = cv2.VideoWriter('media/output/output-' + str(video.id) + '.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (700,600))

    while True:
        _,img = cam.read()
        # img = cv2.resize(img,(520,416))
        try:
            img = cv2.resize(img, (700, 600))
        except:
            break
        detected_boxes,detected_classes,detected_scores = detect_vehicles(img,model)
        display_vehicles(img,detected_boxes,detected_classes,detected_scores)

        out.write(img)
        
    cam.release()
    out.release()
    cv2.destroyAllWindows()

    # video.video_output = out
    video.video_output = 'output/output-' + str(video.id) + '.avi'
    video.save()


