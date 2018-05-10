%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%global defaultpython 3
%else
%global defaultpython 2
%endif
%else
%bcond_with python3
%global defaultpython 2
%endif

%global modname scan-build

# set to 1 to run lit tests; disabled for now as they are flaky
%global littests 0

Name:           python-%{modname}
Version:        2.0.13
Release:        3%{?dist}
Summary:        A Python scan-build implementation

License:        MIT
URL:            https://github.com/rizsotto/%{modname}
Source0:        https://github.com/rizsotto/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
Patch0:         0001-fixrequires.patch

BuildArch:      noarch

%description
An implementation of Clang scan-build in Python

%package -n python2-%{modname}
Summary:        A Python scan-build implementation
Requires:       python2-typing
%{?python_provide:%python_provide python2-%{modname}}

Requires:       python2-setuptools
Requires:       python2-typing

BuildRequires:  clang
BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
BuildRequires:  python2-typing
%if %{littests}
BuildRequires:  cmake
BuildRequires:  python2-lit
%endif

%description -n python2-%{modname}
An implementation of Clang scan-build in Python

%if %{with python3}
%package -n python%{python3_pkgversion}-%{modname}
Summary:        A Python scan-build implementation
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

Requires:       python3-setuptools

BuildRequires:  clang
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
%if %{littests}
BuildRequires:  cmake
BuildRequires:  python3-lit
%endif

%description -n python%{python3_pkgversion}-%{modname}
An implementation of Clang scan-build in Python
%endif

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
mv %{buildroot}%{_bindir}/scan-build %{buildroot}%{_bindir}/scan-build-2
ln -s scan-build-2 %{buildroot}%{_bindir}/scan-build-%{python2_version}

mv %{buildroot}%{_bindir}/analyze-build %{buildroot}%{_bindir}/analyze-build-2
ln -s analyze-build-2 %{buildroot}%{_bindir}/analyze-build-%{python2_version}

mv %{buildroot}%{_bindir}/analyze-c++ %{buildroot}%{_bindir}/analyze-c++-2
ln -s analyze-c++-2 %{buildroot}%{_bindir}/analyze-c++-%{python2_version}

mv %{buildroot}%{_bindir}/analyze-cc %{buildroot}%{_bindir}/analyze-cc-2
ln -s analyze-cc-2 %{buildroot}%{_bindir}/analyze-cc-%{python2_version}

mv %{buildroot}%{_bindir}/intercept-build %{buildroot}%{_bindir}/intercept-build-2
ln -s intercept-build-2 %{buildroot}%{_bindir}/intercept-build-%{python2_version}

mv %{buildroot}%{_bindir}/intercept-c++ %{buildroot}%{_bindir}/intercept-c++-2
ln -s intercept-c++-2 %{buildroot}%{_bindir}/intercept-c++-%{python2_version}

mv %{buildroot}%{_bindir}/intercept-cc %{buildroot}%{_bindir}/intercept-cc-2
ln -s intercept-cc-2 %{buildroot}%{_bindir}/intercept-cc-%{python2_version}

%if %{with python3}
%py3_install
mv %{buildroot}%{_bindir}/scan-build %{buildroot}%{_bindir}/scan-build-3
ln -s scan-build-3 %{buildroot}%{_bindir}/scan-build-%{python3_version}

mv %{buildroot}%{_bindir}/analyze-build %{buildroot}%{_bindir}/analyze-build-3
ln -s analyze-build-3 %{buildroot}%{_bindir}/analyze-build-%{python3_version}

mv %{buildroot}%{_bindir}/analyze-c++ %{buildroot}%{_bindir}/analyze-c++-3
ln -s analyze-c++-3 %{buildroot}%{_bindir}/analyze-c++-%{python3_version}

mv %{buildroot}%{_bindir}/analyze-cc %{buildroot}%{_bindir}/analyze-cc-3
ln -s analyze-cc-3 %{buildroot}%{_bindir}/analyze-cc-%{python3_version}

