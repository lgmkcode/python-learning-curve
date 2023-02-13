Pip is a package management system that contains python libraries. 
Pip is to Python what apt is to Ubuntu.

What is a package management system? The package management system is a tool 
that allows you to easily install, update and delete libraries of 
that language using a single command.

To install pip on a linux system:

	sudo apt install python3-pip (python3.x)
	sudo apt install python-pip  (python2.x)

To view the pip version:

	pip --versiyon

To install the package we will use(For example, let's install the mqtt library.):

	pip install paho.mqtt.client

To delete a package:
	
	pip uninstall <paket_adi>

To list available packages:
	
	pip list

To list available packages that are newly released:

	pip list --oudated 

To download a package without installing it:
	
	pip download <paket_adi>

To update an existing package:

	pip install <paket_adi> --upgrade