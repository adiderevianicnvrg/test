"""
Task A python file
"""
from PIL import Image, ImageDraw
from cnvrg import Experiment 
import time
import random
import argparse                                                                 

parser = argparse.ArgumentParser(description='Task A example in cnvrg Flow')         
parser.add_argument('--partition', help='partition', default='1') 
args = parser.parse_args()                                                      

partition = int(args.partition)

# Initialize experiment
e = Experiment()

# Log parameter (single value) that can be accessed in further tasks
random_accuracy = random.random()
print('Creating random accuracy tag', random_accuracy)
e.log_param('random_accuracy', random_accuracy)

# Log metric (chart) that will be automatically visualized in the task's 
# experiment page
print('Creating chart: random-chart')
for i in range(200):
    print(str(i) + '/ 200')
    e.log_metric('random-chart', [random.random()])
    time.sleep(0.1)


# Create artifacts and save to disk so it will be automatically stored by cnvrg
# and available in the next tasks

# Create image file
print('Creating image file')
img = Image.new('RGB', (100, 30), color = (73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World!", fill=(255,255,0))
img.save('task-a-image-artifact.png')

# Create text file
print('Creating text file')
file = open("task-a-text-artifact.txt", "w") 
file.write("Text file generated in Task\nPartition: " + str(partition)) 
file.close() 
 
