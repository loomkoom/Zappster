# Zappster
Flask webapp to send AR greeting cards.
Hosted with Pythonanywhere


## Setup

### Set up flask on Pythonanywhere
1. Go to the web tab and add a new web app
   - select flask > python 3.8
   - choose the following path (same folder name as repo)
   `/home/<username>/Zappster/flask_app.py`
   
2. Change the working directory of the app to:
  `/home/<username>/Zappster` (to access the database from the same folder as the webapp)
  ![](https://i.imgur.com/I8e2MZu.png)
  
3. Optional: If your flask app is not called `flask_app.py`, edit the WSGI file (`/var/www/<username>_pythonanywhere_com_wsgi.py`): 
    - Change `flask_app.py` > `<flask app file name>`
    
4. Add a path for static files
  `/static/` > `/home/<username>/Zappster/static/`
  ![](https://i.imgur.com/cWSV0Df.png)
  
### Clone the repo
1. Open a pythonanywhere bash console \
  ![](https://i.imgur.com/jNeYvUF.png)

2. (if your repository is private)
    generate SSH keys (no password is fine)
      ```bash
      ssh-keygen -t ed25519
      ```
    Copy this SSH key into your github account settings for access via the console
      ```bash
      cat .ssh/id_ed25519.pub
      ```
      
3. Remove the default folder and clone the repo in the console
    ```
    rm -rf /home/<username>/Zappster
    git clone git@github.com:loomkoom/Zappster.git
    ```

4. refresh the web app

## Usage
  `git pull` in the bash console whenever you want to keep the website up to date.
  
  ! You might have to delete and recreate the database to solve merge errors.
  see error log: `https://www.pythonanywhere.com/user/<username>/files/var/log/zappsters.pythonanywhere.com.error.log`

In larger projects it's also possible to automate it on the free tier, using github webhooks and an endpoint on your webserver that pulls the updated repo. \
For more info see this tutorial: <https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664>
