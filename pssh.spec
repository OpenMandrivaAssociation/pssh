%define name		pssh
%define version		1.4.3
%define rel		3

Summary:	Parallel SSH tools
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Networking/Remote access
Source:		http://www.theether.org/pssh/%name-%version.tar.lzma
License:	BSD
Url:		http://theether.org/pssh/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	openssh
BuildRequires:	python-setuptools 
Buildarch:	noarch
%py_requires -d

%description
This package provides parallel versions of the OpenSSH tools.

%prep 
%setup -q

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
%{py_sitedir}/*.egg-info
