

```zsh
conda create -n new_env_name python=3.10 
conda activate new_env_name

pip install ipykernel jupyter
conda install nb_conda_kernels

python -m ipykernel install --name new_env_name --display-name "Python (myenv)"

# save to file
conda env export > environment.yml
pip freeze >> requirements.txt

```

### Conda Docs
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


conda env remove -n ENV_NAME

https://github.com/Anaconda-Platform/nb_conda_kernels