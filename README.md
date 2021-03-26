# Lokinet RPM packages

This is a work in progress

## Prep System to build with RPM Package Manager

https://www.schotty.com/EL_And_Fedora/RPM_Creation/

[![IMAGE ALT TEXT](http://img.youtube.com/vi/m-3tFdSI3IE/0.jpg)](http://www.youtube.com/watch?v=m-3tFdSI3IE "RPM")

## Overview

To install Lokinet requires three RPM packages to be yum installed. The three packages are in this repository.

Requires:
- oxen-mq
- lokinet
- lokinet-gui

In order build Lokinet from source the SOURCE directory must contain the following:

lokinet  
- a copy of loki-netowrk (gz tarball)  
- a copy of lokinet.ini (unachived)  
- a copy of lokinet.service (unarchived)  

oxen-mq  
- a copy of oxen-mq (gz tarball)  

loki-network-control-panel  
- a copy of loki-network-control (gz tarball)   
- a copy of the shared folder (unarchived)    

## Obtaining Sources

Acquiring, archiving and naming tarballs for RPM Package manager. All source files must be in SOURCE dir.

### Lokinet

`git clone --recursive https://github.com/oxen-io/loki-network`  
`mv loki-network loki-network-<VERSION>`  
`tar czf loki-network-<VERSION>.src.tar.gz loki-network-<VERSION>`  
- `<VERSION>` is version number of loki-network found in source e.g 0.8.4~2  
- download lokinet.ini and lokinet.service to the SOURCES folder

### Oxen-MQ

`git clone https://github.com/oxen-io/oxen-mq`  
`mv oxen-mq oxen-mq-<VERSION>`   
`tar czf oxen-mq-<VERSION>.src.tar.gz oxen-mq-<VERSION>`  
- `<VERSION>` is version number of oxen-mq found in source e.g 1.2.4  
  
### Loki Network Control Panel

`git clone https://github.com/oxen-io/loki-network-control-panel`  
`mv loki-network-control-panel loki-network-control-panel-<VERSION>`  
`tar czf loki-network-control-panel-<VERSION>.src.tar.gz loki-network-control-panel-<VERSION>`  
- `<VERSION>` is the version number of loki-network-control-panel found in source e.g. 0.3.6  
- download a copy shared folder to the SOURCES folder.

When complete the SOURCE dir should appear as follows reflecting the latest versions.  

lokinet.ini loki-network-0.8.4.src.tar.gz loki-network-control-panel-0.3.6.src.tar.gz lokinet.service oxen-mq-1.2.4.src.tar.gz share  

In order to build the three packages the three following SPEC files are required in the SPEC folder of RPM package mananger.  
- oxen.spec
- lokinet.spec
- gui.spec

## BUILD

### Building the packages requires installation of the rpm package on the build system to be used as build dependecies. The packages must be built and installed in order of oxen-mq, loki-network and lastly the GUI. After building the package install it on the build system as it is called as a build dependency for the next package being built.   

1. Edit the `<package>`.spec file "Version:" value to match the `<VERSION>` you provided for the source file name.
2. The build command is `rpmbuild -ba /home/$USER/rpmbuild/SPEC/<package>.spec`
3. `cd /home/$USER/rpmbuild/RPMS`  
4. `sudo yum install <the package last built>`    
Repeat steps 1.,2.,3 and 4. for each of the packages. Return to SPEC dir to build next package.  
RPM packages will be written to /home/$USER/rpmbuild/RPMS

## INSTALL

Download the three RPM packages to the target system  
`sudo yum install oxen-mq-<VERSION>.fc33.x86_64.rpm`  
`sudo yum install loki-network-<VERSION>.fc33.x86_64.rpm`  
`sudo yum install loki-network-control-panel-<VERSION>.fc33.x86_64.rpm`  

## BUILDING WITH RESOLVCONF

 - Uncomment code lines commented out in lokinet.spec
 - add 00-lokinet.conf & lokinet-resolvconf to SOURCES folder
 - build  
