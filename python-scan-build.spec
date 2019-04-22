# Created by pyp2rpm-3.3.2
%global pypi_name scan-build
%global debug_package %{nil}

Name:           python-%{pypi_name}
Version:        2.0.15
Release:        3%{?dist}
Summary:        static code analyzer wrapper for Clang

License:        LICENSE.txt
URL:            https://github.com/rizsotto/scan-build
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

Patch1:         0001-no-typing.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 .. image::


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

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
* Mon Apr 22 2019 Evan Klitzke <evan@eklitzke.org> - 2.0.15-3
- Actually remove typing dep

* Thu Mar 28 2019 Evan Klitzke <evan@eklitzke.org> - 2.0.15-2
- Remove typing dep, which is built into python3.5+

* Tue Mar 26 2019 Evan Klitzke <evan@eklitzke.org> - 2.0.15-1
- Initial package.
