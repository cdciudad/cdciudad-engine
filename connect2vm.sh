#!/bin/sh

USERNAME="ubuntu"
HOST="ec2-3-133-145-119.us-east-2.compute.amazonaws.com"
KEYS="/home/ealvarado/.ssh/cdciudad-server.pem"

sudo chmod 400 $KEYS

ssh -i $KEYS $USERNAME@$HOST && echo "Successful SSH connection ..." | echo "It was not possible to establish the connection ..."
