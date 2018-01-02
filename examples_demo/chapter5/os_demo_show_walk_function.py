# -*- coding:utf-8 -*-
# Author: qjk

import os


label_map = {
    'openCV_GUI': 0,
    'Core_Operations': 1,
    'Image_Process': 2,
    '.idea': -1,
    '.git': -1
}

with open('data.txt', 'w') as f:
    for root, dirs, files in os.walk("/home/qjk/PycharmProjects/openCV/"):
        print(root)
        for filename in files:
            filepath = os.sep.join([root, filename])
            dirname = root.split(os.sep)[-1]
            if dirname in ['openCV_GUI', 'Core_Operations', 'Image_Process']:
                label = label_map[dirname]
                line = '{},{}\n'.format(filepath, label)
                f.write(line)