# Predictor for Biochemical Control in patients with Acromegaly.

We present a SVM model for prediction of biochemical control with first-generation somatostatin receptor ligands for patients with acromegaly that were submitted to surgery. This is a experimental model that should not be used for treatment decision, more tests should be performed. 


## Requirements

* Anaconda or miniconda (recommended)
* Python
  * pandas
  * joblib
  * sklearn
  * Numpy
  
## Installation
1. Anaconda or miniconda:
 Although Anaconda comes with all required python modules, we recommend miniconda since it requires less disk space. Download an instaler compatible with your system 
 on https://docs.conda.io/en/latest/miniconda.html#linux-installers.
 
    * Windows: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/windows.html.
    
    * Linux: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/linux.html.
    
    * macOS: Follow the instructions on https://conda.io/projects/conda/en/latest/user-guide/install/macos.html.
    
    
2. Enviroment creation:
After installing miniconda, execute the anaconda prompt and use the command bellow to create an enviroment with required packages, you can substitute AcroBCpred for any other name. 
```sh
conda create -n AcroBCpred python=3.6 scikit-learn==0.23.1 pandas numpy joblib 
```

3. Download the repository and extract the AcroPred to your user folder then follow the commands on the intructions text file (that will be the same as the displayed in the next item). AcroPred folder contains: intructions.txt, control_prediction.py and SVM7acro_model_final.sav (which is the trained model and could be used along with any other code). Follow the next steps to download the repository locally.

 * Run the anaconda prompt and activate the enviroment:
 ```sh
      conda activate AcroBCpred
 ```
 
 * Get the repository locally
 
  ```sh
      git clone https://github.com/rlymiranda/AcroBC.git
  ```


      
## Usage 
Running the commands bellow will allow the use for predictions on single samples.

1- conda activate AcroBCpred

2- python ./AcroBC/AcroPred/control_prediction.py

3- Fill the information as instructed










