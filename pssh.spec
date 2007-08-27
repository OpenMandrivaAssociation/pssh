%define name	pssh
%define version 1.3.1
%define release %mkrel 1
Summary: Parallel SSH tools
Name: 	 %name
Version: %version
Release: %release
Group: 	 Networking/Remote access
Source:  http://www.theether.org/pssh/%name-%version.tar.bz2
License: BSD
Url:     http://theether.org/pssh/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: python
Requires: openssh, python
Buildarch: noarch

%description
This package provides various parallel tools based on ssh and scp.

%prep 
%setup

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO ChangeLog INSTALL AUTHORS COPYING doc/pssh-HOWTO.html
%{_bindir}/*
%{py_sitedir}/psshlib
%if "%py_ver" == "2.5"
%py_sitedir/*.egg-info
%endif



