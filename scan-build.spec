# Created by pyp2rpm-3.3.2
%global pypi_name scan-build

Name:           python-%{pypi_name}
Version:        2.0.14
Release:        1%{?dist}
Summary:        Static code analyzer wrapper for Clang/GCC

License:        NCSA
URL:            https://github.com/rizsotto/scan-build
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildArch:      noarch

%description
A package designed to wrap a build so that all calls to gcc/clang are
intercepted and logged into a compilation database and/or piped to the clang
static analyzer. Includes intercept-build tool, which logs the build, as well as
scan-build tool, which logs the build and runs the clang static analyzer on it.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2dist(setuptools)
Requires:       python2dist(typing)
%description -n python2-%{pypi_name}
A package designed to wrap a build so that all calls to gcc/clang are
intercepted and logged into a compilation database and/or piped to the clang
static analyzer. Includes intercept-build tool, which logs the build, as well as
scan-build tool, which logs the build and runs the clang static analyzer on it.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
A package designed to wrap a build so that all calls to gcc/clang are
intercepted and logged into a compilation database and/or piped to the clang
static analyzer. Includes intercept-build tool, which logs the build, as well as
scan-build tool, which logs the build and runs the clang static analyzer on it.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/libear
%{python2_sitelib}/libscanbuild
%{python2_sitelib}/scan_build-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/analyze-build
%{_bindir}/analyze-c++
%{_bindir}/analyze-cc
%{_bindir}/intercept-build
%{_bindir}/intercept-c++
%{_bindir}/intercept-cc
%{_bindir}/scan-build
%{python3_sitelib}/libear
%{python3_sitelib}/libscanbuild
%{python3_sitelib}/scan_build-%{version}-py?.?.egg-info

%changelog
* Sat Oct 20 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.14-1
- Bump upstream version.

* Tue May 15 2018 Evan Klitzke <evan@eklitzke.org> - 2.0.13-1
- Initial package.
