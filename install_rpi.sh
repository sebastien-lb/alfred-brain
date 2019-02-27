
# clone repos

BRAIN_FOLDER="brain"
FACE_FOLDER="face"

# echo Deleting previous folder
# rm -rf $BRAIN_FOLDER $FACE_FOLDER

echo "Fetching repos from git"
if [ -d "$BRAIN_FOLDER" ]; then
    echo "A folder named $BRAIN_FOLDER already exists"
    echo "Do you wish to remove it? (y/n)"
    read -r -p "" yn
    case $yn in
        [Yy]* ) echo "removing it.."; 
                rm -rf $BRAIN_FOLDER; 
                git clone https://github.com/sebastien-lb/alfred-brain.git $BRAIN_FOLDER; 
                break;;
        [Nn]* ) echo "Not removing it, exiting script"; exit;;
        * ) echo "Please answer yes or no."; exit;;
    esac
else 
    git clone https://github.com/sebastien-lb/alfred-brain.git $BRAIN_FOLDER
fi

if [ -d "$FACE_FOLDER" ]; then
    echo "A folder named $FACE_FOLDER already exists"
    echo "Do you wish to remove it? (y/n)"
    read -r -p "" yn
    case $yn in
        [Yy]* ) echo "removing it.."; 
                rm -rf $FACE_FOLDER; 
                git clone https://github.com/sebastien-lb/alfred-face.git $FACE_FOLDER; 
                break;;
        [Nn]* ) echo "Not removing it, exiting script"; exit;;
        * ) echo "Please answer yes or no."; exit;;
    esac
else 
    git clone https://github.com/sebastien-lb/alfred-face.git $FACE_FOLDER
fi

# git clone https://github.com/sebastien-lb/alfred-brain.git $BRAIN_FOLDER
# git clone https://github.com/sebastien-lb/alfred-face.git $FACE_FOLDER

# installing deps 

if node --version >/dev/null 2>&1 ; then
    echo "nodejs found"
    echo "version: $(node --version)"
else
    echo "nodejs not found, installing it"
    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
    sudo apt install -y nodejs
    sudo apt install xsel
    echo "version: $(node --version)"

fi 

if python3 --version >/dev/null 2>&1 ; then
    echo "python3 found"
    echo "python3: $(python3 --version)"
else
    echo "python3 not found, installing it"
    sudo apt-get install -y python3
    apt install -y libmysqlclient-dev
    sudo apt-get install python-virtualenv
    echo "python3: $(python3 --version)"
fi 

install_deps() {
    set_up_bdd()
    echo "installing repo deps"
    cd $FACE_FOLDER
    npm install
    npm build
    cd ../$BRAIN_FOLDER
    virtualenv --python=/usr/bin/python3 venv
    source ./venv/bin/activate
    pip install --upgrade setuptools
    pip install -r requirements.txt
    python manage.py migrate
    deactivate
    cd ..
}

set_up_bdd() {
    echo "Setting up bdd, not implementing yet"
    # follow
    # https://www.a2hosting.com/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line
    # add password to django conf
}
    

echo "Do you want to install projet dependencies? (y/n)"
read -r -p "" yn
case $yn in
    [Yy]* ) echo "installing..."; install_deps; break;;
    [Nn]* ) echo "Not installing deps"; exit;;
    * ) echo "Please answer yes or no."; exit;;
esac







