Name:           loki-network
Version:        0.8.3
Release:        1%{?dist}
Summary:        Lokinet is an anonymous, decentralized and IP based overlay network for the internet.

License:        GPL v3
URL:            http://lokinet.org/
Source0:        %{name}-%{version}.src.tar.gz
Source1:	lokinet.service
Source2:	00-lokinet.conf
Source3:	lokinet-resolvconf
Source4:	lokinet.ini

BuildRequires:	systemd
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  kernel-devel
BuildRequires:  wget
BuildRequires:  unbound-devel
BuildRequires:	libsqlite3x-devel
BuildRequires:  git
BuildRequires:  perl
BuildRequires:  sqlite
BuildRequires:  zeromq-devel
BuildRequires:  cmake
BuildRequires:  libcap-devel
BuildRequires:  libuv-devel
BuildRequires:  libsodium-devel
BuildRequires:  pkgconf-pkg-config
Requires:       bash
Requires:       curl


%description

	LLARP is a protocol suite meant to anonymize IP by providing an anonymous
	network level (IPv4/IPv6) tunnel broker for both "hidden services" and
	communication back to "the clearnet" (the normal internet). Both hidden service
	and clearnet communication MUST permit both outbound and inbound traffic on the
	network level without any NAT (except for IPv4 in which NAT is permitted due to
	lack of address availability). 

%prep
%setup


%build

mkdir -p build
cd build
cmake .. -DFORCE_OXENMQ_SUBMODULE=ON -DCMAKE_CXX_FLAGS="-march=x86-64 -mtune=haswell" -DCMAKE_C_FLAGS="-march=x86-64 -mtune=haswell" -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=OFF -DNATIVE_BUILD=OFF -DUSE_AVX2=OFF -DWITH_SETCAP=OFF -DBUILD_STATIC_DEPS=ON -DBUILD_SHARED_LIBS=OFF -DSTATIC_LINK=ON -DWITH_LTO=OFF
make -j8
make DESTDIR=/%{_builddir} install

%install

rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/systemd/resolved.conf.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/var/lib/lokinet
mkdir -p %{buildroot}/etc/loki

cp %{_builddir}/usr/local/bin/lokinet %{buildroot}/usr/bin
cp %{_builddir}/usr/local/bin/lokinet-bootstrap %{buildroot}/usr/bin
cp %{_builddir}/usr/local/bin/lokinet-vpn %{buildroot}/usr/bin
cp %{SOURCE1} %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}/etc/systemd/resolved.conf.d
cp %{SOURCE3} %{buildroot}/usr/sbin
cp %{SOURCE4} %{buildroot}/etc/loki

%post

#!/bin/sh -e

set -e

    # Create the loki_ group (shared with lokid)
    if ! getent group _loki >/dev/null; then
        groupadd --system _loki
    fi

    # Create _lokinet user if it doesn't exist
    if ! getent passwd _lokinet >/dev/null; then
        useradd --system --home-dir /var/lib/lokinet -g _loki _lokinet

    fi

    # Make sure the _lokinet user is part of the _loki group (in case it already existed)
    if ! id -Gn _lokinet | grep -qw _loki; then
        useradd _lokinet _loki
    fi

     datadir=/var/lib/lokinet
     mkdir -p $datadir
     chown _lokinet:_loki $datadir

    if ! [ -e /var/lib/lokinet/bootstrap.signed ]; then
        /usr/bin/lokinet-bootstrap lokinet /var/lib/lokinet/bootstrap.signed
        chown _lokinet:_loki /var/lib/lokinet/bootstrap.signed
    fi
        chown _lokinet:_loki /etc/loki/lokinet.ini

    /usr/bin/lokinet -g /etc/loki/lokinet.ini
    chmod 640 /etc/loki/lokinet.ini
    chgrp _loki /etc/loki/lokinet.ini
    ln -s /etc/loki/lokinet.ini /var/lib/lokinet/lokinet.ini


    sudo systemctl enable lokinet
    sudo systemctl start lokinet

    if [ -x /bin/systemctl ] && /bin/systemctl --quiet is-active systemd-resolved.service; then
        /bin/systemctl restart systemd-resolved.service
    fi

%preun

#!/bin/sh

set -e

    sudo systemctl stop lokinet

%postun

#!/bin/sh

set -e

    rm -f /etc/loki/lokinet.ini
    rm -rf /var/lib/lokinet/{*.{signed,private},lokinet.pid,metrics.json,profiles.dat,netdb}
    rm -f /lib/systemd/system/lokinet.service
    rm -rf /etc/loki
    rm -rf /var/lib/lokinet

%files
%license LICENSE.txt
/etc/systemd/resolved.conf.d/00-lokinet.conf
#/usr/lib/debug/usr/bin/lokinet-0.8.3-1.fc33.x86_64.debug
#/usr/lib/debug/usr/bin/lokinet-vpn-0.8.3-1.fc33.x86_64.debug
/usr/lib/systemd/system/lokinet.service
/usr/bin/lokinet
/usr/bin/lokinet-bootstrap
/usr/bin/lokinet-vpn
/usr/sbin/lokinet-resolvconf
%config(noreplace)/etc/loki/lokinet.ini

%changelog
* Sun Mar 07 2021 Technical Tumbleweed (necro_nemesis@hotmail.com) Lokinet 0.8.2
-First Lokinet RPM
