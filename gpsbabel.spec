Summary:	GPSBabel converts GPS data from one format to another	
Name:		gpsbabel
Version:	1.3.4
Release:	%mkrel 3
License:	GPL
Group:		File tools		

Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Url:		http://%{name}.sourceforge.net
BuildRoot:	%_tmppath/%name-%version-root
BuildRequires:	expat-devel libusb-devel zlib-devel

%description
GPSBabel converts waypoints, tracks, and routes from one format to another, 
whether that format is a common mapping format like Delorme, Streets and 
Trips, or even a serial upload or download to a GPS unit such as those from 
Garmin and Magellan. By flatting the Tower of Babel that the authors of 
various programs for manipulating GPS data have imposed upon us, it returns 
to us the ability to freely move our own waypoint data between the programs 
and hardware we choose to use.

%prep
%setup -q
perl -pi -e 's|^INSTALL_TARGETDIR=/usr/local/|INSTALL_TARGETDIR=\$(DESTDIR)%_usr|' Makefile

%build
%configure --with-zlib=system
%make

%install
install -d %buildroot%{_bindir}
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README* COPYING
%{_bindir}/%{name}
