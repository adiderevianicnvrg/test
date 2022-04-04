# support git lfs
apt-get update -y
apt-get install git-lfs -y
git lfs install

# For a more compact command line
echo "export PS1='\w$ '" >> ~/.bashrc

# Prerequisite to use cv2 on cnvrg
apt-get update
apt-get install -y libgl1-mesa-glx



wget https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
unzip -y ninja-linux.zip -d /usr/local/bin/
update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force

export PYTHONPATH=/cnvrg;$PYTHONPATH

apt-get install gettext-base
envsubst < /cnvrg/clearml_template.conf > /cnvrg/clearml.conf
mv /cnvrg/clearml.conf /root
apt-get install psmisc #to enable gpu memory cleanup using fuser -v /dev/nvidia* and then kill -9 PID
envsubst < /cnvrg/clearml_template.conf > /cnvrg/clearml.conf
mv /cnvrg/clearml.conf /root

pip install --extra-index-url https://shared:HF6w0RbukY@packages.allegro.ai/repository/allegroai/simple -U allegroai==3.4.1rc2

# Temporary hack
list_of_files=`ls -d /cnvrg/output/checkpoints/*/*.pth`
for file in $list_of_files
do
  dir_name=`dirname $file`
  link_name="/latest_checkpoint.pth"
  full_link="$dir_name$link_name"
  ln -s $file $full_link
done
