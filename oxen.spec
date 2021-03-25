Name:           oxen-mq
Version:        1.2.4
Release:        1%{?dist}
Summary:        Lokinet is an anonymous, decentralized and IP based overlay network for the internet.

License:        GPL v3
URL:            http://lokinet.org/
Source0:        %{name}-%{version}.src.tar.gz

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zeromq-devel
BuildRequires:  cmake
BuildRequires:  libsodium-devel
Requires:	libsodium-devel
Requires:	zeromq-devel

%description

	LLARP is a protocol suite meant to anonymize IP by providing an anonymous
	network level (IPv4/IPv6) tunnel broker for both "hidden services" and
	communication back to "the clearnet" (the normal internet). Both hidden service
	and clearnet communication MUST permit both outbound and inbound traffic on the
	network level without any NAT (except for IPv4 in which NAT is permitted due to
	lack of address availability). 

%global debug_package %{nil}
%prep

#update sources (note: old oxen-mq .src.tar.gz) needs to be present for build to run. To achieve this mv old oxen-mq tar to new version number then run build. Sources will be updated during build.
#sourcedir=/home/$USER/rpmbuild/SOURCES
#cd $sourcedir
#rm -rf temp
#rm -rf %{name}-%{version}
#git clone --recursive https://github.com/oxen-io/oxen-mq $sourcedir/temp
#mv temp %{name}-%{version}
#tar -czf %{name}-%{version}.src.tar.gz %{name}-%{version}

%setup


%build
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DOXENMQ_INSTALL_CPPZMQ=ON -DOXENMQ_BUILD_TESTS=OFF
make -j6


%install

#rm -rf $RPM_BUILD_ROOT
cd build
%make_install


%files
%license LICENSE
%doc README.md
   /usr/include/lokimq/address.h
   /usr/include/lokimq/auth.h
   /usr/include/lokimq/base32z.h
   /usr/include/lokimq/base64.h
   /usr/include/lokimq/batch.h
   /usr/include/lokimq/bt_serialize.h
   /usr/include/lokimq/bt_value.h
   /usr/include/lokimq/connections.h
   /usr/include/lokimq/hex.h
   /usr/include/lokimq/lokimq.h
   /usr/include/lokimq/message.h
   /usr/include/lokimq/variant.h
   /usr/include/lokimq/version.h
   /usr/include/oxenmq/address.h
   /usr/include/oxenmq/auth.h
   /usr/include/oxenmq/base32z.h
   /usr/include/oxenmq/base64.h
   /usr/include/oxenmq/batch.h
   /usr/include/oxenmq/bt_serialize.h
   /usr/include/oxenmq/bt_value.h
   /usr/include/oxenmq/byte_type.h
   /usr/include/oxenmq/connections.h
   /usr/include/oxenmq/hex.h
   /usr/include/oxenmq/message.h
   /usr/include/oxenmq/oxenmq.h
   /usr/include/oxenmq/variant.h
   /usr/include/oxenmq/version.h
   /usr/include/oxenmq/zmq.hpp
   /usr/lib64/liboxenmq.so
   /usr/lib64/liboxenmq.so.0
   /usr/lib64/pkgconfig/liblokimq.pc
   /usr/lib64/pkgconfig/liboxenmq.pc



%changelog
* Tue Mar 09 2021 Technical Tumbleweed (necro_nemesis@hotmail.com) oxenmq
-First oxenmq RPM

