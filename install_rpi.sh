
# clone repos

BRAIN_FOLDER="brain"
FACE_FOLDER="face"

echo Deleting previous folder
rm -rf $BRAIN_FOLDER $FACE_FOLDER

echo Fetching repos from git
git clone https://github.com/sebastien-lb/alfred-brain.git $BRAIN_FOLDER
git clone https://github.com/sebastien-lb/alfred-face.git $FACE_FOLDER

# installing deps 

if node --version >/dev/null 2>&1 ; then
    echo "nodejs found"
    echo "version: $(node --version)"
else
    echo "nodejs not found, installing it"
    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
    sudo apt install -y nodejs
    echo "version: $(node --version)"

fi 

if python3 --version >/dev/null 2>&1 ; then
    echo "python3 found"
    echo "python3: $(python3 --version)"
else
    echo "python3 not found, trying python"
    if python --version > /dev/null 2>&1 ; then
        echo "python found"
        echo "python: $(python --version)"
    else 
        echo "python not found"
    fi
fi 


echo installing repo deps
cd $FACE_FOLDER 
npm install
cd ..
cd $BRAIN_FOLDER
python -m venv .
source ./bin/activate
pip install r requirements.txt





