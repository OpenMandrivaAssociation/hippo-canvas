%define name hippo-canvas
%define api 1
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Name:           %name
Version:        0.3.0
Release:        %mkrel 6
Summary:        A canvas widget

Group:          Graphical desktop/GNOME
License:        LGPLv2
URL:            http://developer.mugshot.org/wiki/Hippo_Canvas
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/hippo-canvas/hippo-canvas-%{version}.tar.bz2
Patch0:		hippo-canvas-0.3.0-linkage.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gtk2-devel
BuildRequires:  librsvg-devel

%description
The hippo-canvas library contains a canvas widget developed by the 
Mugshot team for displaying GTK+ UI across multiple platforms.

%package -n %libname
Group:          System/Libraries
Summary:        A canvas widget

%description -n %libname
The hippo-canvas library contains a canvas widget developed by the 
Mugshot team for displaying GTK+ UI across multiple platforms.


%package -n %develname
Summary:        Development files for hippo-canvas
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:	lib%name-devel = %version-%release
Provides:	%name-devel = %version-%release

%description -n %develname
The hippo-canvas-devel package contains libraries and header files for
developing applications that use hippo-canvas.

%package -n     python-%name
Summary:        Python module for hippo-canvas
Group:          Development/Python
Requires:       %{libname} = %{version}-%{release}
BuildRequires:  pygtk2.0-devel
BuildRequires:  gtk-doc

%description -n python-%name
The hippo-canvas-python package contains a Python interface.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post  -n %libname -p /sbin/ldconfig
%postun  -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc LICENSE README AUTHORS
%{_libdir}/libhippocanvas-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/hippo-canvas-1.pc
%{_libdir}/*.so
%{_libdir}/*.la

%files -n python-%name
%defattr(-,root,root,-)
%{python_sitearch}/*.so
%{python_sitearch}/*.la

