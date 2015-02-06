%define name		pssh
%define version		2.3.1
%define release		2

Summary:	Parallel SSH tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/Remote access
Source:		http://parallel-ssh.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		man-install-2.3.1.patch
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
%__install -m 644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS COPYING 
%{_bindir}/p*
%{_mandir}/man1/p*

%files -n python-psshlib
%{py_sitedir}/psshlib
%{py_sitedir}/*.egg-info


%changelog
* Thu Feb 02 2012 Lev Givon <lev@mandriva.org> 2.3.1-1mdv2011.0
+ Revision: 770782
- Update to 2.3.1.

* Tue Jan 24 2012 Lev Givon <lev@mandriva.org> 2.3-1
+ Revision: 768084
- Update to 2.3.

* Fri Feb 11 2011 Lev Givon <lev@mandriva.org> 2.2.2-1
+ Revision: 637327
- Update to 2.2.2.
  Package psshlib separately.

* Fri Nov 05 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.1.1-2mdv2011.0
+ Revision: 593540
- Rebuild for new python.

* Tue Mar 09 2010 Lev Givon <lev@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 517197
- Update to 2.1.1.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.3-3mdv2010.0
+ Revision: 441966
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.4.3-2mdv2009.1
+ Revision: 325813
- rebuild

* Sun Nov 09 2008 Lev Givon <lev@mandriva.org> 1.4.3-1mdv2009.1
+ Revision: 301464
- Update to 1.4.3.

* Tue Sep 09 2008 Lev Givon <lev@mandriva.org> 1.4.2-1mdv2009.0
+ Revision: 283311
- Update to 1.4.2.

* Sun Jun 22 2008 Lev Givon <lev@mandriva.org> 1.3.2-1mdv2009.0
+ Revision: 227949
- Update to 1.3.2.

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.3.1-2mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Lev Givon <lev@mandriva.org> 1.3.1-2mdv2008.0
+ Revision: 72167
- Fix arg bug.
- Update to 1.3.1.
  Clean up spec file.


* Mon Nov 06 2006 Erwan Velu <erwan@mandriva.org> 1.2.2-2mdv2007.0
+ Revision: 76853
- Adding Buildrequires on python
- Import pssh

* Thu Nov 02 2006 Erwan Velu <erwan@mandriva.org> 1.2.2-1mdv2007.1
- Initial relase

