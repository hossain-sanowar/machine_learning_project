# machine_learning_project
End-End Machine Leaning Project

Project Name: House Price Prediction

Requirement:
1. Github link
2. VsCode IDE
3. Heroku Account
4. GIT cli
5. Creating conda environment

```
conda --version
conda create -p venv python==3.9 -y
conda activate venv/
```

```
pip install -r requirements.tx

```
> Git Comand files
```
git --version
git clone
git add . #to Add files in git
git add <file name>
git status
git log
git commit -m 'message' #to create version/commit all changes in git
git push origin main #to send version/changes to GitHub
git remote -v #to check remote URL status
git pull #all the missing file update in the local system
```

Build DOCKER Image
```
docker build -t <image_name>:<tagname> #build image; image name for docker must be lowercase
docker build -t ml_project .
docker images #to show the list of docker images
docker run -p 5000:80 -e PORT=5000 <image id> #run docker image
docker run -d -p 8000:8000 -e PORT=8000 52879125fe4b #running docker images and working
docker ps #check running container status
docker ps -a # all project running container status
docker stop container_id #stop container
docker stop 0cc6448810ee
```