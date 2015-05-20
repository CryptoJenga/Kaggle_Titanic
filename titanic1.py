import numpy as np
import csv as csv

train_csv_file_object = csv.reader(open('data/train.csv', 'rb')) 
train_header = train_csv_file_object.next() 
train_data=[] 

for row in train_csv_file_object:
    train_data.append(row)
train_data = np.array(train_data) 


train_sex = train_data[0::,4]
train_survived = train_data[0::, 1]
train_passenger_id = train_data[0::, 0]


sex_total = [0,0]
sex_survived = [0,0]

for i in range(len(train_passenger_id)):
  if (train_sex[i] == "female"):
    sex_total[0] += 1
    if (train_survived[i] == "1"):
      sex_survived[0] += 1

  if (train_sex[i] == "male"):
    sex_total[1] += 1
    if (train_survived[i] == "1"):
      sex_survived[1] += 1

sex_ratio = [(1.0 * sex_survived[0]) / sex_total[0], (1.0 * sex_survived[1]) / sex_total[1]]




test_csv_file_object = csv.reader(open('data/test.csv', 'rb')) 
test_header = test_csv_file_object.next() 
test_data=[] 

for row in test_csv_file_object:
    test_data.append(row)
test_data = np.array(test_data) 


test_sex = test_data[0::,3]
test_passenger_id = test_data[0::, 0]

prediction = [["PassengerId","Survived"]]
for i in range(len(test_passenger_id)):
  result = 0

  if (test_sex[i] == "female" ):
    if (sex_ratio[0] >= 0.5):
      result = 1

  if (test_sex[i] == "male"):
    if (sex_ratio[1] >= 0.5):
      result = 1

  prediction.append([test_passenger_id[i], result])


with open("output.csv","wb") as f:
  writer = csv.writer(f)
  writer.writerows(prediction)
