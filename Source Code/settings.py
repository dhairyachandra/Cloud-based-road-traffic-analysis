'''
App settings.
'''

import os
import ast


ENVS_READY = True

# Specify if video capture is from a camera
try:
    IS_CAM = ast.literal_eval(os.getenv('IS_CAM', 'False'))
except ValueError:
    print('Invalid value for IS_CAM. It should be either True or False.')
    ENVS_READY = False

os.environ['DEBUSSY'] = "hihi"
print(os.environ.get('DEBUSSY'))

print(os.getenv('SHOW_COUNTS','okok'))
print(os.environ.get('RECORD'))

# Absolute/relative path to video or camera input
# E.g "./data/videos/sample_traffic_scene.mp4" or 1
if os.getenv('VIDEO','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/videos/sample_traffic_scene.mp4'):
    VIDEO = int(os.getenv('VIDEO','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/videos/sample_traffic_scene.mp4')) if IS_CAM else os.getenv('VIDEO','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/videos/sample_traffic_scene.mp4')
else:
    print('Path to video or camera input not set.')
    ENVS_READY = False

# Specify a detection Region of Interest (ROI)
# i.e a set of vertices that represent the area (polygon) where you want detections to be made
# E.g [(750, 405), (1094, 398), (1569, 1028), (501, 1028)]
# Default: [(0, 0), (frame_width, 0), (frame_width, frame_height), (0, frame_height)] (i.e the whole video frame)
try:
    USE_DROI = ast.literal_eval(os.getenv('USE_DROI', 'True'))
except ValueError:
    print('Invalid value for USE_DROI. It should be either True or False.')
    ENVS_READY = False

if USE_DROI:
    try:
        DROI = ast.literal_eval(os.getenv('DROI','[(750, 405), (1094, 398), (1569, 1028), (501, 1028)]'))
    except ValueError:
        print('Invalid value for DROI. It should be a list of coordinates (2-tuples).')
        ENVS_READY = False

# Display/overlay the detection ROI on the video
try:
    SHOW_DROI = ast.literal_eval(os.getenv('SHOW_DROI', 'True'))
except ValueError:
    print('Invalid value for SHOW_DROI. It should be either True or False.')
    ENVS_READY = False

# Display cumulative counts on the video
try:
    SHOW_COUNTS = ast.literal_eval(os.getenv('SHOW_COUNTS', 'True'))
except ValueError:
    print('Invalid value for SHOW_COUNTS. It should be either True or False.')
    ENVS_READY = False

# Maximum consecutive detection failures i.e number of detection failures
# before it's concluded that an object is no longer in the frame
try:
    MCDF = int(os.getenv('MCDF', '2'))
except ValueError:
    print('Invalid value for MCDF. It should be a positive integer.')
    ENVS_READY = False

# Maximum consecutive tracking failures i.e number of tracking failures
# before the tracker concludes the tracked object has left the frame
try:
    MCTF = int(os.getenv('MCTF', '3'))
except ValueError:
    print('Invalid value for MCTF. It should be a positive integer.')
    ENVS_READY = False

# Detection interval i.e number of frames before detection is carried out again
# (in order to find new vehicles and update the trackers of old ones)
try:
    DI = int(os.getenv('DI', '10'))
except ValueError:
    print('Invalid value for DI. It should be a positive integer.')
    ENVS_READY = False

# Model/algorithm to use for vehicle detection (options: yolo, tfoda, detectron2, haarcascade)
DETECTOR = os.getenv('DETECTOR', 'yolo')

# Algorithm to use for vehicle tracking (options: kcf, csrt)
TRACKER = os.getenv('TRACKER', 'kcf')

# Record vehicle counting as video
try:
    RECORD = ast.literal_eval(os.getenv('RECORD', 'False'))
except ValueError:
    print('Invalid value for RECORD. It should be either True or False.')
    ENVS_READY = False

# Set path where recorded video will be stored
if RECORD:
    if os.getenv('OUTPUT_VIDEO_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/videos/output.mp4'):
        OUTPUT_VIDEO_PATH = os.getenv('OUTPUT_VIDEO_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/videos/output.mp4')
    else:
        print('Output video path not set.')
        ENVS_READY = False

# Run VCS without UI display
try:
    HEADLESS = ast.literal_eval(os.getenv('HEADLESS', 'False'))
