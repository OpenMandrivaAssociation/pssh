%define name pssh
%define version 1.2.2
%define release %mkrel 2 
Summary: Parallel SSH tools
Name: %name
Version: %version
Release: %release
Group: Networking/Remote access
Source: http://www.theether.org/pssh/%name-%version.tar.gz 
License: GPL
Url:            http://theether.org/pssh/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: python
Requires: openssh, python
Buildarch: noarch

%description
This package provides various parallel tools based on ssh and scp.

%prep 
%setup

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 bin/pssh $RPM_BUILD_ROOT/%{_bindir}/pssh
install -D -m 755 bin/pscp $RPM_BUILD_ROOT/%{_bindir}/pscp
install -D -m 755 bin/pnuke $RPM_BUILD_ROOT/%{_bindir}/pnuke
install -D -m 755 bin/prsync $RPM_BUILD_ROOT/%{_bindir}/prsync
install -D -m 755 bin/pslurp $RPM_BUILD_ROOT/%{_bindir}/pslurp
install -D -m 644 lib/python/psshutil.py \
                  $RPM_BUILD_ROOT/%py_puresitedir/psshutil.py
install -D -m 644 lib/python/basethread.py \
                  $RPM_BUILD_ROOT/%py_puresitedir/basethread.py

%clean

%files
%defattr(-,root,root)
%doc NEWS TODO ChangeLog INSTALL README AUTHORS COPYING
%{_bindir}/pssh
%{_bindir}/pscp
%{_bindir}/pnuke
%{_bindir}/prsync
%{_bindir}/pslurp
%{py_puresitedir}/psshutil.py
%{py_puresitedir}/basethread.py


