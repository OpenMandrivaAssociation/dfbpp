%define name	dfb++
%define Name	DFB++
%define version	1.2.0
%define rel	6

%define api		%(A=%version; echo ${A%%.*})
%define major		%(A=%version; echo ${A##*.})
%define libname		%mklibname %{name} %{api} %{major}
%define libnamedevel	%mklibname %{name} -d

Summary:	C++ binding for DirectFB providing a much easier usage
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	LGPLv2+
Group:		System/Libraries
URL:		http://directfb.org/
Source0:	http://directfb.org/downloads/Extras/%{Name}-%{version}.tar.gz
Patch0:		DFB++-1.2.0-directfb-api.patch
BuildRequires:	directfb-devel >= %{version}
BuildRoot:	%{_tmppath}/%{name}-root

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
Requires:	pkgconfig
Obsoletes:	%{libname}-devel
Obsoletes:	%{mklibname -d dfb++ 1.0 0}
Obsoletes:	%{mklibname -d dfb++ 1.2}

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README AUTHORS ChangeLog
%{_libdir}/libdfb++-%{api}.so.%{major}*

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
