import os
import numpy as np
import joblib

model = joblib.load(os.getcwd() + '\\AcroBC\\AcroPred\\SVM7acro_model_final.sav')



age = input('Insert the age of diagnosis: ')
sex = input('Insert patients gender (0 = Female | 1 = Male): ')
cam5 = input('Insert CAM5.2 value(0 = sparsely granulated | 1 = densely granulated): ')
sst2 = input('Insert SST2 value: ')
sst5 = input('Insert SST5 value: ')
gh_pre = input('Insert Gh levels before initiating treatment: ')
igf_pre = input('Insert IGF-1 before initiating treatment: ')

data = [[int(cam5), int(sst2), int(sst5), int(sex), int(age), float(gh_pre), float(igf_pre)]]

prediction = model.predict(data)
result = ''
if prediction[0] == 0:
    result = 'not controled'
else:
    result = 'controled'

proba = model.predict_proba(data)

if prediction[0] == 0:
    result = 'not controled'
    probability = proba[0][0]
else:
    result = 'controled'
    probability = proba[0][1]
print ('\nWith given parameters the patient has a {:.2%} chance to be -{}- after treatment'.format(probability, result))
