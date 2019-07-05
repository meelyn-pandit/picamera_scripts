# import picamera

# camera = picamera.PiCamera(resolution=(640, 480))
# camera.start_recording('1.h264')
# camera.wait_recording(5)
# for i in range(2, 11):
    # camera.split_recording('%d.h264' % i)
    # camera.wait_recording(5)
# camera.stop_recording()

import picamera

camera = picamera.PiCamera(resolution=(640, 480))
for filename in camera.record_sequence(
        '%d.h264' % i for i in range(1, 11)):
    camera.wait_recording(5)