#
# Conditional build:
%bcond_without	graphviz	# do not require graphviz in doc regeneration
#
Summary:	X protocol C-language Binding library
Summary(pl.UTF-8):	XCB - biblioteka dowiązań języka C do protokołu X
Name:		libxcb
Version:	1.4
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	b00fd506c717dea01f595e8da31f6914
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	check >= 0.9.4
BuildRequires:	doxygen
%if %{with graphviz}
BuildRequires:	graphviz
%endif
BuildRequires:	libtool
BuildRequires:	libpthread-stubs-devel >= 0.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	xcb-proto >= 1.5
BuildRequires:	xorg-lib-libXau-devel >= 0.99.2
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

libxcb provides an interface to the X Window System protocol, slated to
replace the current Xlib interface. It has several advantages over
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
Requires:	libpthread-stubs-devel >= 0.2
Requires:	xorg-lib-libXau-devel
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
%configure
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
%attr(755,root,root) %{_libdir}/libxcb*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb.so.1
%attr(755,root,root) %ghost %{_libdir}/libxcb-*.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/{manual,tutorial}
%attr(755,root,root) %{_libdir}/libxcb*.so
%{_libdir}/libxcb*.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb*.a
