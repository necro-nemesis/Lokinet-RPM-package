Name:           loki-network-control-panel
Version:        0.3.8
Release:        1%{?dist}
Summary:        Lokinet is an anonymous, decentralized and IP based overlay network for the internet.

License:        GPL v3
URL:            http://lokinet.org/
Source0:        %{name}-%{version}.src.tar.gz

BuildRequires:	systemd
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:	qt5-qtquickcontrols
BuildRequires:  qt5-qtquickcontrols2
BuildRequires:  qt5-qtcharts-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  cmake
BuildRequires:  pkgconf-pkg-config
BuildRequires:  oxen-mq
BuildRequires:  loki-network
Requires:	qt5-qtcharts
Requires:	qt5-qtgraphicaleffects
Requires:	qt5-qtbase
Requires:	qt5-qtquickcontrols
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtsvg

%description

	LLARP is a protocol suite meant to anonymize IP by providing an anonymous
	network level (IPv4/IPv6) tunnel broker for both "hidden services" and
	communication back to "the clearnet" (the normal internet). Both hidden service
	and clearnet communication MUST permit both outbound and inbound traffic on the
	network level without any NAT (except for IPv4 in which NAT is permitted due to
	lack of address availability). 

%global debug_package %{nil}
%prep
%setup


%build

mkdir -p build
cd build
cmake -DSYSTEMD=ON ..
make -j8
make DESTDIR=%{_builddir} install

%install
#rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/doc/lokinet-gui
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/16x16/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/192x192/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/24x24/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/32x32/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/64x64/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/96x96/apps
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps

cp %{_builddir}/usr/local/bin/lokinet-gui %{buildroot}/usr/bin/lokinet-gui
#cp %{_builddir}/%{name}-%{version}/build/lokinet-gui %{buildroot}/usr/bin/lokinet-gui
cp %{_sourcedir}/share/applications/lokinet-gui.desktop %{buildroot}/usr/share/applications/lokinet-gui.desktop
cp %{_sourcedir}/share/doc/lokinet-gui/copyright %{buildroot}/usr/share/doc/lokinet-gui/copyright
cp %{_sourcedir}/share/icons/hicolor/128x128/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/16x16/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/16x16/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/192x192/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/192x192/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/24x24/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/24x24/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/256x256/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/32x32/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/32x32/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/48x48/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/64x64/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/64x64/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/96x96/apps/lokinet-gui.png %{buildroot}/usr/share/icons/hicolor/96x96/apps/lokinet-gui.png
cp %{_sourcedir}/share/icons/hicolor/scalable/apps/lokinet-gui.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/lokinet-gui.svg



%post


%preun


%postun


%files
%license

   /usr/bin/lokinet-gui
   /usr/share/applications/lokinet-gui.desktop
   /usr/share/doc/lokinet-gui/copyright
   /usr/share/icons/hicolor/128x128/apps/lokinet-gui.png
   /usr/share/icons/hicolor/16x16/apps/lokinet-gui.png
   /usr/share/icons/hicolor/192x192/apps/lokinet-gui.png
   /usr/share/icons/hicolor/24x24/apps/lokinet-gui.png
   /usr/share/icons/hicolor/256x256/apps/lokinet-gui.png
   /usr/share/icons/hicolor/32x32/apps/lokinet-gui.png
   /usr/share/icons/hicolor/48x48/apps/lokinet-gui.png
   /usr/share/icons/hicolor/64x64/apps/lokinet-gui.png
   /usr/share/icons/hicolor/96x96/apps/lokinet-gui.png
   /usr/share/icons/hicolor/scalable/apps/lokinet-gui.svg

%changelog
* Tue Mar 09 2021 Technical Tumbleweed (necro_nemesis@hotmail.com) %{name}-%{version}
-First loki-network-control-panel RPM
