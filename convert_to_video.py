####### Code from https://stackoverflow.com/a/62434934/15602544  #######

import os
import moviepy.video.io.ImageSequenceClip

EXPERIMENT_NAME = 'tag_with_clst_3'
# EXPERIMENT_NAME = 'tag_baseline'
RUN_NAME = 'simple_tag/exp_0608/run4'
RENDER_DIR = os.path.join('models', RUN_NAME ,'rendered_images')

fps = 2

image_files = [os.path.join(RENDER_DIR,img)
               for img in os.listdir(RENDER_DIR)
               if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(EXPERIMENT_NAME + '.mp4')

