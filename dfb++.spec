
%define name	dfb++
%define Name	DFB++
%define version	1.0.0
%define rel	1

%define major_major	%(A=%version; echo ${A%%.*})
%define minor_major	%(A=%version; echo ${A##*.})
%define lib_major	%{major_major}_%{minor_major}
%define libname		%mklibname %name %lib_major
%define libnamedevel	%mklibname %name %lib_major -d

Summary:	C++ binding for DirectFB providing a much easier usage
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		System/Libraries
URL:		http://directfb.org/
Source0:	http://directfb.org/downloads/Extras/%{Name}-%{version}.tar.bz2
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
Provides:	lib%{name}%(echo %lib_major | cut -f 1 -d _)-devel = %{version}-%{release}
Requires:	pkgconfig

%description -n %{libnamedevel}
This package contains the headers that programmers will need to develop
applications which will use DFB++.

%package	examples
Summary:	Example programs that use DFB++
Group:		Development/C++

%description	examples
Example programs dfbshow and dfbswitch that use DFB++.

Source code is included in %{_docdir}/%{name}-%{version}/examples.

%prep
%setup -q -n %{Name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
chmod 644 %{buildroot}%{_libdir}/*.la

%multiarch_binaries %{buildroot}%{_bindir}/dfb++-config

make -C examples clean

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README AUTHORS ChangeLog
%{_libdir}/libdfb++-%{major_major}.so.%{minor_major}*

%files -n %{libnamedevel}
%defattr(-,root,root)
%doc COPYING
%{_bindir}/dfb++-config
%multiarch %{multiarch_bindir}/dfb++-config
%{_includedir}/dfb++
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/dfb++.pc

%files examples
%defattr(-,root,root)
%doc COPYING examples
%{_bindir}/dfbshow
%{_bindir}/dfbswitch


