# Lokinet RPM packages
![](https://i.imgur.com/aMrZcjq.png)

This is a work in progress

## Prep System to build with RPM Package Manager

https://www.schotty.com/EL_And_Fedora/RPM_Creation/  

## Overview

To install Lokinet requires three RPM packages to be yum installed. The three packages are in this repository.

Requires:
- oxen-mq
- lokinet
- lokinet-gui

In order build Lokinet from source the SOURCE directory must contain the following:

oxen-mq  
- a copy of oxen-mq (gz tarball)  

loki-network  
- a copy of loki-netowrk (gz tarball)  
- a copy of lokinet.ini (unachived)  
- a copy of lokinet.service (unarchived)  

loki-network-control-panel  
- a copy of loki-network-control (gz tarball)   
- a copy of the share folder (unarchived)    

## Obtaining SOURCES and SPECS

Cloning, renaming and archiving source code into tarballs in the SOURCES directory also adding in files from here to the SOURCES and SPECS folders.  

Copy the contents of the SOURCES and SPECS folders from here to your SOURCES and SPECS folders respectively in your rpmbuild directory.  
Clone the latest versions of the source code from their respective github repositories as follows:  

### oxen-mq

Clone the lastest oxen-mq source code in your SOURCES folder, rename it and tarball:  

    git clone --recursive https://github.com/oxen-io/oxen-mq  
    mv oxen-mq oxen-mq-<VERSION>
    tar czf oxen-mq-<VERSION>.src.tar.gz oxen-mq-<VERSION>
`<VERSION>` is version number of oxen-mq found in source e.g 1.2.4

### loki-network

Clone the lastest loki-network source code in your SOURCES folder, rename it and tarball:  

    git clone --recursive https://github.com/oxen-io/loki-network  
    mv loki-network loki-network-<VERSION>  
    tar czf loki-network-<VERSION>.src.tar.gz loki-network-<VERSION>  
- `<VERSION>` is version number of loki-network found in source e.g 0.8.4~2  
- download copies of lokinet.ini and lokinet.service here in to the SOURCES folder
  
### loki-network-control-panel

Clone the lastest loki-network-control-panel source code in your SOURCES folder, rename it and tarball: 

    git clone https://github.com/oxen-io/loki-network-control-panel
    mv loki-network-control-panel loki-network-control-panel-<VERSION>
    tar czf loki-network-control-panel-<VERSION>.src.tar.gz loki-network-control-panel-<VERSION>
- `<VERSION>` is the version number of loki-network-control-panel found in source e.g. 0.3.6  
- download a copy of the share folder here in to the SOURCES folder.

When complete the SOURCE dir should appear as follows reflecting the latest versions.  

lokinet.ini loki-network-0.8.4.src.tar.gz loki-network-control-panel-0.3.6.src.tar.gz lokinet.service oxen-mq-1.2.4.src.tar.gz share     

## Build

### Building the packages requires installation of the built rpm packages on the build system to be used as build dependencies. The packages must be built and installed in order of oxen-mq, loki-network and lastly loki-network-control-panel. After building the package install it on the build system as it is called as a build dependency for the next package being built.   

Install dependencies  

    $ sudo yum install automake cmake gcc-c++ libsodium-devel zeromq-devel libcap-devel libsqlite3x-devel libtool libuv-devel perl unbound-devel qt5-qtbase qt5-qtcharts-devel qt5-qtdeclarative-devel qt5-qtquickcontrols qt5-qtquickcontrols2 qt5-qtsvg-devel


1. Edit the `<package>`.spec file "Version:" value to match the `<VERSION>` you provided for the source file name.
![](https://i.imgur.com/Je26PET.jpg)
2. The build command is `rpmbuild -ba /home/$USER/rpmbuild/SPEC/<package>.spec`
3. `cd /home/$USER/rpmbuild/RPMS`  
4. `sudo yum install <the package last built>`  
Repeat steps 1.,2.,3 and 4. for each of the packages. Return to SPEC dir to build next package.  
RPM packages will be written to /home/$USER/rpmbuild/RPMS

## Install

Download the three RPM packages to the target system  

    sudo yum install oxen-mq-<VERSION>.fc33.x86_64.rpm
    sudo yum install loki-network-<VERSION>.fc33.x86_64.rpm
    sudo yum install loki-network-control-panel-<VERSION>.fc33.x86_64.rpm

## Building with Resolvconf

 - Use SPEC file lokinetresolv.spec to build  
  
Differences between lokinetresolv.spec and lokinet.spec  
 - Uncommented resolvconf code found in lokinet.spec
 - installs and uses 00-lokinet.conf & lokinet-resolvconf in SOURCES folder

## Support us

Lokinet-RPM-packages and the packaging files are free software but powered by your support. If you find it beneficial or wish to contribute to inspire ongoing development small donations are greatly appreciated.

- Oxen Donation Address:
```sh
LA8VDcoJgiv2bSiVqyaT6hJ67LXbnQGpf9Uk3zh9ikUKPJUWeYbgsd9gxQ5ptM2hQNSsCaRETQ3GM9FLDe7BGqcm4ve69bh
```
- Donation Wallets

![](https://i.imgur.com/HGVuijh.jpg) ![](https://i.imgur.com/6dMgBVr.jpg) ![](https://i.imgur.com/gIhGB1X.jpg)

## How to contribute

1. File an issue in the repository, using the bug tracker, describing the
   contribution you'd like to make. This will help us to get you started on the
   right foot.
2. Fork the project in your account and create a new branch:
   `your-great-feature`.
3. Commit your changes in that branch.
4. Open a pull request, and reference the initial issue in the pull request
   message.

## License
See the [LICENSE](./LICENSE) file.
