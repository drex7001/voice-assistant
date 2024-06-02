# import pyperclip

# def get_clipboard_text():
#     clipboard_content = pyperclip.paste()
#     if isinstance(clipboard_content,str):
#         return clipboard_content
#     else:
#         print("Error: Clipboard content is not a string")
#         return None


# print(get_clipboard_text())






# import cv2

# web_cam = cv2.VideoCapture(0)

# def web_cam_capture():
#     if not web_cam.isOpened():
#         print("Error opening video stream or file")
#         exit()

#     path = 'webcam.jpg'
#     ret, frame = web_cam.read()
#     cv2.imwrite(path, frame)

# web_cam_capture()













# from PIL import ImageGrab

# def take_screenshot():
#     path = 'screenshot.jpg'
#     screenshot = ImageGrab.grab()
#     rgb_screenshot = screenshot.convert('RGB')
#     rgb_screenshot.save(path,quality=15)


# take_screenshot()