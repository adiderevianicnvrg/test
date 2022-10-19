from cnvrg import Experiment
import argparse
import os

parser = argparse.ArgumentParser(description='Task B example in cnvrg Flow')         
parser.add_argument('--task_a_accuracy', help='accuracy', default='1') 
args = parser.parse_args()                                                      

accuracy = float(args.task_a_accuracy)
    
# Print previous task accuracy (passed as parameter with `{{ }}`)
print('Previous task accuracy: ', accuracy)

# Read parameter from previous task using environment variables
# https://app.cnvrg.io/docs/core_concepts/flows.html#tags-parameters-flow
print('Previous task partitions: ', os.environ['CNVRG_TASK_A_PARTITION'])

# Read & print text file from previous task
f = open('/input/task_a/task-a-text-artifact.txt')
print("task_a's text file contents:")
print(f.read())
f.close()
