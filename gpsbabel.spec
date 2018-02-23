Summary:	Converts GPS data from one format to another
Name:		gpsbabel
Version:	1.5.4
Release:	1
License:	GPLv2+
Group:		File tools
URL:		http://www.gpsbabel.org/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.png
Patch1:		gpsbabel-1.5.4-qt.patch
BuildRequires:	expat-devel
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	zlib-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
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
%apply_patches

# fix bad execute perms
%{__chmod} a-x *.c *.h

%build
export CC=gcc
export CXX=g++
%configure --with-zlib=system
%make
pushd gui
%qmake_qt5
%_qt5_bindir/lrelease *.ts
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

%files gui
%doc gui/{AUTHORS,COPYING*,README*,TODO} gui/help/gpsbabel.html
%{_bindir}/gpsbabelfe-bin
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

