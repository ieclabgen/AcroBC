import os
import numpy as np
import joblib

model = joblib.load(os.getcwd() + '\\demo\\RFacro_model_final.sav')

#  Insert sst2 value(0 or 1): 0 = normal or low |  1 = high

cam5 = input('Insert CAM5.2 value(0 = normal or low | 1 = high): ')
sst2 = input('Insert sst2 value(0 = normal or low |  1 = high): ')
age_diag = input('Insert the age at diagnosis: ')
gh_diag = input('Insert Gh levels at diagnosis: ')
gh_pre = input('Insert Gh levels before initiating treatment: ')
igf_pre = input('Insert IGF-1 before initiating treatment: ')

data = [[int(sst2), int(cam5), int(age_diag), float(gh_diag), float(gh_pre), float(igf_pre)]]

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
print ('\nWith given parameters the patient have a {:.2%} chance to be -{}- after treatment'.format(probability, result))