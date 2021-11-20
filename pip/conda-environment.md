
# create new conda env
```shell
conda create -n env_name
conda activate env_name


```

## environment file
```shell
conda env export > environment.yml

# when create env, it was not working, update conda version. and try --no-builds 
conda env export  --no-builds > environment.yml

# create env by yml file
conda env create -f environment.yml
```

## etc
```shell
# update conda version
conda update -n base -c defaults conda
conda deactivate
conda info --envs 
conda env remove --name env-name
```