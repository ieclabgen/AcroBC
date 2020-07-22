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
    
2. Enviroment creation:
After installing miniconda, execute the anaconda prompt and use the command bellow to create an enviroment with required packages, you can substitute RFacro for any other name. 
```sh
conda create -n RFacro python=3.6 scikit-learn pandas numpy joblib 
```
      
## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```
## Meta

[https://github.com/yourname/github-link](https://github.com/dbader/)





