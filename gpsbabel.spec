Summary:	GPSBabel converts GPS data from one format to another
Name:		gpsbabel
Version:	1.4.3
Release:	1
License:	GPLv2+
Group:		File tools
URL:		http://www.gpsbabel.org/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.png
Patch0:		gpsbabel-1.3.5-autoconf.patch
BuildRequires:	expat-devel
BuildRequires:	libusb-devel
BuildRequires:	zlib-devel
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils

%description
GPSBabel converts waypoints, tracks, and routes from one format to another, 
whether that format is a common mapping format like Delorme, Streets and 
Trips, or even a serial upload or download to a GPS unit such as those from 
Garmin and Magellan. By flatting the Tower of Babel that the authors of 
various programs for manipulating GPS data have imposed upon us, it returns 
to us the ability to freely move our own waypoint data between the programs 
and hardware we choose to use.

%package gui
Summary:	Qt GUI interface for GPSBabel
Group:		Graphical desktop/KDE
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description gui
Qt GUI interface for GPSBabel.

%prep

%setup -q
perl -pi -e 's|^INSTALL_TARGETDIR=/usr/local/|INSTALL_TARGETDIR=\$(DESTDIR)%_usr|' Makefile
%patch0 -p0 -b .autoconf

# fix bad execute perms
%{__chmod} a-x *.c *.h

%build
%configure2_5x --with-zlib=system
%make
pushd gui
%qmake_qt4
%qt4bin/lrelease *.ts
%make
popd

%install
%__install -d %{buildroot}%{_bindir}
%makeinstall_std
%makeinstall_std -C gui

%__install -m 0755 -d %{buildroot}%{_bindir}/
%__install -m 0755 -p gui/objects/gpsbabelfe-bin %{buildroot}%{_bindir}/
%__install -m 0755 -d %{buildroot}%{translationdir}/
%__install -m 0644 -p gui/gpsbabel*_*.qm %{buildroot}%{translationdir}/

desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        %{SOURCE1}

install -m 0755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%files
%doc README* COPYING
%{_bindir}/%{name}

%files gui -f %{name}.lang
%doc gui/{AUTHORS,COPYING*,README*,TODO} gui/help/gpsbabel.html
%{_bindir}/gpsbabelfe-bin
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*