except ValueError:
    print('Invalid value for HEADLESS. It should be either True or False.')
    ENVS_READY = False

# Specify one or more counting lines
# A counting line is represented by a label and line segment
# E.g {'label': 'A', 'line': [(667, 713), (888, 713)]}

os.environ['COUNTING_LINES'] = "[{'label': 'A', 'line': [(667, 713), (888, 713)]}, {'label': 'B', 'line': [(1054, 866), (1423, 868)]}]"
print(os.environ.get('COUNTING_LINES'))

if os.getenv('COUNTING_LINES','true'):
    print('------')
    COUNTING_LINES = ast.literal_eval(os.getenv('COUNTING_LINES'))
else:
    print('Invalid value for COUNTING_LINES. It should be a list of lines.')
    ENVS_READY = False

# Configs for YOLO
if DETECTOR == 'yolo':
    if os.getenv('YOLO_WEIGHTS_PATH', 'C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/yolo/yolov3.weights') and \
            os.getenv('YOLO_CONFIG_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/yolo/yolov3.cfg') and \
            os.getenv('YOLO_CLASSES_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/coco_classes.txt') and \
            os.getenv('YOLO_CLASSES_OF_INTEREST_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/coco_classes_of_interest.txt') and \
            os.getenv('YOLO_CONFIDENCE_THRESHOLD','0.5'):
        YOLO_WEIGHTS_PATH = os.getenv('YOLO_WEIGHTS_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/yolo/yolov3.weights')
        YOLO_CONFIG_PATH = os.getenv('YOLO_CONFIG_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/yolo/yolov3.cfg')
        YOLO_CLASSES_PATH = os.getenv('YOLO_CLASSES_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/coco_classes.txt')
        YOLO_CLASSES_OF_INTEREST_PATH = os.getenv('YOLO_CLASSES_OF_INTEREST_PATH','C:/UMKC/2020/Spring_2020/CC/Project/Vehicle Dectection System/data/detectors/coco_classes_of_interest.txt')
        YOLO_CONFIDENCE_THRESHOLD = float(os.getenv('YOLO_CONFIDENCE_THRESHOLD','0.5'))
    else:
        print('YOLO_WEIGHTS_PATH, YOLO_CONFIG_PATH, YOLO_CLASSES_PATH, YOLO_CLASSES_OF_INTEREST_PATH, ' +
              'and/or YOLO_CONFIDENCE_THRESHOLD not set or invalid.')
        ENVS_READY = False

# Log destinations
try:
    ENABLE_CONSOLE_LOGGER = ast.literal_eval(os.getenv('ENABLE_CONSOLE_LOGGER', 'True'))
    ENABLE_FILE_LOGGER = ast.literal_eval(os.getenv('ENABLE_FILE_LOGGER', 'True'))
    ENABLE_LOGSTASH_LOGGER = ast.literal_eval(os.getenv('ENABLE_LOGSTASH_LOGGER', 'False'))
except ValueError:
    print('Invalid value for ENABLE_CONSOLE_LOGGER, ENABLE_FILE_LOGGER ' +
          'and/or ENABLE_LOGSTASH_LOGGER. They should be either True or False.')
    ENVS_READY = False

# Absolute/relative path to log files directory
if ENABLE_FILE_LOGGER:
    LOG_FILES_DIRECTORY = os.getenv('LOG_FILES_DIRECTORY', './data/logs/')

# Log base 64 images
# Logging images will increase the size of your logs significantly
# However, if you intend to do some post-processing that involves images,
# you might want to have it on
try:
    LOG_IMAGES = ast.literal_eval(os.getenv('LOG_IMAGES', 'False'))
except ValueError:
    print('Invalid value for LOG_IMAGES. It should be either True or False.')
    ENVS_READY = False

# Size of window used to view the vehicle counting process
try:
    DEBUG_WINDOW_SIZE = ast.literal_eval(os.getenv('DEBUG_WINDOW_SIZE', '(858, 480)'))
except ValueError:
    print('Invalid value for DEBUG_WINDOW_SIZE. It should be a 2-tuple: (width, height).')
    ENVS_READY = False


if not ENVS_READY:
    raise Exception('One or more environment variables are either invalid or not set. ' +
                    'Please ensure all variables are properly set.')
