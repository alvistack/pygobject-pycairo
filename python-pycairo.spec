# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pycairo
Epoch: 100
Version: 1.20.1
Release: 1%{?dist}
Summary: Python interface for cairo
License: LGPL-2.1-or-later
URL: https://github.com/pygobject/pycairo/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cairo-gobject-devel >= 1.15.10
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pycairo is a Python module providing bindings for the cairo graphics
library.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
export CFLAGS="%{optflags}"
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pycairo
Summary: Python interface for cairo
Requires: python3
Provides: python3-pycairo = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pycairo
Pycairo is a Python module providing bindings for the cairo graphics
library.

%package -n python%{python3_version_nodots}-pycairo-devel
Summary: Development files for the Cairo Python bindings
Requires: python-pycairo-common-devel = %{epoch}:%{version}-%{release}
Requires: python3
Requires: python3-devel
Requires: python3-pycairo = %{epoch}:%{version}-%{release}
Provides: python3-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo-devel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pycairo-devel
This package provides the development files needed to build packages
that depend on Pycairo.

%package -n python-pycairo-common-devel
Summary: Headers for the Cairo Python bindings
Requires: cairo-devel
Requires: python3
Provides: python3-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}

%description -n python-pycairo-common-devel
This package provides the headers and development files needed to build
packages that depend on Pycairo.

%files -n python%{python3_version_nodots}-pycairo
%license COPYING-LGPL-2.1
%{python3_sitearch}/*
%exclude %{python3_sitearch}/cairo/include

%files -n python%{python3_version_nodots}-pycairo-devel
%{python3_sitearch}/cairo/include

%files -n python-pycairo-common-devel
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/py3cairo.pc
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pycairo
Summary: Python interface for cairo
Requires: python3
Provides: python3-pycairo = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo) = %{epoch}:%{version}-%{release}

%description -n python3-pycairo
Pycairo is a Python module providing bindings for the cairo graphics
library.

%package -n python3-pycairo-devel
Summary: Development files for the Cairo Python bindings
Requires: python-pycairo-common-devel = %{epoch}:%{version}-%{release}
Requires: python3
Requires: python3-devel
Requires: python3-pycairo = %{epoch}:%{version}-%{release}
Provides: python3-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo-devel) = %{epoch}:%{version}-%{release}

%description -n python3-pycairo-devel
This package provides the development files needed to build packages
that depend on Pycairo.

%package -n python-pycairo-common-devel
Summary: Headers for the Cairo Python bindings
Requires: cairo-devel
Requires: python3
Provides: python3-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycairo-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycairo-common-devel) = %{epoch}:%{version}-%{release}

%description -n python-pycairo-common-devel
This package provides the headers and development files needed to build
packages that depend on Pycairo.

%files -n python3-pycairo
%license COPYING-LGPL-2.1
%{python3_sitearch}/*
%exclude %{python3_sitearch}/cairo/include

%files -n python3-pycairo-devel
%{python3_sitearch}/cairo/include

%files -n python-pycairo-common-devel
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/py3cairo.pc
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cairo
Summary: Python interface for cairo
Requires: python3
Provides: python3-cairo = %{epoch}:%{version}-%{release}
Provides: python3dist(cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cairo) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cairo = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cairo) = %{epoch}:%{version}-%{release}

%description -n python3-cairo
Pycairo is a Python module providing bindings for the cairo graphics
library.

%package -n python3-cairo-devel
Summary: Python interface for cairo
Requires: python3
Provides: python3-cairo-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(cairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cairo-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cairo-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cairo-devel) = %{epoch}:%{version}-%{release}

%description -n python3-cairo-devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with py3cairo.

%files -n python3-cairo
%license COPYING-LGPL-2.1
%{python3_sitearch}/*

%files -n python3-cairo-devel
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc
%endif

%changelog
