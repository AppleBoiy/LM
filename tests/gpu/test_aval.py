#!/usr/bin/env python3

import tensorflow as tf

gpu_av = tf.config.list_physical_devices('GPU')
if gpu_av:
    print(f"Found {len(gpu_av)}")
    for g in gpu_av:
        print(g)
else:
    print("not found")
