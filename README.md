# Feature Selection Evalulation on Physio MIMIC III
Author: Matthew Davis


## Objective
To investigate different features selection methods on clincal data. This project uses a variety of feature selection methods to reduced a feature set derived from max /min  labs collected during hosptial intatient encounters and classifiers probablity of the patient expiring in the hosptial.  



## Project Setup
This projects requires Mimic III Clincal Data as a data sources, features seletion methods, autoML and Mlflow tracking repo
to be reproducable


#### Data Source
Download Physio MIMIC III v 1.4 and unzip csvs
+ run csv_to_parquet.py to create parquet copies on MIMIC III (for faster transfomration later)
    Edit paths as needed
+ set an environmental variable PHYSIO_HOME to the directory with the parquet file  

#### Tracking Server

Start an MLFLOW Tracking Server (wiill create a sqllite db to store run links)

```sh
mlflow server --backend-store-uri sqlite:///mydb.sqlite --default-artifact-root ~/mlruns
```

#### Feature Selection Methods
to get pyCausalFS feature Selection methods, clone from git into the ml director (to keep imports from breaking)


```sh

link here
```

#### Requirments from pypi
    pyspark==3.1.2
    mlflow==1.15.0
    evalml==0.25.0
    boruta  ## for feature selection
    PyImpetus ## for feature selection
    pyCausalFS ## for feature selection (needs to be cloned manually from git into the ml directory)
    
