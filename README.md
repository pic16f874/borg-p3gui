# How to install Bord server
``` Install borg server (on Hetzner dedicated Ubuntu20.04)
apt update
# run ansible provisionig here, without borgmatic role
 
# if you install borg as binary it not works properly in "borg serve" mode
# not properly installed borg return error "permission denied(publickey)"
# - not clear to understand what happened.
# please install package borgbackup and dependencies instead binary
#
  
useradd -m borg -d /opt/compname/borg
mkdir /opt/compname/borg/.ssh
 
echo 'command="/usr/bin/borg serve" ssh-rsa AAAABz...JvsP rsync_id_rsa.pub'  >> /opt/compname/borg/.ssh/authorized_keys
echo 'ssh-rsa AAAAB3...NgMX rsync_ls_id_rsa.pub' >> /opt/compname/borg/.ssh/authorized_keys
 
chown -R borg:borg /opt/compname/borg/
 
apt install python3 python3-dev python3-pip libssl-dev openssl libacl1-dev libacl1 build-essential
apt install libfuse-dev fuse pkg-config
apt install borgbackup

```



