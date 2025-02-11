Summary:	Converts GPS data from one format to another
Name:		gpsbabel
Version:	1.10.0
Release:	1
License:	GPLv2+
Group:		File tools
URL:		https://www.gpsbabel.org/
# needs to be downloaded from https://www.gpsbabel.org/
#Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.png
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(shapelib)
BuildRequires:	zlib-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6SerialPort)
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

%autosetup -p1

%build
export CC=gcc
export CXX=g++
%cmake \
  -DGPSBABEL_WITH_LIBUSB=pkgconfig \
  -DGPSBABEL_WITH_ZLIB=pkgconfig \
  -DGPSBABEL_WITH_SHAPELIB=pkgconfig

%make_build

#pushd gui
#qmake_qt5
#_qt5_bindir/lrelease *.ts
#make
#popd

%install
#make_install -C build

%__install -m 0755 -d %{buildroot}%{_bindir}/

%__install -m 0755 -p build/gpsbabel %{buildroot}%{_bindir}/

%__install -m 0755 -p build/gui/GPSBabelFE/gpsbabelfe %{buildroot}%{_bindir}/

desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        %{SOURCE1}

install -m 0755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%files
%doc README* COPYING
%{_bindir}/%{name}

%files gui
%doc gui/{AUTHORS,COPYING*,README*,TODO}
%{_bindir}/gpsbabelfe
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*


%changelog
* Thu Jul 26 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-1
+ Revision: 811058
- duh...
- No translations found for gpsbabel
- 1.4.3

* Mon Oct 31 2011 Andrey Bondrov <abondrov@mandriva.org> 1.4.2-1
+ Revision: 707998
- New version 1.4.2, now we have Qt4 frontend

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-3mdv2011.0
+ Revision: 619250
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.3.6-2mdv2010.0
+ Revision: 437808
- rebuild

* Thu Jan 08 2009 Emmanuel Andry <eandry@mandriva.org> 1.3.6-1mdv2009.1
+ Revision: 327269
- New version 1.3.6
- use configure2_5x
- reimport broken P0 from Fedora
- diff P1 to fix str fmt

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3.4-3mdv2009.0
+ Revision: 246546
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.3.4-1mdv2008.1
+ Revision: 165954
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 06 2007 Emmanuel Andry <eandry@mandriva.org> 1.3.4-1mdv2008.0
+ Revision: 81316
- New version

  + Nicolas Vigier <nvigier@mandriva.com>
    - Import gpsbabel

