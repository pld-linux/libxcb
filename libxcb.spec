#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	graphviz	# do not require graphviz in doc regeneration
#
Summary:	X protocol C-language Binding library
Summary(pl.UTF-8):	XCB - biblioteka dowiązań języka C do protokołu X
Name:		libxcb
Version:	1.10
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	074c335cc4453467eeb234e3dadda700
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	check >= 0.9.4
BuildRequires:	doxygen
%{?with_graphviz:BuildRequires:	graphviz}
BuildRequires:	libpthread-stubs >= 0.3
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	xcb-proto >= 1.10
BuildRequires:	xorg-lib-libXau-devel >= 0.99.2
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-proto-xproto-devel
Requires:	xorg-lib-libXau >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

libxcb provides an interface to the X Window System protocol, slated
to replace the current Xlib interface. It has several advantages over
Xlib, including:
- size: small library and lower memory footprint
- latency hiding: batch several requests and wait for the replies later
- direct protocol access: one-to-one mapping between interface and protocol
- proven thread support: transparently access XCB from multiple threads
- easy extension implementation: interfaces auto-generated from XML-XCB

Xlib can also use XCB as a transport layer, allowing software to make
requests and receive responses with both, which eases porting to XCB.
However, client programs, libraries, and toolkits will gain the most
benefit from a native XCB port.

%description -l pl.UTF-8
XCB - biblioteka dowiązań języka C do protokołu X.

libxcb udostępnia interfejs do protokołu X Window System, mający
zastąpić aktualny interfejs Xlib. Ma kilka zalet w stosunku do Xliba,
w tym:
- rozmiar: mała biblioteka i niewielki narzut pamięciowy
- ukrywanie opóźnień: kolejkowanie kilku żądań i oczekiwanie na
  odpowiedź później
- bezpośredni dostęp do protokołu: odwzorowanie 1-1 między interfejsem
  a protokołem
- sprawdzoną obsługę wątków: bezpośredni dostęp do XCB z wielu wątków
- łatwe implementowanie rozszerzeń: automatyczne generowanie
  interfejsów z XML-XCB

Xlib może także używać XCB jako warstwy transportowej, pozwalając
programom wykonywać żądania i odbierać odpowiedzi poprzez oba
interfejsy, co ułatwia przechodzenie na XCB. Jednak programy
klienckie, biblioteki i toolkity zyskają więcej na natywnym porcie
XCB.

%package devel
Summary:	Header files for XCB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpthread-stubs >= 0.3
Requires:	xorg-lib-libXau-devel >= 0.99.2
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-proto-xproto-devel

%description devel
Header files for XCB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB.

%package static
Summary:	Static XCB library
Summary(pl.UTF-8):	Statyczna biblioteka XCB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB.

%package apidocs
Summary:	XCB library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki XCB
Group:		Documentation

%description apidocs
API and internal documentation for XCB library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki XCB.

