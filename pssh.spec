%define name		pssh
%define version		2.1.1
%define release		%mkrel 2

Summary:	Parallel SSH tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/Remote access
Source:		http://parallel-ssh.googlecode.com/files/%{name}-%{version}.tar.gz
License:	BSD
Url:		http://parallel-ssh.googlecode.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	openssh
BuildRequires:	python-setuptools 
Buildarch:	noarch
%py_requires -d

%description
PSSH provides parallel versions of OpenSSH and related tools. Included
are pssh, pscp, prsync, pnuke, and pslurp. The project includes
psshlib which can be used within custom applications.

%prep 
%setup -q

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS COPYING 
%{_bindir}/*
%{py_sitedir}/psshlib
%{py_sitedir}/*.egg-info

