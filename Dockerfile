### NUM-ENV

### Используйте базовый образ Python
FROM continuumio/miniconda3

### Копирование зависимостей проекта
#ADD environment.yml /tmp/environment.yml

### Install Conda environment from environment.yml

# pip install virtualenv
# virtualenv -p python3 num-env
# source num-env/bin/activate
RUN pip install pandas
RUN pip install openpyxl
RUN pip install ipykernel
RUN pip install seaborn
RUN pip install scipy
RUN pip install mlxtend
# Pull the environment name out of the environment.yml
# RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
# ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

### Copy your project files into the container
COPY . /data

### Activate the virtual environment
# SHELL ["python3", "run", "-n", "amazon-bot-env"]
# SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

### Command to be executed when the container is run
CMD [ "python3", "main.py" ]
     