mv %{buildroot}%{_bindir}/intercept-build %{buildroot}%{_bindir}/intercept-build-3
ln -s intercept-build-3 %{buildroot}%{_bindir}/intercept-build-%{python3_version}

mv %{buildroot}%{_bindir}/intercept-c++ %{buildroot}%{_bindir}/intercept-c++-3
ln -s intercept-c++-3 %{buildroot}%{_bindir}/intercept-c++-%{python3_version}

mv %{buildroot}%{_bindir}/intercept-cc %{buildroot}%{_bindir}/intercept-cc-3
ln -s intercept-cc-3 %{buildroot}%{_bindir}/intercept-cc-%{python3_version}
%endif

ln -s scan-build-%{defaultpython} %{buildroot}%{_bindir}/scan-build
ln -s analyze-build-%{defaultpython} %{buildroot}%{_bindir}/analyze-build
ln -s analyze-c++-%{defaultpython} %{buildroot}%{_bindir}/analyze-c++
ln -s analyze-cc-%{defaultpython} %{buildroot}%{_bindir}/analyze-cc
ln -s intercept-build-%{defaultpython} %{buildroot}%{_bindir}/intercept-build
ln -s intercept-c++-%{defaultpython} %{buildroot}%{_bindir}/intercept-c++
ln -s intercept-cc-%{defaultpython} %{buildroot}%{_bindir}/intercept-cc

%check
nosetests-2 tests/unit
%if %{littests}
CCACHE_DISABLE=1 lit -v tests
%endif

%if %{with python3}
nosetests-3 tests/unit
%if %{littests}
CCACHE_DISABLE=1 lit -v tests
%endif
%endif

%files -n python2-%{modname}
%doc README.rst CHANGES.txt LICENSE.txt
%if %{defaultpython} == 2
%{_bindir}/scan-build
%{_bindir}/analyze-build
%{_bindir}/analyze-c++
%{_bindir}/analyze-cc
%{_bindir}/intercept-build
%{_bindir}/intercept-c++
%{_bindir}/intercept-cc
%endif
%{_bindir}/scan-build-2
%{_bindir}/scan-build-%{python2_version}
%{_bindir}/analyze-build-2
%{_bindir}/analyze-build-%{python2_version}
%{_bindir}/analyze-c++-2
%{_bindir}/analyze-c++-%{python2_version}
%{_bindir}/analyze-cc-2
%{_bindir}/analyze-cc-%{python2_version}
%{_bindir}/intercept-build-2
%{_bindir}/intercept-build-%{python2_version}
%{_bindir}/intercept-c++-2
%{_bindir}/intercept-c++-%{python2_version}
%{_bindir}/intercept-cc-2
%{_bindir}/intercept-cc-%{python2_version}
%{python2_sitelib}/*

%if %{with python3}
%files -n python%{python3_pkgversion}-%{modname}
%doc README.rst CHANGES.txt LICENSE.txt
%if %{defaultpython} == 3
%{_bindir}/scan-build
%{_bindir}/analyze-build
%{_bindir}/analyze-c++
%{_bindir}/analyze-cc
%{_bindir}/intercept-build
%{_bindir}/intercept-c++
%{_bindir}/intercept-cc
%endif
%{_bindir}/scan-build-3
%{_bindir}/scan-build-%{python3_version}
%{_bindir}/analyze-build-3
%{_bindir}/analyze-build-%{python3_version}
%{_bindir}/analyze-c++-3
%{_bindir}/analyze-c++-%{python3_version}
%{_bindir}/analyze-cc-3
%{_bindir}/analyze-cc-%{python3_version}
%{_bindir}/intercept-build-3
%{_bindir}/intercept-build-%{python3_version}
%{_bindir}/intercept-c++-3
%{_bindir}/intercept-c++-%{python3_version}
%{_bindir}/intercept-cc-3
%{_bindir}/intercept-cc-%{python3_version}
%{python3_sitelib}/*
%endif

%changelog
* Thu May 10 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.13-3
- Run nose tests when building RPM

* Thu May 10 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.13-2
- Update to be more conformant with py2/py3 packaging guidelines

* Mon May 07 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.13-1
- initial packaging work
