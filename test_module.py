# def foo():
#     var = False
#     var1 = True
#     if var1:
#         # nonlocal var
#         var = True
#         print(var)
#
# # foo()
#
# import os
#
# def on_created():
#     ''' Called when the media is inserted '''
#     # usb_path = s.get(['usb', 'folder'])
#     usb_path = 'None'
#     expected_paths = ['/media/usb0', '/media/usb1', '/media/usb2', '/media/usb3', '/media/usb4']
#     for path in expected_paths:
#         if len(os.listdir(path)) > 0:
#             usb_path = path
#             break
#     print("USB found at " + usb_path)

# on_created()

# print(os.path.isfile('/home/toran/Desktop/test2.txt'))

import glob

for i in glob('/home/toran/Desktop'):
    print(i)