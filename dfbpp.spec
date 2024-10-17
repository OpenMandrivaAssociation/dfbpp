%define Name	DFB++

%define api		%(A=%version; echo ${A%%.*})
%define major		%(A=%version; echo ${A##*.})
%define libname		%mklibname %{name} %{api} %{major}
%define libnamedevel	%mklibname %{name} -d

Summary:	C++ binding for DirectFB providing a much easier usage
Name:		dfb++
Version:	1.2.0
Release:	10
License:	LGPLv2+
Group:		System/Libraries
URL:		https://directfb.org/
Source0:	http://directfb.org/downloads/Extras/%{Name}-%{version}.tar.gz
Patch0:		DFB++-1.2.0-directfb-api.patch
BuildRequires:	directfb-devel >= %{version}

%description
This is a C++ binding for DirectFB providing a much easier usage.

%package -n	%{libname}
Summary:	C++ binding for DirectFB providing a much easier usage
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This is a C++ binding for DirectFB providing a much easier usage.

This package contains the library needed to run programs dynamically
linked with DFB++.

%package -n 	%{libnamedevel}
Summary:	Headers for developing programs that will use DFB++
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api}-devel = %{version}-%{release}

%description -n %{libnamedevel}
This package contains the headers that programmers will need to develop
applications which will use DFB++.

%package	examples
Summary:	Example programs that use DFB++
Group:		Development/C++

%description	examples
Example programs dfbshow and dfbswitch that use DFB++.

%prep
%setup -q -n %{Name}-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
chmod 644 %{buildroot}%{_libdir}/*.la

%multiarch_binaries %{buildroot}%{_bindir}/dfb++-config

make -C examples clean

%files -n %{libname}
%{_libdir}/libdfb++-%{api}.so.%{major}*

%files -n %{libnamedevel}
%doc COPYING
%{_bindir}/dfb++-config
%{multiarch_bindir}/dfb++-config
%{_includedir}/dfb++
%{_libdir}/*.so
%{_libdir}/pkgconfig/dfb++.pc

%files examples
%doc COPYING examples
%{_bindir}/dfbshow
%{_bindir}/dfbswitch

