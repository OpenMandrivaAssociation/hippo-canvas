%define name hippo-canvas
%define api 1
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Name:           %name
Version:        0.3.1
Release:        6
Summary:        A canvas widget

Group:          Graphical desktop/GNOME
License:        LGPLv2
URL:            http://developer.mugshot.org/wiki/Hippo_Canvas
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/hippo-canvas/hippo-canvas-%{version}.tar.bz2
Patch0:		hippo-canvas-0.3.0-linkage.patch
BuildRequires:  gtk+2.0-devel
BuildRequires:  librsvg-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(pycairo)

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
BuildRequires:  python-gobject-devel > 2.21.2
BuildRequires:  gtk-doc

%description -n python-%name
The hippo-canvas-python package contains a Python interface.

%prep
%setup -q
%patch0 -p0

%build
export LDFLAGS="-lgmodule-2.0"
%configure2_5x --disable-static
%make

%install
%makeinstall_std
mv %buildroot%_datadir/gir %buildroot%_datadir/gir-1.0


%files -n %libname
%defattr(-,root,root,-)
%doc LICENSE README AUTHORS
%{_libdir}/libhippocanvas-%api.so.%{major}*
%_libdir/girepository-1.0/Hippo-1.0.typelib

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/hippo-canvas-1.pc
%{_libdir}/*.so
%_datadir/gir-1.0/Hippo-1.0.gir

%files -n python-%name
%defattr(-,root,root,-)
%{python_sitearch}/*.so



%changelog
* Tue Nov 22 2011 Götz Waschk <waschk@mandriva.org> 0.3.1-4mdv2012.0
+ Revision: 732425
- rebuild

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 0.3.1-3mdv2011.0
+ Revision: 599398
- rebuild for py2.7

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 578945
- rebuild for new gobject-introspection

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 563542
- new version
- bump python-gobject dep
- add introspection support

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-6mdv2010.0
+ Revision: 437868
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.3.0-5mdv2009.1
+ Revision: 324094
- fix linkage

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.3.0-4mdv2009.1
+ Revision: 323728
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-3mdv2009.1
+ Revision: 301580
- rebuilt against new libxcb

* Thu Jul 24 2008 Götz Waschk <waschk@mandriva.org> 0.3.0-2mdv2009.0
+ Revision: 244978
- fix python package deps

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 242275
- fix buildrequires
- import hippo-canvas


* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2009.0
- adapt for Mandriva

* Thu Jun 19 2008 Owen Taylor <otaylor@redhat.com> - 0.2.34-1
- Update to 0.2.34 (Fixes crash when destroying HippoCanvasWidget)

* Tue Jun 17 2008 Owen Taylor <otaylor@redhat.com> - 0.2.33-1
- Update to 0.2.33 (Fixes problem with python bindings missing get_font() method)

* Mon Jun 16 2008 Owen Taylor <otaylor@redhat.com> - 0.2.32-1
- Update to 0.2.32

* Thu Apr 24 2008 Colin Walters <walters@redhat.com> - 0.2.31-1
- Update to 0.2.31

* Mon Mar 31 2008 Colin Walters <walters@redhat.com> - 0.2.30-1
- Update to 0.2.30

* Tue Feb 26 2008 Colin Walters <walters@redhat.com> - 0.2.26-1
- Update to 0.2.26

* Sat Feb  2 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.2.25-1
- Update to 0.2.25

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.2.24-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 13 2007 Owen Taylor <otaylor@redhat.com> - 0.2.24-1
- Update to 0.2.24

* Wed Jul 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.2.23-1
- Update to 0.2.23

* Mon Jul  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.2.22-1
- Update to 0.2.22

* Fri Jul  6 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.2.21-1
- Update to 0.2.21

* Wed Jun 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.2.19-1
- Update to 0.2.19
- Require gtk-doc

* Mon May 14 2007 Colin Walters <walters@redhat.com> - 0.2.17-3
- Hopefully make patch apply

* Fri May 11 2007 Colin Walters <walters@redhat.com> - 0.2.17-2
- Add patch to install python in pyexecdir. 

* Thu May 02 2007 Colin Walters <walters@redhat.com> - 0.2.17-1
- New upstream
- Package pc file
- Add BRs on pycairo-devel, pygtk-devel

* Mon Apr 30 2007 Colin Walters <walters@redhat.com> - 0.2.16-1
- New upstream

* Mon Apr 09 2007 Colin Walters <walters@redhat.com> - 0.2.13-2
- Fully qualify source url

* Tue Apr 03 2007 Colin Walters <walters@redhat.com> - 0.2.13-1
- Tweak for mugshot.org releases

* Tue Oct 03 2006 John (J5) Palmieri <johnp@redhat.com> - 0.1.2-1
- initial package
