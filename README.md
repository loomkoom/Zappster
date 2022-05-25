# Zappster

## Setup
1. Open a pythonanywhere bash console

  ![](https://i.imgur.com/jNeYvUF.png)
  
3. generate SSH keys (no password is fine)
  ```bash
  ssh-keygen -t ed25519
  ```
3. Copy this key into your github for access via the console
  ```bashp
  cat .ssh/id_ed25519.pub
  ```
4. Clone the repo in the console
  ```
  git clone git@github.com:loomkoom/Zappster.git
  ```
5. Go to the web tab and add a new web app
 - select flask > python 3.8
 - choose the following path
 `/home/<username>/Zappster/default_app.py`
6. Change the working directory of the app to:
  `/home/<username>/Zappster`
  ![](https://i.imgur.com/npXYqpu.png)
7. Add a path for static files
  `/static/` > `/home/<username>/Zappster/static/`
  ![](https://i.imgur.com/ACsvixB.png)
