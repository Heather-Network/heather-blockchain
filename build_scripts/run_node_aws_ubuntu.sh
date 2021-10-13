#!/bin/bash
# based on the example in https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
# Note - Although this updates linux, it does not reboot the server, it does not start
# start heather at boot and it runs as root, so not ideal!
# Anywho, this is what we use for now to inject into the instance.
# TODO: Set up to reboot and start the node on reboot.  we don't want to provision every boot as the blockchain grows.
# or we could store blockchain versions in a git-repo (no, it's too big)
apt-get install git -y
git clone https://www.github.com/Heather-Network/heather-blockchain
cd heather-blockchain/
git checkout main
sh install.sh
. ./activate
heather init
heather configure -log-level INFO
heather init --fix-ssl-permissions
mkdir -p ~/.heather/mainnet/db/
wget www.heathernetwork.io/downloads/blockchain_v1_mainnet.sqlite -P ~/.heather/mainnet/db/
heather start node
sleep 5m
apt update -y && sudo apt upgrade -y