%prep
%setup -q
%if %{without graphviz}
%{__sed} -i -e 's/HAVE_DOT               = YES/HAVE_DOT               = NO/g' doc/xcb.doxygen.in
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-selinux \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libxcb

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libxcb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb.so.1
%attr(755,root,root) %{_libdir}/libxcb-composite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-composite.so.0
%attr(755,root,root) %{_libdir}/libxcb-damage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-damage.so.0
%attr(755,root,root) %{_libdir}/libxcb-dpms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-dpms.so.0
%attr(755,root,root) %{_libdir}/libxcb-dri2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-dri2.so.0
%attr(755,root,root) %{_libdir}/libxcb-dri3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-dri3.so.0
%attr(755,root,root) %{_libdir}/libxcb-glx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-glx.so.0
%attr(755,root,root) %{_libdir}/libxcb-present.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-present.so.0
%attr(755,root,root) %{_libdir}/libxcb-randr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-randr.so.0
%attr(755,root,root) %{_libdir}/libxcb-record.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-record.so.0
%attr(755,root,root) %{_libdir}/libxcb-render.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-render.so.0
%attr(755,root,root) %{_libdir}/libxcb-res.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-res.so.0
%attr(755,root,root) %{_libdir}/libxcb-screensaver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-screensaver.so.0
%attr(755,root,root) %{_libdir}/libxcb-shape.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-shape.so.0
%attr(755,root,root) %{_libdir}/libxcb-shm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-shm.so.0
%attr(755,root,root) %{_libdir}/libxcb-sync.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-sync.so.1
%attr(755,root,root) %{_libdir}/libxcb-xevie.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xevie.so.0
%attr(755,root,root) %{_libdir}/libxcb-xf86dri.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xf86dri.so.0
%attr(755,root,root) %{_libdir}/libxcb-xfixes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xfixes.so.0
%attr(755,root,root) %{_libdir}/libxcb-xinerama.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xinerama.so.0
%attr(755,root,root) %{_libdir}/libxcb-xkb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xkb.so.1
%attr(755,root,root) %{_libdir}/libxcb-xprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xprint.so.0
%attr(755,root,root) %{_libdir}/libxcb-xselinux.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xselinux.so.0
%attr(755,root,root) %{_libdir}/libxcb-xtest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xtest.so.0
%attr(755,root,root) %{_libdir}/libxcb-xv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xv.so.0
%attr(755,root,root) %{_libdir}/libxcb-xvmc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-xvmc.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/tutorial
%attr(755,root,root) %{_libdir}/libxcb.so
%attr(755,root,root) %{_libdir}/libxcb-composite.so
%attr(755,root,root) %{_libdir}/libxcb-damage.so
%attr(755,root,root) %{_libdir}/libxcb-dpms.so
%attr(755,root,root) %{_libdir}/libxcb-dri2.so
%attr(755,root,root) %{_libdir}/libxcb-dri3.so
%attr(755,root,root) %{_libdir}/libxcb-glx.so
%attr(755,root,root) %{_libdir}/libxcb-present.so
%attr(755,root,root) %{_libdir}/libxcb-randr.so
%attr(755,root,root) %{_libdir}/libxcb-record.so
%attr(755,root,root) %{_libdir}/libxcb-render.so
%attr(755,root,root) %{_libdir}/libxcb-res.so
%attr(755,root,root) %{_libdir}/libxcb-screensaver.so
%attr(755,root,root) %{_libdir}/libxcb-shape.so
%attr(755,root,root) %{_libdir}/libxcb-shm.so
%attr(755,root,root) %{_libdir}/libxcb-sync.so
%attr(755,root,root) %{_libdir}/libxcb-xevie.so
%attr(755,root,root) %{_libdir}/libxcb-xf86dri.so
%attr(755,root,root) %{_libdir}/libxcb-xfixes.so
%attr(755,root,root) %{_libdir}/libxcb-xinerama.so
%attr(755,root,root) %{_libdir}/libxcb-xkb.so
%attr(755,root,root) %{_libdir}/libxcb-xprint.so
%attr(755,root,root) %{_libdir}/libxcb-xselinux.so
%attr(755,root,root) %{_libdir}/libxcb-xtest.so
%attr(755,root,root) %{_libdir}/libxcb-xv.so
%attr(755,root,root) %{_libdir}/libxcb-xvmc.so
%{_libdir}/libxcb.la
%{_libdir}/libxcb-composite.la
%{_libdir}/libxcb-damage.la
%{_libdir}/libxcb-dpms.la
%{_libdir}/libxcb-dri2.la
%{_libdir}/libxcb-dri3.la
%{_libdir}/libxcb-glx.la
%{_libdir}/libxcb-present.la
%{_libdir}/libxcb-randr.la
%{_libdir}/libxcb-record.la
%{_libdir}/libxcb-render.la
%{_libdir}/libxcb-res.la
%{_libdir}/libxcb-screensaver.la
%{_libdir}/libxcb-shape.la
%{_libdir}/libxcb-shm.la
%{_libdir}/libxcb-sync.la
%{_libdir}/libxcb-xevie.la
%{_libdir}/libxcb-xf86dri.la
%{_libdir}/libxcb-xfixes.la
%{_libdir}/libxcb-xinerama.la
%{_libdir}/libxcb-xkb.la
%{_libdir}/libxcb-xprint.la
%{_libdir}/libxcb-xselinux.la
%{_libdir}/libxcb-xtest.la
%{_libdir}/libxcb-xv.la
%{_libdir}/libxcb-xvmc.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb*.pc
%{_mandir}/man3/xcb-examples.3*
%{_mandir}/man3/xcb-requests.3*
%{_mandir}/man3/xcb_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb.a
%{_libdir}/libxcb-composite.a
%{_libdir}/libxcb-damage.a
%{_libdir}/libxcb-dpms.a
%{_libdir}/libxcb-dri2.a
%{_libdir}/libxcb-dri3.a
%{_libdir}/libxcb-glx.a
%{_libdir}/libxcb-present.a
%{_libdir}/libxcb-randr.a
%{_libdir}/libxcb-record.a
%{_libdir}/libxcb-render.a
%{_libdir}/libxcb-res.a
%{_libdir}/libxcb-screensaver.a
%{_libdir}/libxcb-shape.a
%{_libdir}/libxcb-shm.a
%{_libdir}/libxcb-sync.a
%{_libdir}/libxcb-xevie.a
%{_libdir}/libxcb-xf86dri.a
%{_libdir}/libxcb-xfixes.a
%{_libdir}/libxcb-xinerama.a
%{_libdir}/libxcb-xkb.a
%{_libdir}/libxcb-xprint.a
%{_libdir}/libxcb-xselinux.a
%{_libdir}/libxcb-xtest.a
%{_libdir}/libxcb-xv.a
%{_libdir}/libxcb-xvmc.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/manual/*
%endif
