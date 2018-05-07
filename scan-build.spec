%global srcname scan-build
%global sum scan-build implementation in python

Name:           python-%{srcname}
Version:        2.0.13
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/7e/94/c8235245aee84953a03ed49e2bb6985afa03099a3a0b190a9a0db74701bb/scan-build-2.0.13.tar.gz
Patch0:         0001-fixrequires.patch

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  python2-devel
BuildRequires:  python2-typing
BuildRequires:  python3-devel

%description
An implementation of Clang scan-build in Python

%package -n python2-%{srcname}
Summary:        %{sum}
Requires:       python2-typing
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
An implementation of Clang scan-build in Python

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
An implementation of Clang scan-build in Python

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{srcname}
%doc README.rst CHANGES.txt LICENSE.txt
%{python2_sitelib}/*
%{_bindir}/{analyze,intercept}-{build,c++,cc}
%{_bindir}/scan-build

%files -n python3-%{srcname}
%doc README.rst CHANGES.txt LICENSE.txt
%{python3_sitelib}/*
%{_bindir}/{analyze,intercept}-{build,c++,cc}
%{_bindir}/scan-build

%changelog
* Mon May 07 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.13-1
- initial packaging work
