%define name		pssh
%define version		2.2.2
%define release		%mkrel 1

Summary:	Parallel SSH tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/Remote access
Source:		http://parallel-ssh.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		man-install-2.2.2.patch
License:	BSD
Url:		http://parallel-ssh.googlecode.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	openssh
Requires:	python-psshlib = %{version}-%{release}
BuildRequires:	python-setuptools 
Buildarch:	noarch
%py_requires -d

%description
PSSH provides parallel versions of OpenSSH and related tools. Included
are pssh, pscp, prsync, pnuke, and pslurp. 

%package -n python-psshlib
Summary:	Parallel SSH library for Python
Group:		Development/Python
Version:	%{version}

%description -n python-psshlib
The psshlib library enables custom applications to use PSSH.

%prep 
%setup -q
%patch0 -p0

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__install -d 755 %{buildroot}%{_mandir}/man1/
%__install -m 644 man/man1/pssh.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS COPYING 
%{_bindir}/p*
%{_mandir}/man1/pssh*

%files -n python-psshlib
%{py_sitedir}/psshlib
%{py_sitedir}/*.egg-info
