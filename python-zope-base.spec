#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Common dirs for Zope libraries
Summary(pl.UTF-8):	Katalogi wspólne dla bibliotek Zope
Name:		python-zope-base
Version:	1.0
Release:	8
License:	Public Domain
Group:		Libraries/Python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-modules
%endif
Provides:	Zope-dirs
Obsoletes:	Zope-dirs < 1.0-8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
Common dirs for Zope libraries.

%description -l pl.UTF-8
Katalogi wspólne dla bibliotek Zope.

%package -n python3-zope-base
Summary:	Common dirs for Zope libraries
Summary(pl.UTF-8):	Katalogi wspólne dla bibliotek Zope
Group:		Libraries/Python

%description -n python3-zope-base
Common dirs for Zope libraries.

%description -n python3-zope-base -l pl.UTF-8
Katalogi wspólne dla bibliotek Zope.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py3_sitescriptdir},%{py_sitedir},%{py3_sitedir}}/zope

%if %{with python2}
touch $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py_sitedir}}/zope/__init__.py
%py_comp $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py_sitedir}}/zope
%py_ocomp $RPM_BUILD_ROOT{%{py_sitescriptdir},%{py_sitedir}}/zope
%py_postclean
%endif

%if %{with python3}
touch $RPM_BUILD_ROOT{%{py3_sitescriptdir},%{py3_sitedir}}/zope/__init__.py
%py3_comp $RPM_BUILD_ROOT{%{py3_sitescriptdir},%{py3_sitedir}}/zope
%py3_ocomp $RPM_BUILD_ROOT{%{py3_sitescriptdir},%{py3_sitedir}}/zope
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitedir}/zope
%{py_sitescriptdir}/zope
%endif

%if %{with python3}
%files -n python3-zope-base
%defattr(644,root,root,755)
%{py3_sitedir}/zope
%{py3_sitescriptdir}/zope
%endif
