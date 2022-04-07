
1. Install XCode Developer Tools
2. Install Homebrew
```
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/devos/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

From here, any installs should ideally be done through `homebrew`.

If you have ever installed any GUI software on Mac the “standard way,” you probably know that it normally requires downloading the package, opening it, and installing by the drag-and-drop method to the Application folder. Homebrew, by default, can only install command-line tools.

Homebrew Cask is a Homebrew extension for installing GUI software on Mac. It means that instead of the standard download and drag-and-drop process, you can use this.

`brew install --cask <package_name>`

3. install vscode

```
brew install --cask vscode
```

4. install Git (if not already done) and set up github

```
git config --global user.name "Your Name Here"
git config --global user.email "your_email@youremail.com"
```
This will get added to your `.gitconfig` file on your home directory. Note: files starting with `.` are often hidden on most OS)

To prevent git from asking for your username and password every time you push a commit you can cache your credentials by running the following command:
```
git config --global credential.helper osxkeychain
```

If you don't want to push it to your keychain and/or don't have a Mac you can cache them and give a timeout period like so:

```
git config --global credential.helper cache
# or
git config --global credential.helper 'cache --timeout=600'
```

This will allow you to clone a repository like so:
```
git clone https://github.com/<username>/<repo-name>.git
```

To set up Git/Github for SSH, you can go here:
https://sourabhbajaj.com/mac-setup/Git for more info.


For SSH:
```
ssh-keygen -t rsa -b 4096 -C "your@email.com" -f ~/.ssh/id_rsa_personal

```
Copy the contents from the id_rsa_persona.pub file into Github SSH Keys (e.g. https://github.com/settings/ssh)

```
# create .ssh/config if doesn't exist
touch .ssh/config

# add to the file and save.
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519

# Add your SSH private key to the ssh-agent and store your passphrase in the keychain 

ssh-add -K ~/.ssh/id_rsa_personal
```





5. install [pyenv](https://gist.github.com/josemarimanio/9e0c177c90dee97808bad163587e80f8)

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

eval "$(pyenv init --path)"
eval "$(pyenv init -)"

To fix this message, add these lines to the '.profile' and '.zprofile' files
in your home directory:

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

6. install conda (miniconda)

brew install --cask miniconda
conda init zsh

7. install docker


```
# for MacOS M1 Chips Install (https://docs.docker.com/desktop/mac/install/)
softwareupdate --install-rosetta

# install Docker Engine
brew install docker

# install Docker Machine
brew install docker-machine

# install VirualBox
brew install --cask virtualbox

# for docker to work you need to go to the "Applications" folder and click on the docker app to start it and it will work

# test it works
docker run hello-world
```


7. brew install --cask dbngin

8. brew install --cask obs


### Other Goodies for ZSH
https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dotenv


### VS Code Extensions

- Thunder Client (REST API Client)
- Remote Containers (Docker)
- aws toolkit
- aws boto3
- terraform
- GitLens
- Docker
- Live Server
- Markdown PDF
- Paste JSON as Code
- Rainbow CSV
- vscode-icons


### Python Specific
- autoDocstring
- Python
- Jupyter
- Jupyter Notebook Renderers
- Python Extension Pack
  - Python Extended
  - Python Environment Manager