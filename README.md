# Predictor for Biochemical Control in Acromegallic patients.

We present a Random forest model for prediction of biochemical control of 
patients with acromegally that were submitted to surgery. This is a experimental model
that should not be used for treatment decision, more tests should be performed. 


## Requirements

* Anaconda or miniconda (recommended)
* Python
  * pandas
  * joblib
  * sklearn
  * Numpy
  
## Installation
1. Anaconda or miniconda:
 Although Anaconda comes with all required python modules, we recommend miniconda since it requires less disk space. Download an instaler compatible with you system 
 on https://docs.conda.io/en/latest/miniconda.html#linux-installers.
 
    * Windows: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/windows.html.
    
    * Linux: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/linux.html.
    
    * macOS: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/macos.html.
    
    
2. Enviroment creation:
After installing miniconda, execute the anaconda prompt and use the command bellow to create an enviroment with required packages, you can substitute RFacro for any other name. 
```sh
conda create -n RFacro python=3.6 scikit-learn pandas numpy joblib 
```

3. Download the folder AcroRF from this repository and put it in your user folder then follow the commands on the intructions text file (that will be the same as the displayed in the next item). AcroRF folder contains: intructions.txt, rf_prediction.py and RFacro_model_final.sav (which is the trained model and could be used along with any other code.


      
## Usage 
Running the commands bellow will allow the use for predictions on single samples.

1- conda activate RFacro

2- python ./AcroRF/rf_prediction.py

3- Fill the information as instructed










